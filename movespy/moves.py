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

''' This module defines one class and one function:

- Moves: a class for running MOVES.
- getDefaultAgeDistribution: a function for retrieving a national-level
  default age distribution from MOVES

How to Use this Module
======================


1. Import the module: ``import movespy.moves``
2. Construct the initializer parameters (`activity` and `options`) for the `Moves` class.
   (See *Moves Class Initializer Parameters* for details on the structure of these
   parameters.)
3. If needed, generate a default
   age distribution for your `activity` parameter by using `getDefaultAgeDistribution`.
4. Create an instance of the `Moves` class: ``m = movespy.moves.Moves(activity, options)``
5. Run MOVES: ``emission_out = m.run()``
6. Use the output: ``print emission_out.next()``
'''

import os
import xml.etree.ElementTree as et
import subprocess
import datetime

import MySQLdb

import templates
import movespy_settings



class Output(object):
    '''The output from a MOVES run.

    An iterator over the rows of the movesoutput table.
    Rows are returned as dictionaries.
    
    Can only be iterated over once.

    If cleanup is True, then the output database is dropped
    upon Python garbage collection.

    The field attribute is a convenient way to get the
    keys that each dictionary will have without retrieving
    any rows. 
        
    '''

    

    def __init__(self, cur, db, cleanup, fields):
        self.cleanup = cleanup
        self.cur = cur
        self.db = db
        self.fields = fields

    def __del__(self):
        if self.cleanup:
            self.cur.execute('drop database %s'%self.db)

    def __iter__(self):
        return self.cur

    def next(self):
        return self.cur.next()


    

        

    
		



class Moves(object):
    '''This is the class to use to run MOVES.
    Just initialize an instance, then call the run method. For example:

    >>> links = {1: {'grade': -1.2,
                     'length': 0.25,
                     'road_type': 3,
                     'source_distr': {21: 1.0},
                     'speed': 34,
                     'volume': 400}}
    >>> activity =  {'age_distr': {21: {5: 1.0}},
                     'county': 50027,
                     'day_type': 5,
                     'hour': 16,
                     'month': 6,
                     'year': 2015,
                     'links': links}
    >>> options = {'detail': 'average'}
    >>> m = Moves(activity, options)
    >>> emissions_out = m.run()
        
    '''


    tablenames = ['links', 'source_distr', 'age_distr', 'fuel_supply', 'fuel_form', 'meteor', 'opmode_distr', 'drive_schedule']

    tablepaths = ['link/parts/link/filename',
                           'linksourcetypehour/parts/linkSourceTypeHour/filename',
                           'agedistribution/parts/sourceTypeAgeDistribution/filename',
                           'fuel/parts/FuelSupply/filename',
                           'fuel/parts/FuelFormulation/filename',
                           'zonemonthhour/parts/zoneMonthHour/filename',
                           'linkopmodedistribution/parts/opModeDistribution/filename',
                  'driveschedulesecondlink/parts/driveScheduleSecondLink/filename']

    process_pollutant = {1:(1,2,3,30,91,101,102,111,112),
                     9:(116,),
                     10:(117,)}

    


    @staticmethod
    def _hourToHourID(hour):
        return int(hour) + 1


    def __init__(self, activity, options):
        '''Use this initializer to set up a MOVES run. The
        activity parameter describes the vehicle activity that you are
        modeling, and the options parameter controls how the model runs.
        Each of these parameters is a nested dictionary; to learn the
        structure for these dictionaries see
        *Moves Class Initializer Parameters*.
        '''
        

        self.activity = activity
        self.options = options

        self.prefix = 'movespy_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + '_'
        self.wd = os.getcwd()
        
        self.moves_dir = movespy_settings.moves_dir
        self.cur = MySQLdb.connect(host = 'localhost', db = movespy_settings.moves_db).cursor(MySQLdb.cursors.SSCursor)

        self.runspec_template = templates.runspec_template
        self.importscript_template = templates.importscript_template

        self.cleanup = True

        assert options['detail'] in ['average','opmode','driveschedule']

        
    def run(self, output_level = 1):
        '''Use this method to run MOVES.

        Returns an Output instance.

        '''

        


        wd = self.wd
        prefix = self.prefix

        importscript_loc = os.path.join(wd, prefix+'importscript.xml')
        runspec_loc = os.path.join(wd, prefix+'runspec.xml')

        tablelocations = [os.path.join(wd, prefix+tname+'.csv') for tname in Moves.tablenames]

        for tname, tloc in zip(Moves.tablenames, tablelocations):
            open(tloc,'w').write(getattr(self,'%s_table'%tname))      


        mcl = [os.path.join(self.moves_dir,'setenv.bat'),
               '&&',
               'java',
               'gov.epa.otaq.moves.master.commandline.MOVESCommandLine']

        open(importscript_loc,'w').write(self.importscript)
        open(runspec_loc,'w').write(self.runspec)
   

        if output_level > 0:
            print 'running MOVES ...'

        for cmd in [mcl + ['-i',importscript_loc],mcl + ['-r',runspec_loc]]:

            try:
                sp = subprocess.Popen(cmd,
                                      cwd = self.moves_dir,
                                      stdout = subprocess.PIPE,
                                      stderr = subprocess.STDOUT,
                                      creationflags=0x08000000)
            except:
                print 'Error when executing:', cmd
                print 'current working directory:', self.moves_dir
                raise
                
                
            
            out = ''
            for line in iter(sp.stdout.readline,""):
                out += line
                if output_level > 1:
                    print line.strip()
                   
            if sp.wait(): #does moves use return codes? or should i be parsing the output for "ERROR"?
                raise subprocess.CalledProcessError(sp.returncode,
                                                    cmd,
                                                    out)
        
                                                
        

        if self.cleanup:
            for tloc in tablelocations:
                os.remove(tloc)
            os.remove(importscript_loc)
            os.remove(runspec_loc)
            self.cur.execute('drop database movesexecution')
            self.cur.execute('drop database movesworker')
            self.cur.execute('drop database %s'%(self.prefix + 'input'))
        

        choices = dict([('source','sourcetypeid'),
                   ('model_year','modelyearid'),
                   ('fuel','fueltypeid'),
                   ('process','processid')])
        
        
        optional_fields_selection = ''

        if not self.options.get('breakdown'):
            pass
        else:
            for field in self.options['breakdown']:
                assert field in choices
                optional_fields_selection += '{} as {},\n'.format(choices[field], field)
            

        db = '{}output'.format(self.prefix)
        
        cur = MySQLdb.connect(host = 'localhost',
                              db = db).cursor(MySQLdb.cursors.SSDictCursor)


        cur.execute('''select  linkid as link,pollutantid as pollutant,
                       {}
                       emissionquant as quantity
                       from {}output.movesoutput'''.format(optional_fields_selection,
                                                           self.prefix))

        fields = zip(*cur.description)[0]


        return Output(cur, db, self.cleanup, fields)




    @property
    def links_table(self):
        result = 'linkID,countyID,zoneID,roadTypeID,linkLength,linkVolume,linkAvgSpeed,linkDescription,linkAvgGrade\n'
        zone_id = str(self.activity['county']) + '0'
        for link_id, link in self.activity['links'].iteritems():
            row = [link_id,
                   self.activity['county'],
                   zone_id,
                   link['road_type'],
                   link['length'],
                   link['volume'],
                   link['speed'],
                   link.get('description',''),
                   link['grade']
                   ]
            result += ','.join([str(x) for x in row]) + '\n'
        return result

    @property
    def source_distr_table(self):
        result = 'linkID,sourceTypeID,sourceTypeHourFraction\n'
        for link_id, link in self.activity['links'].iteritems():
            for source_type_id, fraction in link['source_distr'].iteritems():
                row = [link_id,
                       source_type_id,
                       fraction]
                result += ','.join([str(x) for x in row]) + '\n'
        return result

    @property
    def age_distr_table(self):
        result = 'sourceTypeID,yearID,ageID,ageFraction\n'
        for source_type_id in self.activity['age_distr'].keys():
            for age,fraction in self.activity['age_distr'][source_type_id].iteritems():
                row = [source_type_id,
                       self.activity['year'],
                       age,
                       fraction]
                result += ','.join([str(x) for x in row]) + '\n'
        return result

    @property
    def opmode_distr_table(self):
        activity = self.activity
        options = self.options
        result = 'sourceTypeID,hourDayID,linkID,polProcessID,opModeID,opModeFraction\n'
        if options['detail'] == 'opmode':
            hour_day_id = str(Moves._hourToHourID(activity['hour'])) + str(activity['day_type'])
            for link_id, link in activity['links'].iteritems():
                for source_type_id in link['opmode_distr'].keys(): 
                    for process_id, pollutant_ids in Moves.process_pollutant.items():
                        for pollutant_id in pollutant_ids:
                            pollutant_process_id = pollutant_id * 100 + process_id
                            op_mode_dist = link['opmode_distr'][source_type_id].copy()
                            if pollutant_process_id != 11609 and 501 in op_mode_dist.keys():
                                if 1 not in op_mode_dist.keys():
                                    op_mode_dist[1] = 0
                                op_mode_dist[1] += op_mode_dist.pop(501)
                            for operating_mode_id,fraction in op_mode_dist.iteritems():
                                row = [source_type_id,
                                       hour_day_id,
                                       link_id,
                                       pollutant_process_id,
                                       operating_mode_id,
                                       fraction]
                                result += ','.join([str(x) for x in row]) + '\n'
        return result



    @property
    def drive_schedule_table(self):
        options = self.options
        activity = self.activity
        
        result = 'linkID,secondID,speed,grade\n'

        if options['detail'] == 'driveschedule':
            for link_id, link in activity['links'].iteritems():
                second_id = 0
                for speed, grade in link['driveschedule']:
                    second_id += 1
                    row = map(str, [link_id, second_id, speed, grade])
                    result += ','.join(row) + '\n'

        return result
            
            
            

            
    
        
    




    @property
    def fuel_supply_table(self):
        sql = '''   select countyID, year.fuelYearID AS fuelYearID, monthGroupID,
                        fuelFormulationID, marketShare, marketShareCV
                    from fuelsupply
                    LEFT JOIN year ON fuelsupply.fuelYearID = year.fuelYearID
                    WHERE countyID = %s AND yearID = %s AND monthGroupID = %s'''
        sql = sql%(self.activity['county'],self.activity['year'],self.activity['month'])
        return self._getCSV(sql)
    
    @property
    def fuel_form_table(self):
        sql = '''   select *
                    from fuelformulation
                    WHERE fuelFormulationID in
                    (select fuelFormulationID
                    from fuelsupply
                    LEFT JOIN year ON fuelsupply.fuelYearID = year.fuelYearID
                    WHERE countyID = %s AND yearID = %s AND monthGroupID = %s)'''
        sql = sql%(self.activity['county'],self.activity['year'],self.activity['month'])
        return self._getCSV(sql)
    
    @property
    def meteor_table(self):
        hour_id = Moves._hourToHourID(self.activity['hour'])
        sql = '''   select monthID, zoneID, hourID, temperature, relHumidity
                    from zonemonthhour
                    WHERE monthID = %s AND zoneID = %s0 AND hourID = %s'''
        sql = sql%(self.activity['month'],self.activity['county'],hour_id)
        return self._getCSV(sql)




    def _getCSV(self,query):
        self.cur.execute(query)
        field_names = [f[0] for f in self.cur.description]
        result = ','.join(field_names) + '\n'
        rows = self.cur.fetchall()
        for row in rows:
            result += ','.join([str(x) for x in row]) + '\n'
        return result.replace('None','')

    @property
    def runspec(self):
        root = et.fromstring(self.runspec_template)
        self._setSelections(root)
        self._setBreakdown(root)
        root.find('scaleinputdatabase').set('databasename',self.prefix + 'input')
        root.find('outputdatabase').set('databasename',self.prefix + 'output')
        return et.tostring(root)

    @property
    def importscript(self):
        wd = self.wd
        prefix = self.prefix

        root = et.fromstring(self.importscript_template)
        importer = root.find('importer')
        filters = importer.find('filters')
        self._setSelections(filters)
        importer.find('databaseselection').set('databasename',self.prefix + 'input')

        for tname, tpath in zip(Moves.tablenames, Moves.tablepaths):
            importer.find(tpath).text = os.path.join(wd, prefix+tname+'.csv')
            
        return et.tostring(root)



    def _setSelections(self, root):
        activity = self.activity
        options = self.options
        
        geo_sel = root.find('geographicselections/geographicselection')
        geo_sel.set('key', str(activity['county']))
        
        time_span = root.find('timespan')
        time_span.find('year').set('key', str(activity['year']))
        time_span.find('month').set('id', str(activity['month']))
        time_span.find('day').set('id', str(activity['day_type']))
        time_span.find('beginhour').set('id', str(Moves._hourToHourID(activity['hour'])))
        time_span.find('endhour').set('id', str(Moves._hourToHourID(activity['hour'])))

        if self.options.has_key('pollutants'):
            pol_sel = root.find('pollutantprocessassociations')
            for item in list(pol_sel):
                if int(item.get('pollutantkey')) not in self.options['pollutants']:
                    pol_sel.remove(item)

        return None

    def _setBreakdown(self, root):

        breakdown_sel = root.find('outputemissionsbreakdownselection')

        choices = {'model_year':'modelyear',
         'fuel':'fueltype',
         'process':'emissionprocess',
         'source':'sourceusetype'}


        if not self.options.get('breakdown'):
            return None
            
        for field in self.options['breakdown']:
            assert field in choices

            breakdown_sel.find(choices[field]).set('selected', 'true')

        return None

        

        
        
        
    

def getDefaultAgeDistribution(year):
    '''Use this function to get a MOVES national-level default age distribution.

    Returns a dictionary suitable for inclusion in the
    Moves class initializer activity parameter.

    '''

    root = et.fromstring(templates.mean_age_run_spec)
    root.find('timespan').find('year').set('key', str(year))
    root.find('outputdatabase').set('databasename', 'average_age_dist_output')
    runspec_loc = os.path.abspath('average_age_dist_runspec.xml')
    open(runspec_loc,'w').write(et.tostring(root))
    mcl = [os.path.join(movespy_settings.moves_dir,'setenv.bat'),
               '&&',
               'java',
               'gov.epa.otaq.moves.master.commandline.MOVESCommandLine']

    subprocess.check_call(mcl + ['-r',runspec_loc], cwd = movespy_settings.moves_dir)
    cur = MySQLdb.connect(host = 'localhost', db = movespy_settings.moves_db).cursor()
    sql = '''select sourcetypeid, ageid, population from movesexecution.sourcetypeagepopulation
                where yearid = %s'''%year
    cur.execute(sql)
    result = {}
    for source_type, age, population in cur:
        temp = result.setdefault(source_type, {})
        temp[age] = population
    for source_type in result.keys():
        total = sum(result[source_type].values())
        for age, v in result[source_type].items():
            result[source_type][age] = v * 1.0 / total

    os.remove(runspec_loc)
    cur.execute('drop database movesexecution')
    cur.execute('drop database movesworker')
    cur.execute('drop database average_age_dist_output')

    return result


 
if __name__ == "__main__":
    links = {1: {'grade': -1.2,
                 'length': 0.25,
                 'road_type': 5,
                 'source_distr': {21: 1.0},
                 'speed': 34,
                 'volume': 400}}

    activity =  {'age_distr': {21: {5: 1.0}},
                 'county': 50027,
                 'day_type': 5,
                 'hour': 16,
                 'month': 6,
                 'year': 2015,
                 'links': links}

    options = {'detail': 'average'}

    moves = Moves(activity, options)
    emissions_out = moves.run(2)
    
    
    
        


    

    


    

    

    
