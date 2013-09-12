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
                          db = movespy_settings.moves_db)


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



#below this point functions are specific to caliper


def getClassAttr(output_folder):
    '''Parses the XML parameters files in a TransModeler simulation output folder.
    Returns a dictionary keyed by Class ID. Values are dictionaries with keys for
    class_name, and mass_metric_tonnes. 
    '''

    
    
    import xml.etree.ElementTree as ET

    
    convert2tonnes = {'lbs':0.000453592,
                      'kg': 0.001}

    def getclassmass(root):



        veh_attrib = root.findall(".//item[@name='VehicleAttributes']")

        assert len(veh_attrib) == 1

        veh_attrib = veh_attrib[0]

        result = {}

        cols = veh_attrib.find('cols')

        col = cols.find('col')

        units = col.attrib['unit']

        assert units in convert2tonnes #check both the units and that the mass appears on the first row

        rows = veh_attrib.find('rows').findall('row')

        for row in rows:
            veh_class = row.attrib['label']
            weight = float(row.find('v').text) #assume first row

            mass = weight * convert2tonnes[units] #lbs to metric tonnes

            result[veh_class] = mass

        return result

    def getclassname(root):

        class_names = root.findall(".//item[@name='ClassNames']")

        assert len(class_names) == 1

        class_names = class_names[0]

        result = {}

        
        rows = class_names.find('rows').findall('row')

        for row in rows:

            veh_class = row.find('./v[2]').text

            class_name = row.find('./v[3]').text

            result[veh_class] = class_name

        return result
        

    try:
        tree = ET.parse(os.path.join(output_folder, 'pm_project.xml'))
        root = tree.getroot()
        classmass = getclassmass(root)

    except:
        tree = ET.parse(os.path.join(output_folder, 'pm_system.xml'))
        root = tree.getroot()
        classmass = getclassmass(root)



    try:
        tree = ET.parse(os.path.join(output_folder, 'pm_project.xml'))
        root = tree.getroot()
        classname = getclassname(root)
    except:
        tree = ET.parse(os.path.join(output_folder, 'pm_system.xml'))
        root = tree.getroot()
        classname = getclassname(root)

    
    result = {}

    for k in classmass:
        result[k] = {'mass_metric_tonnes': classmass[k],
                     'class_name': classname[k]}

    return result




def getCaliperBinaryTable(loc):
    '''Parses a Caliper binary table (.bin) into a numpy record array. 

    loc: the path to the binary table.


    '''
    import csv
    import numpy
    
    def getNumpyFormat(type_, size):
        format_lookup =     {'I':{1:'i1',2:'i2',4:'i4'},
                            'S':{1:'i1',2:'i2',4:'i4'},
                            'R':{4:'f4',8:'f8'},
                            'F':{4:'f4',8:'f8'}}

        if type_ == 'C':
            return 'S'+str(size)
        else:
            return format_lookup[type_][size]



    def getCaliperCategories(data):

        result = {}

        data = list(data)

        data = data[44:] #skip header

        while len(data) >= 51:

            field_name = data[:51]

            field_name = reduce(lambda x, y: x + y, field_name, '')

            field_name = field_name.replace('\x00','')#?


            data = data[51:]

            
            pairs = [data.pop(0)]
        
            while True:

                if pairs[-1] == '\x00':
                    if (not data) or (data[0] == '\x00'):
                        break

                pairs.append(data.pop(0))


            pairs = reduce(lambda x, y: x + y, pairs, '')

            pairs = pairs.split('\x00')

            keys = pairs[0::2]

            values = pairs[1::2]


            
            result[field_name] = dict(zip(keys, values))

        return result







    names = []
    formats = []

    root, ext = os.path.splitext(loc)
    meta = csv.reader(open(root + '.dcb').readlines()[2:])
    for row in meta:
        names.append(row[0])  
        formats.append(getNumpyFormat(row[1], int(row[3])))


    data_file = open(root + '.bin','rb')

    a = numpy.fromfile(data_file, dtype = zip(names, formats))



    if os.path.exists(root + '.bxl'):

        import numpy.lib.recfunctions

        
        category_data = open(root + '.bxl').read()

        categories = getCaliperCategories(category_data)

        for field_name in categories:
            
            assert field_name in a.dtype.names


            num_chars = max(map(len,categories[field_name].values()))

            dtype = 'a{}'.format(num_chars)

            new_column = a[field_name].copy()

            new_column = [x.replace('\x001','') for x in new_column]####

            new_column = [categories[field_name][k] for k in new_column]


            a = numpy.lib.recfunctions.drop_fields(a, [field_name])

            a = numpy.lib.recfunctions.append_fields(a, field_name, new_column, dtype)


    return a
    

#todo: get grade from caliper


default_class_source = {    'AB': 42,
                            'B': 42,
                            'BK': None,
                            'M': 11,
                            'PC1': 21,
                            'PC2': 21,
                            'PC3': 21,
                            'PU': 31,
                            'ST': 52,
                            'T':None,
                            'TT':62}


def getOpModes(folder, simple = False, class_source = None):
    '''Gets the total vehicle-seconds for each combination of source type and
    operating mode from the output of a TransModeler simulation.

    The output must include a trajectory file in "standard" format with
    observations every one second.

    `class_source` is a dictionary mapping Class IDs to source type IDs. Optional.
    If not provided a default mapping will be used.

    `simple` indicates whether to use a simplified calculation for effect of grade.
    Optional. The default is False.

    Currently grade is always set to zero.

    '''

    import collections
    import movespy.trajectory

    if class_source is None:
        class_source = default_class_source

    

    

    traj_data = getCaliperBinaryTable(os.path.join(folder,'trajectory'))
    traj_data = traj_data[traj_data.argsort(order = ('ID','Time'))]
    
    trip_data = getCaliperBinaryTable(os.path.join(folder,'trips'))

    source_attr = getSourceAttr()

    class_attr = getClassAttr(folder)
    
    id_class = {}
    for row in trip_data:
        id_class[row['ID']] = row['Class']

    params = []
    source_types = []
    for row in traj_data:

        class_ = id_class[row['ID']]

        source = class_source[class_]
        source_types.append(source)
        
        grade_percent = 0.

        mass_tonnes = class_attr[class_]['mass_metric_tonnes']

        mass_factor = source_attr[source]['mass_factor']
        alpha = source_attr[source]['alpha']
        beta = source_attr[source]['beta']
        gamma = source_attr[source]['gamma']


        params.append([grade_percent, mass_tonnes, mass_factor, alpha, beta, gamma])


    grade_percent, mass_tonnes, mass_factor, alpha, beta, gamma = zip(*params)


    opmode = movespy.trajectory.getVSPOpMode(traj_data['ID'],
                                                  traj_data['Speed'],
                                                  grade_percent,
                                                  mass_tonnes,
                                                  mass_factor,
                                                  alpha,
                                                  beta,
                                                  gamma,
                                                  simple)[1]

    return collections.Counter(zip(source_types, opmode))




def getTotalEmissions(opmodes, ratetable):

    '''Calculate total emissions based on an opmode/source type distribution and a rate table.
    Returns a dictionary keyed by pollutant ID. Values are total emissions quantities
    in either grams or kJ.

    Parameters

    opmodes: an opmode distribution as returned by getOpModes

    ratetable: a rate table as returned by ratetable.getRateTable 
    '''


    result = {}

    for pollutant in ratetable:
        total = 0.
        for (source_type, opmode), seconds in opmodes.items():
            try:
                rate = ratetable[pollutant][source_type][opmode]
            except:
                print pollutant, source_type, opmode
                assert 0
            hours = seconds / 3600.

            total += rate * hours

        result[pollutant] = total

    return result





def calcEmissions(folders, ratetable, simple = False, class_source = None, **args):
    '''Calculate total emissions for each of several simulations, using multiprocessing.

    folders: a sequence of paths for folders containing simulation outputs.

    rate table: ratetable: a rate table as returned by ratetable.getRateTable

    `class_source` is a dictionary mapping Class IDs to source type IDs. Optional.
    If not provided a default mapping will be used.

    `simple` indicates whether to use a simplified calculation for effect of grade.
    Optional. The default is False.

    **args: keyword arguments that are passed on to initialize an instance of
    multiprocessing.Pool. Defaults to one process. Provide a processes argument
    to increase the number of processes.

    '''




    import functools

    import multiprocessing



    getOpModes2 = functools.partial(getOpModes,
                                   simple = simple,
                                   class_source = class_source)   

    pool = multiprocessing.Pool(**args)

    opmode_distrs = pool.map(getOpModes2, folders)
  
    result = {}
    for folder, opmodes in zip(folders, opmode_distrs):
        total_emissions = getTotalEmissions(opmodes, ratetable)
        result[folder] = total_emissions

    return result

    





    
    

    
        

    





    


    

    
