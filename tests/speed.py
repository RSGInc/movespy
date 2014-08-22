




#average speed approach
#may be fast, depending on number links (dissagregation)


#link drive schedule approach (one link for every vehicle)
#takes way to long

#opmode -> moves approach
#may be fast, depending on number links (dissagregation)

def test():

    import movespy.tm
    import datetime
    import movespy.moves

    age_distr = movespy.moves.getDefaultAgeDistribution(2015)


    output_folder = r'C:\Users\eric.talbot\movespy\movespy\tests\data\20130730105509'


    start = datetime.datetime.now()

    opmode_distr = movespy.tm.getOpModeDistr(output_folder)


    print datetime.datetime.now() - start



    
    source_distr = {}


    for sourcetype, distr in opmode_distr.items():
        total_seconds = float(sum(distr.values()))

        source_distr[sourcetype] = total_seconds

        for opmode, v in distr.items():
            opmode_distr[sourcetype][opmode] = v / total_seconds


    total_seconds = float(sum(source_distr.values()))

    total_hours = total_seconds / 3600.


    for k,v in source_distr.items():
        source_distr[k] = v / total_seconds


    import pprint
    pprint.pprint(source_distr)

    pprint.pprint(opmode_distr)

        
    links = {1: {'grade': 0.0,
             'length': 15.,
             'road_type': 5, #5 is the ID for an urban non-freeway
             'source_distr': source_distr,
             'speed': 30.,
             'volume': 2. * total_hours,
                 'opmode_distr': opmode_distr}}

    activity =  {'age_distr': age_distr,
             'county': 50027, 
             'day_type': 5, 
             'hour': 16,
             'month': 6,
             'year': 2015,
             'links': links} 

    options = {'detail': 'opmode'}        


    moves = movespy.moves.Moves(activity, options)

    emissions_out = moves.run()


    total_CO = sum([row['quantity'] for row in emissions_out if row['pollutant'] == 2])

    print total_CO

    print datetime.datetime.now() - start


    options = {'detail': 'average'}        


    moves = movespy.moves.Moves(activity, options)

    emissions_out = moves.run()


    total_CO = sum([row['quantity'] for row in emissions_out if row['pollutant'] == 2])

    print total_CO

    print datetime.datetime.now() - start
            




#opmode -> look up table approach
#for many links (high dissagregation) this is probably faster


if __name__ == "__main__":
    import sys

    sys.path.insert(0, '..')

    test()


