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

''' Functions for calculating total emissions from each of a collection
of simulations.

Eaxmple::


    import movespy.ratetable
    import movespy.moves
    import os.path


    #create an emissions rate lookup table

    year = 2010

    age_distr = movespy.moves.getDefaultAgeDistribution(year)

    activity = {'year':year, 'county':50027, 'month':11,
                'hour': 7, 'day_type': 5, 'age_distr':age_distr}

    ratetable = movespy.ratetable.getRateTable(activity)


    #calculate opmode distributions for 30 different simulations

    outputfolder = (r'Q:\Projects\NH\UNH & Durham\2013 model update'
                    r'\2013 TransModeler Files\after Steve P. tweaks'
                    r'\Trajectories\Build')

    folders = os.walk(outputfolder).next()[1]

    folders = [os.path.join(outputfolder, f) for f in folders]


    #combine opmode distributions and the rate table to calculate total emissions
    a = calcEmissions(folders, ratetable, processes = 4)

'''

import os.path
import movespy.trajectory
import itertools
import collections

def getOpModeDistr(veh, speed_mph, grade_percent, veh_attr, simple = False):
    '''given vehicle trajectory data and vehicle attributes information
    calculate the opmode distribution. The returned value is like the
    opmode_distr element of the moves activity argument, but gives total
    seconds rather than time proportions. (I may change this in the future
    to be consistant with the activity argument. In that case I would also need
    to return total seconds for each source type? or source type distribution
    and total seconds overall)


      - `veh`: a sequence of vehicle IDs
      - `speed_mph`: current speed (miles per hour)
      - `grade_percent`: current grade (percent)
      - `veh_attr`: a dictionary keyed by vehicle id. Values
         are dictionaries with the following keys: source_type, mass_tonnes,
         mass_factor, alpha, beta, gamma
      - `simple`: Boolean indicating whether to use simplified grade calculation

    '''

    params = []
    source_types = []
    for veh_id in veh:

        source_types.append(veh_attr[veh_id]['source_type'])


        mass_tonnes = veh_attr[veh_id]['mass_tonnes']

        mass_factor = veh_attr[veh_id]['mass_factor']
        alpha = veh_attr[veh_id]['alpha']
        beta = veh_attr[veh_id]['beta']
        gamma = veh_attr[veh_id]['gamma']


        params.append([mass_tonnes, mass_factor, alpha, beta, gamma])


    mass_tonnes, mass_factor, alpha, beta, gamma = zip(*params)


    opmodes = movespy.trajectory.getVSPOpMode(veh,
                                                  speed_mph,
                                                  grade_percent,
                                                  mass_tonnes,
                                                  mass_factor,
                                                  alpha,
                                                  beta,
                                                  gamma,
                                                  simple)[1]


    opmode_distr = {}

    groups = itertools.groupby(sorted(zip(source_types, opmodes)),
                               lambda x: x[0])

    for source_type, omd in groups:

        omd = zip(*list(omd))[1]

        omd = dict(collections.Counter(omd))

        opmode_distr[source_type] = omd


    return opmode_distr


def getTotalEmissions(opmode_distr, ratetable):

    '''Calculate total emissions based on an opmode/source type distribution and a rate table.
    Returns a dictionary keyed by pollutant ID. Values are total emissions quantities
    in either grams or kJ.

    Parameters

    opmode_distr: an opmode distribution as returned by getOpModeDistr

    ratetable: a rate table as returned by ratetable.getRateTable
    '''


    result = {}



    for source in opmode_distr:
        for opmode, seconds in opmode_distr[source].items():
            rows = filter(lambda x: all([x['source'] == source,
                                         x['opmode'] == opmode]),
                          ratetable)



            hours = seconds / 3600.
            for row in rows:

                pollutant = row['pollutant']




                rate = row['quantity']

                total = rate * hours

                result.setdefault(pollutant, 0.0)

                result[pollutant] += total


    return result


def getSourceAttr():

    '''Queries the moves database to get source use type attributes.
    Returns a dictionary keyed by source use type ID. Values
    are dictionaries with keys sourcename, massfactor, alpha, beta, gamma
    and default mass. Mass is in metric tonnes.
    '''



    #I noticed that the most recent moves db has a new table that has vsp params
    #that vary by model year - this is not addressed here or anywhere else (yet)

    import MySQLdb

    import movespy_settings

    con = MySQLdb.connect(host = 'localhost',
                          db = movespy_settings.moves_db,
                          user = movespy_settings.user_name,
                          passwd = movespy_settings.password)

    cur = con.cursor()

    cur.execute('''select sourceTypeID, sourceTypeName, fixedMassFactor,
                   rollingTermA, rotatingTermB, dragTermC, sourceMass from sourceusetype''')

    result = {}

    for sourceusetype, sourcename, mass_factor, alpha, beta, gamma, default_mass in cur:


        result[sourceusetype] = dict(sourcename = sourcename,
                                     mass_factor = mass_factor,
                                     alpha = alpha,
                                     beta = beta,
                                     gamma = gamma,
                                     default_mass = default_mass)

    return result
