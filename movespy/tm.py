

import movespy.utils
import movespy.trajectory
import os.path


    
def getClassAttr(output_folder):
    '''Parses the XML parameters files in a TransModeler simulation output folder.
    Returns a dictionary keyed by Class ID. Values are dictionaries with keys for
    class_name, and mass_tonnes. 
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
        result[k] = {'mass_tonnes': classmass[k],
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






def getOpModeDistr(folder, simple = False, class_source = None):
    '''Gets the total vehicle-seconds for each combination of source type and
    operating mode from the output of a TransModeler simulation.

    The output must include a trajectory file in "standard" format with
    observations every one second, and speeds in miles per hour.

    `class_source` is a dictionary mapping Class IDs to source type IDs. Optional.
    If not provided a default mapping will be used.

    `simple` indicates whether to use a simplified calculation for effect of grade.
    Optional. The default is False.

    Currently grade is always set to zero.

    '''

    trip_data = getCaliperBinaryTable(os.path.join(folder,'trips'))

    if class_source is None:
        class_source = default_class_source

    source_attr = movespy.utils.getSourceAttr()

    class_attr = getClassAttr(folder)
    
    veh_attr = {}
    for row in trip_data:

        class_ = row['Class']
        
        attr = class_attr[class_].copy()
        
        source_type = class_source[row['Class']]

        attr['source_type'] = source_type

        attr.update(source_attr[source_type])

        veh_attr[row['ID']] = attr

    traj_data = getCaliperBinaryTable(os.path.join(folder,'trajectory'))
    traj_data = traj_data[traj_data.argsort(order = ('ID','Time'))]

    grade_percent = [0.] * len(traj_data) #todo: get grade from caliper

    opmode_distr = movespy.utils.getOpModeDistr(traj_data['ID'],
                                                 traj_data['Speed'],
                                                 grade_percent,
                                                 veh_attr,
                                                 simple)

    return opmode_distr
                                                 



