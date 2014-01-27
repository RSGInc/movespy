import datetime
import movespy.utils
import movespy.ratetable

def test_average_speed_run():

    start = datetime.datetime.now()


    age_distr = {0: 0.2,
                 1: 0.15,
                 2: 0.1,
                 3: 0.1,
                 4: 0.1,
                 5: 0.07,
                 6: 0.05,
                 7: 0.05,
                 8: 0.05,
                 9: 0.02,
                 10: 0.02,
                 11: 0.01,
                 12: 0.01,
                 13: 0.01,
                 14: 0.01,
                 15: 0.01,
                 16: 0.01,
                 17: 0.01,
                 18: 0.01,
                 19: 0.01}




    links = {1: {'grade': 0.857,
                 'length': 0.997,
                 'road_type': 3, 
                 'source_distr': {62:1.0}, 
                 'speed': 28.5,
                 'volume': 100},
             2: {'grade': -0.857,
                 'length': 0.997,
                 'road_type': 3, 
                 'source_distr': {62:1.0}, 
                 'speed': 28.5,
                 'volume': 10}}


    #the example has an in consistency: uses hour 23, but the meteorology table uses
    #default temperature and humidity for hour 13
    activity =  {'age_distr': {62:age_distr},
                 'county': 26161, 
                 'day_type': 5, 
                 'hour': 13, 
                 'month': 1,
                 'year': 2009,
                 'links': links}



    options = {'detail': 'average',
               'breakdown': ['process'],
               'pollutants':[3]}

    import movespy.moves

    m = movespy.moves.Moves(activity, options)

    output = m.run(0)

    rows = list(output)


    # the example only sums emissions from the running processs
    # movespy doesn't allow limiting processes, so we have to limit it here:
    result = sum([row['quantity'] for row in rows if (row['pollutant'] == 3) and row['process'] == 1])

    elapsed_time = (datetime.datetime.now() - start).total_seconds() / 60.

    target_value = 1696.47 + 117.47
    error_ratio = result / target_value

    if abs(1 - error_ratio) < 1e-6:
        status =  'SUCCEEDED'
    else:
        status =  'FAILED'



    print status
    print 'target value:', target_value
    print 'estimated value:', result
    print 'error ratio:', error_ratio
    print 'elapsed time (minutes):', elapsed_time

#next step: add ability to run drive schedule
#run moves with drive schedule from example
#compare with results from example and
#compare with lookup table approach
#this will test vsp calculation, opmode calculation, lookup table construction


def test_driveschedule_run():

    start = datetime.datetime.now()


    age_distr = {0: 0.2,
                 1: 0.15,
                 2: 0.1,
                 3: 0.1,
                 4: 0.1,
                 5: 0.07,
                 6: 0.05,
                 7: 0.05,
                 8: 0.05,
                 9: 0.02,
                 10: 0.02,
                 11: 0.01,
                 12: 0.01,
                 13: 0.01,
                 14: 0.01,
                 15: 0.01,
                 16: 0.01,
                 17: 0.01,
                 18: 0.01,
                 19: 0.01}




    links = {1: {'grade': 0.857,
                 'length': 0.997,
                 'road_type': 3, 
                 'source_distr': {62:1.0}, 
                 'speed': 28.5,
                 'volume': 100},
             2: {'grade': -0.857,
                 'length': 0.997,
                 'road_type': 3, 
                 'source_distr': {62:1.0}, 
                 'speed': 28.5,
                 'volume': 10}}




    drive_schedules = {1: [(30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 0.5), (30.0, 0.5), (30.0, 0.5), (30.0, 0.5), (30.0, 0.25), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.5), (30.0, 2.0), (30.0, 2.0), (30.0, 2.0), (30.0, 2.0), (30.0, 2.0), (30.0, 2.0), (30.0, 2.0), (30.0, 2.0), (30.0, 2.0), (30.0, 2.0), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 0.5), (30.0, 0.5), (30.0, 0.5), (30.0, 0.0), (28.0, 0.0), (25.0, 0.0), (21.0, 0.0), (16.0, 0.0), (9.0, 0.0), (5.0, 0.0), (4.0, 0.0), (1.0, 0.0), (0.0, 0.0), (0.0, 0.0)], 2: [(0.0, 0.0), (0.0, 0.0), (1.0, 0.0), (4.0, 0.0), (5.0, 0.0), (9.0, 0.0), (16.0, 0.0), (21.0, 0.0), (25.0, 0.0), (28.0, 0.0), (30.0, 0.0), (30.0, -0.5), (30.0, -0.5), (30.0, -0.5), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -2.0), (30.0, -2.0), (30.0, -2.0), (30.0, -2.0), (30.0, -2.0), (30.0, -2.0), (30.0, -2.0), (30.0, -2.0), (30.0, -2.0), (30.0, -2.0), (30.0, -1.5), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, -0.25), (30.0, -0.5), (30.0, -0.5), (30.0, -0.5), (30.0, -0.5), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0)]}


    links[1]['driveschedule'] = drive_schedules[1]
    links[2]['driveschedule'] = drive_schedules[2]




    #the example has an in consistency: uses hour 23, but the meteorology table uses
    #default temperature and humidity for hour 13
    activity =  {'age_distr': {62:age_distr},
                 'county': 26161, 
                 'day_type': 5, 
                 'hour': 13, 
                 'month': 1,
                 'year': 2009,
                 'links': links}



    options = {'detail': 'driveschedule',
               'breakdown': ['process'],
               'pollutants':[3]}





    import movespy.moves

    m = movespy.moves.Moves(activity, options)

    output = m.run(0)

    rows = list(output)


    # the example only sums emissions from the running processs
    # movespy doesn't allow limiting processes, so we have to limit it here:
    result = sum([row['quantity'] for row in rows if (row['pollutant'] == 3) and row['process'] == 1])

    elapsed_time = (datetime.datetime.now() - start).total_seconds() / 60.

    target_value = 1266.54 + 57.73
    error_ratio = result / target_value

    if abs(1 - error_ratio) < 1e-5:
        status =  'SUCCEEDED'
    else:
        status =  'FAILED'



    print status
    print 'target value:', target_value
    print 'estimated value:', result
    print 'error ratio:', error_ratio
    print 'elapsed time (minutes):', elapsed_time



def test_lookuptable_approach():

    start = datetime.datetime.now()

    import collections

    opmode_distr = collections.Counter()

    opmode_distr.update({0:700,
        1:200,
        11:100,
        22:2800,
        23:7800,
        24:1000})

    opmode_distr.update({1:20,
        12:20,
        13:10,
        16:30,
        21:810,
        22:340,
        29:10,
        30:20})

            


    opmode_distr = {62:dict(opmode_distr)}

    age_distr = {0: 0.2,
         1: 0.15,
         2: 0.1,
         3: 0.1,
         4: 0.1,
         5: 0.07,
         6: 0.05,
         7: 0.05,
         8: 0.05,
         9: 0.02,
         10: 0.02,
         11: 0.01,
         12: 0.01,
         13: 0.01,
         14: 0.01,
         15: 0.01,
         16: 0.01,
         17: 0.01,
         18: 0.01,
         19: 0.01}


    activity =  {'age_distr': {62:age_distr},
                 'county': 26161, 
                 'day_type': 5, 
                 'hour': 13, 
                 'month': 1,
                 'year': 2009}

    options = {'breakdown': ['process']}


    ratetable = movespy.ratetable.getRateTable(activity,
                                               options,
                                               source_type_ids = [62])


    ratetable = filter(lambda x: x['process'] == 1, ratetable)

    result =  movespy.utils.getTotalEmissions(opmode_distr, ratetable)[3]

    


    elapsed_time = (datetime.datetime.now() - start).total_seconds() / 60.

    target_value = 1266.54 + 57.73
    error_ratio = result / target_value

    if abs(1 - error_ratio) < 1e-3:
        status =  'SUCCEEDED'
    else:
        status =  'FAILED'



    print status
    print 'target value:', target_value
    print 'estimated value:', result
    print 'error ratio:', error_ratio
    print 'elapsed time (minutes):', elapsed_time




def test_lookuptable_approach2():

    start = datetime.datetime.now()
    
    drive_schedules = {1: [(30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 0.5), (30.0, 0.5), (30.0, 0.5), (30.0, 0.5), (30.0, 0.25), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.5), (30.0, 2.0), (30.0, 2.0), (30.0, 2.0), (30.0, 2.0), (30.0, 2.0), (30.0, 2.0), (30.0, 2.0), (30.0, 2.0), (30.0, 2.0), (30.0, 2.0), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.5), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.25), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 1.0), (30.0, 0.5), (30.0, 0.5), (30.0, 0.5), (30.0, 0.0), (28.0, 0.0), (25.0, 0.0), (21.0, 0.0), (16.0, 0.0), (9.0, 0.0), (5.0, 0.0), (4.0, 0.0), (1.0, 0.0), (0.0, 0.0), (0.0, 0.0)], 2: [(0.0, 0.0), (0.0, 0.0), (1.0, 0.0), (4.0, 0.0), (5.0, 0.0), (9.0, 0.0), (16.0, 0.0), (21.0, 0.0), (25.0, 0.0), (28.0, 0.0), (30.0, 0.0), (30.0, -0.5), (30.0, -0.5), (30.0, -0.5), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.25), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -1.5), (30.0, -2.0), (30.0, -2.0), (30.0, -2.0), (30.0, -2.0), (30.0, -2.0), (30.0, -2.0), (30.0, -2.0), (30.0, -2.0), (30.0, -2.0), (30.0, -2.0), (30.0, -1.5), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, 0.0), (30.0, -0.25), (30.0, -0.5), (30.0, -0.5), (30.0, -0.5), (30.0, -0.5), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0), (30.0, -1.0)]}

    drive_schedules.pop(2)

    veh = []

    vols = {1:100,
            2:10}


    veh_id = 0
    for k, v in sorted(drive_schedules.items()):
        for i in range(vols[k]):
            veh_id += 1
            veh.extend([veh_id] * len(v))


    speed_mph = []
    grade_percent = []

    for k, v in sorted(drive_schedules.items()):
        for i in range(vols[k]):
            speed_mph.extend(zip(*v)[0])
            grade_percent.extend(zip(*v)[1])

    source_attr = movespy.utils.getSourceAttr()[62]

    source_attr['source_type'] = 62
    source_attr['mass_tonnes'] = source_attr['default_mass']

    veh_attr = dict.fromkeys(set(veh), source_attr)

    opmode_distr =  movespy.utils.getOpModeDistr(veh, speed_mph, grade_percent, veh_attr)


    age_distr = {0: 0.2,
         1: 0.15,
         2: 0.1,
         3: 0.1,
         4: 0.1,
         5: 0.07,
         6: 0.05,
         7: 0.05,
         8: 0.05,
         9: 0.02,
         10: 0.02,
         11: 0.01,
         12: 0.01,
         13: 0.01,
         14: 0.01,
         15: 0.01,
         16: 0.01,
         17: 0.01,
         18: 0.01,
         19: 0.01}


    activity =  {'age_distr': {62:age_distr},
                 'county': 26161, 
                 'day_type': 5, 
                 'hour': 13, 
                 'month': 1,
                 'year': 2009}

    options = {'breakdown': ['process']}


    ratetable = movespy.ratetable.getRateTable(activity,
                                               options,
                                               source_type_ids = [62])


    ratetable = filter(lambda x: x['process'] == 1, ratetable)

    result =  movespy.utils.getTotalEmissions(opmode_distr, ratetable)[3]

    elapsed_time = (datetime.datetime.now() - start).total_seconds() / 60.

    target_value = 1266.54 + 57.73
    error_ratio = result / target_value

    if abs(1 - error_ratio) < 1e-2:
        status =  'SUCCEEDED'
    else:
        status =  'FAILED'



    print status
    print 'target value:', target_value
    print 'estimated value:', result
    print 'error ratio:', error_ratio
    print 'elapsed time (minutes):', elapsed_time


    #for link one, the differences are due to two missplaced seconds (out of 126 seconds)
    #I think the op modes are different because of floating point math


    
    





    



    

    

    

    


    


if __name__ == "__main__":


    test_average_speed_run()
    test_driveschedule_run()
    test_lookuptable_approach()
    test_lookuptable_approach2()



