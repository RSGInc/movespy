# Copyright (c) 2013, Resource Systems Group, Inc.
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met:
# 
#     - Redistributions of source code must retain the above copyright notice, 
#       this list of conditions and the following disclaimer.
#     
#     - Redistributions in binary form must reproduce the above copyright notice, 
#       this list of conditions and the following disclaimer in the documentation 
#       and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
# POSSIBILITY OF SUCH DAMAGE.


''' This module defines two functions:

- getRateTable
- getAverageSpeedRateTable

Use these functions to generate lookup tables for emissions rates. 

'''



import moves


def getRateTable(activity,
                 operating_mode_ids = None,
                 source_type_ids = None):

    '''Get an emissions rate lookup table.

    Parameters

    
    - activity: a dictionary structured exactly like the activity paramter
      to the moves.Moves initializer, except that it does not have the `links` key.

    - operating_mode_ids: a sequence of operating mode IDs to be included in the lookup
      table. Optional; if it is not included all operating modes
      will be included. Limiting the number of operating modes will make
      this function go faster

    - source_type_ids: as above, but for source type IDs. 


    Return Value

    Returns a nested dict keyed by pollutant, source type and opmode.
    All values are for one vehicle hour, and are either in grams or kJ. 

    Example::

        activity =  {'age_distr': dict.fromkeys((11,21,31,32,41,42,43,51,52,53,54,61,62),
                                            {5: 1.0}),
                     'county': 50027,
                     'day_type': 5,
                     'hour': 16,
                     'month': 6,
                     'year': 2015}


        table =  getRateTable(activity)


    '''

    

    if operating_mode_ids is None:
        operating_mode_ids = (0,1,11,12,13,14,15,16,21,22,23,24,25,
                      27,28,29,30,33,35,37,38,39,40,501)

    if source_type_ids is None:
        source_type_ids = (11,21,31,32,41,42,43,51,52,53,54,61,62)
        

    sourcetypeshare = 1.0 / len(source_type_ids)

    activity['links'] = None

    linkid = 5
    link_lookup = {}
    links = {}
    
    for opmode in operating_mode_ids:

        link_lookup[linkid] = opmode


        link = {'grade': 0.,
                'length': 15.,
                'road_type': 5,
                'speed': 30.,
                'volume': 2.} #one vehicle hour

        link['source_distr'] = dict.fromkeys(source_type_ids, sourcetypeshare)

        link['opmode_distr'] = dict.fromkeys(source_type_ids, {opmode:1.0})

        links[linkid] = link

        linkid += 1

    activity['links'] = links


    options = {'detail':'opmode',
               'breakdown':['source']}



    m = moves.Moves(activity, options)

    moves_out = m.run()
    

    ratetable = {}

    for row in moves_out:
        linkid = row['link']

        opmode = link_lookup[linkid]

        sourcetype = row['source']
        pollutant = row['pollutant']

        if row['quantity'] is None:
            quantity = 0.0
        else:
            quantity = row['quantity'] / sourcetypeshare

        a = ratetable.setdefault(pollutant, {})

        b = a.setdefault(sourcetype, dict.fromkeys(operating_mode_ids, 0.0))
        
        b[opmode] = quantity


    return ratetable

                

def getAverageSpeedRateTable(activity,
                 roadtype_grade_speed,
                 source_type_ids = None):


    '''Get an emissions rate lookup table.

    Parameters

    
    - activity: a dictionary structured exactly like the activity paramter
      to the moves.Moves initializer, except that it does not have the `links` key.

    - roadtype_grade_speed: a sequence of tuples. Each is tuple of road type id,
      grade, and speed. Road type IDs can be found in the MOVES database. Grade
      is given in percent, and speed in miles per hour. 

    - source_type_ids: a sequence of source type IDs to be included in the lookup
      table. Optional; if it is not given all source types
      will be included. Limiting the number of source types will make
      this function go faster


    Return Value

    Returns a nested dict keyed by pollutant, source type, roadtype, grade, speed
    All values are for one vehicle hour, and are either in grams or kJ.


    Example::

        activity =  {'age_distr': dict.fromkeys((11,21,31,32,41,42,43,51,52,53,54,61,62),
                                            {5: 1.0}),
                     'county': 50027,
                     'day_type': 5,
                     'hour': 16,
                     'month': 6,
                     'year': 2015}


        table =  getAverageSpeedRateTable(activity,
                                      [(5, 1., 20.),(4, 1., 50.)])

    

    '''

    if source_type_ids is None:
        source_type_ids = (11,21,31,32,41,42,43,51,52,53,54,61,62)
        

    sourcetypeshare = 1.0 / len(source_type_ids)

    activity['links'] = None

    linkid = 5
    link_lookup = {}
    links = {}
    
    for roadtype, grade, speed in roadtype_grade_speed:

        link_lookup[linkid] = dict(roadtype = roadtype,
                                   grade = grade,
                                   speed = speed)


        link = {'grade': float(grade),
                'length': float(speed) / 2.,
                'road_type': roadtype,
                'speed': float(speed), #was 30
                'volume': 2.} #one vehicle hour

        link['source_distr'] = dict.fromkeys(source_type_ids, sourcetypeshare)

        links[linkid] = link

        linkid += 1

    activity['links'] = links


    options = {'detail':'average',
               'breakdown':['source']}



    m = moves.Moves(activity, options)

    moves_out = m.run()
    

    ratetable = {}

    for row in moves_out:
        linkid = row['link']

        roadtype = link_lookup[linkid]['roadtype']
        grade = link_lookup[linkid]['grade']
        speed = link_lookup[linkid]['speed']

        sourcetype = row['source']
        pollutant = row['pollutant']

        if row['quantity'] is None:
            quantity = 0.0
        else:
            quantity = row['quantity'] / sourcetypeshare

        a = ratetable.setdefault(pollutant, {})

        b = a.setdefault(sourcetype, {})

        c = b.setdefault(roadtype, {})

        d = c.setdefault(grade, {})

        d[speed] = quantity



    return ratetable

                


    



    

        


        


    
