
import moves
reload(moves)

def getRateTable(activity,
                 operating_mode_ids = None,
                 source_type_ids = None):


    '''Get an emissions rate lookup table.

    Returns a nested dict keyed by pollutant, source type and opmode

    All values are for one vehicle hour

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

        b = a.setdefault(sourcetype, {})

        b[opmode] = quantity


    return ratetable

                

def getAverageSpeedRateTable(activity,
                 roadtype_grade_speed,
                 source_type_ids = None):


    '''Get an emissions rate lookup table.

    Returns a nested dict keyed by pollutant, source type, roadtype, grade, speed

    All values are for one vehicle hour

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

                
##        a = ratetable.setdefault(pollutant, {})
##
##        b = a.setdefault(sourcetype, {})
##
##        b[opmode] = quantity
       


if __name__ == "__main__":
    import datetime

##    start = datetime.datetime.now()
##
##
##    activity =  {'age_distr': dict.fromkeys((11,21,31,32,41,42,43,51,52,53,54,61,62),
##                                            {5: 1.0}),
##                 'county': 50027,
##                 'day_type': 5,
##                 'hour': 16,
##                 'month': 6,
##                 'year': 2015}
##
##
##    table =  getRateTable(activity)
##
##    end = datetime.datetime.now()
##    print 'elapsed time:', (end - start).total_seconds()
##
##    #884 seconds or about 15 minutes for all source types and op modes


    start = datetime.datetime.now()


    activity =  {'age_distr': dict.fromkeys((11,21,31,32,41,42,43,51,52,53,54,61,62),
                                            {5: 1.0}),
                 'county': 50027,
                 'day_type': 5,
                 'hour': 16,
                 'month': 6,
                 'year': 2015}


    table =  getAverageSpeedRateTable(activity,
                                      [(5, 1., 20.),(4, 1., 50.)])

    end = datetime.datetime.now()
    print 'elapsed time:', (end - start).total_seconds()

    # seconds or about 15 minutes for all source types and op modes    

    



    

        


        


    
