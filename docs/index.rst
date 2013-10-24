
##################
The movespy Manual
##################



   


************
Introduction
************

MOVES is a software package developed by the US EPA for estimating pollution
from cars. MOVES is a valuable resource for analysts because it is based 
upon substantial and rigorous research. Some analysts may even be required 
to use MOVES because it is mandatory for certain analysis linked to federal
transportation funding. 

 
:mod:`movespy` aims to make using MOVES easier by making it easy to
write programs to automate MOVES runs and retrieve the results.

.. note::
    Currently :mod:`movespy` focuses on project-level on-road analysis. In the future
    :mod:`movespy` may also focus on county-level or off-road analysis.


Installing and learning Python
==============================

:mod:`movespy` is implemented as a Python package. To use :mod:`movespy` effectively you should know at least a little about Python. But don't worry: Python is easy to learn. And once you know it there's a lot you can do with it (not just :mod:`movespy`). To download Python go to `python.org`_. To learn Python, try one of the many good `Python tutorials`_ online.

.. _Python tutorials: http://www.google.com/search?q=python+tutorial
.. _Python.org: http://python.org/

Installing MOVES
================

:mod:`movespy` works by interacting with MOVES, so you'll need to install MOVES on your computer. To download MOVES go to the EPA's `MOVES webpage`_.

.. _MOVES webpage: http://www.epa.gov/otaq/models/moves/index.htm

When you install moves, make a note of the folder where you put it. You'll need that to install :mod:`movespy`.

Installing :mod:`movespy`
=========================

Download the installer_ and run it.

.. _installer: https://pypi.python.org/pypi/movespy

Next, open the ``movespy_settings.py`` module in the ``movespy`` folder. You 
should see something like this:

::

    moves_dir="C:\\Users\\Public\\MOVES20120410"
    moves_db ="movesdb20120410"
    
You might need to edit the two text values inside the quotes. The first one 
should be the complete path to your MOVES installation directory (the one 
you noted when you installed MOVES). Remember to use double slashes. The 
second one should be the name of the MOVES database (which is assumed to be 
on the local MySQL server). If you're not what the database name is, it's 
probably the same as the name of the installation folder, with "moves" in 
lower case, and "db" inserted after "moves" and before the numbers. Once 
you've make your edits, make sure to save the file.

Getting Help
============

If you need help with movespy, please email Eric.


********
Examples
********

Using :mod:`movespy` to run MOVES
=================================

Let's say we would like to estimate emissions for vehicle traffic on a single link. First some details about the link:

  - This link has a volume of 400 vehicles per hour, a length of 0.25 miles, and an average speed of 34 mph. 
  - It's an urban surface street (not a freeway) and it's one-way and has a grade of -1.2 percent in the direction of travel. 
  - The link is in Windsor County, Vermont and we want to do the analysis for 4:00 pm on a weekday in June in 2015. 
  - Just to make things easy, all the vehicles on the link are passenger cars, and they are all five years old.
  
To set up this analysis we first construct a `links` :class:`dict` that holds 
just one key-value pair. The key is the ID for the link, which in this case 
is ``1``. The 
value is another :class:`dict` that has that has strings for keys and our input 
data for values, like so::

    links = {1: {'grade': -1.2,
                 'length': 0.25,
                 'road_type': 5, #5 is the ID for an urban non-freeway
                 'source_distr': {21: 1.0}, #21 is the ID for passenger vehicles
                 'speed': 34,
                 'volume': 400}}
                 
Next we construct an `activity` :class:`dict`, like so::

    activity =  {'age_distr': {21: {5: 1.0}},
                 'county': 50027, #50027 is the ID for Windsor County, Vermont
                 'day_type': 5, #5 is the ID for weekdays
                 'hour': 16,
                 'month': 6,
                 'year': 2015,
                 'links': links} #notice that the links dictionary is included here

So now we have the `activity` :class:`dict`, which contains the `links` :class:`dict`. Between the two dictionaries, we've included all the input data that we listed at the beginning. There's just one more dictionary that we need to make before we can run MOVES, and that's the `options` :class:`dict`::

    options = {'detail': 'average'}
    
This :class:`dict` specifies that we want to use the average speed analysis approach in MOVES (rather than the operating mode distribution approach).

Now we're ready. To run MOVES we first import :mod:`movespy.moves`::

    import movespy.moves
    
Then we initialize an instance of the :class:`movespy.moves.Moves` class, passing the `activity` and `options` dictionaries as parameters::

    moves = movespy.moves.Moves(activity, options)

Then we call the :meth:`movespy.moves.Moves.run` method on the :class:`movespy.moves.Moves` instance::

    emissions_out = moves.run()
    
This kicks-off the MOVES run. When the run is done, the results are returned and assigned to the `emissions_out` variable. Now we can inspect the results. Let's say we want to know the total carbon monoxide emissions. We can type::

    # 2 is the ID for carbon monoxide 
    total_CO = sum([row['quantity'] for row in emissions_out if row['pollutant'] == 2])


Putting it all together, our entire script for this analysis would be::

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

    import movespy.moves
    moves = movespy.moves.Moves(activity, options)
    emissions_out = moves.run()
    total_CO = sum([row['quantity'] for row in emissions_out if row['pollutant'] == 2])
                 


Using :mod:`movespy` to calculate VSP and Operating Mode
========================================================

We have a vehicle trajectory
dataset produced by a traffic microsimulation. The data set looks like this:

============== ========== =========== ===============
Time (seconds) Vehicle ID Speed (mph) Grade (percent)
============== ========== =========== ===============
  0                 1            3            1
  1                 1            6            2
  2                 1            1           -3
  3                 1            3            1
  3                 2            8            2
  4                 2            5            1
  5                 2            6            3
  2                 3            3            1
  3                 3            9           -2
  4                 3            1            3
  5                 3            3           -4
  6                 3            9           -2
============== ========== =========== ===============                    

The data set includes
three vehicles and 12 vehicle seconds. Vehicle 1 has four seconds, 
vehicle 2 has three seconds, and vehicle 3 has five seconds. Each of the 
three vehicles starts at a different time: seconds 0, 3, and 2 for vehicles
1, 2 and 3 respectively. For each vehicle second, the speed in miles per hour
and grade in percent is given in the table. We will also assume that 
all three vehicles have a mass of 2.0 tonnes, and that they are all 
passenger vehicles.

We want to use :mod:`movespy` to calculate the VSP and operating mode for 
each vehicle second. Before we can do that, we need find values for 
four parameters of the VSP equation: fixed mass factor, alpha, beta and gamma.
Fortunately, MOVES has default values for these parameters for each of the 
vehicle types. So we look up passenger vehicles in the sourceusetype table 
of the MOVES database, and find that the values of these parameters are 
1.5, 0.16, 0.0020, and 0.00049 respectively. 

Now we're ready to calculate VSP and operating mode. First, we prepare
our inputs::

    veh = [1,1,1,1,2,2,2,3,3,3,3,3]
    speed = [3.,6.,1.,3.,8.,5.,6.,3.,9.,1.,3.,9.]
    grade = [1.,2.,-3.,1.,2.,1.,3.,1.,-2.,3.,-4.,-2.]
    mass, mass_factor, alpha, beta, gamma = 2., 1.5, 0.16, 0.0020, 0.00049    

Next we import the :mod:`movespy.trajectory` module::

    import movespy.trajectory
    
Finally, we run the :func:`moves.trajectory.getVSPOpMode` function::

    vsp, opmode = movespy.trajectory.getVSPOpMode(veh, speed, grade, mass, 
        mass_factor, alpha, beta, gamma)

                                              
Using :mod:`movespy` to Generate Emission Rate Look-up Tables 
=============================================================

To generate a look-up table of emissions rates, you will need to provide an activity argument that is similar
to the activity argument for the :class:`movespy.moves.Moves` initializer, except that it does not include 
the 'links' key/value pair. For example::

    activity =  {'age_distr': {11: {5: 1.0}, 21: {5: 1.0}},
                 'county': 50027,
                 'day_type': 5,
                 'hour': 16,
                 'month': 6,
                 'year': 2015}
                 
This dictionary specifies that we want a look up table for a fleet composed entirely of vehicles that 
are five years old; in Windsor County, Vermont; on weekday; during the 4:00 pm hour; in June; and 
in the year 2015. To generate the look up table we first import the :mod:`movespy.ratetable` module::

    import movespy.ratetable
    
Then we run the :func:`movespy.ratetable.getRateTable` function, with our activity dictionary as the argument. We also limit the table to include only two operating modes and two source types. We also 
provide an empty options dictionary::

    table = movespy.ratetable.getRateTable(activity,
                                           {},    
                                           operating_mode_ids = [0, 1],
                                           source_type_ids = [11, 21])
    
The result is a list of dictionaries. Each dict has keys for pollutant, source, opmode and quantity. The 
quantity values are emissions rates in either grams or kJ per vehicle-hour. 
    
If you want to create a flat file look up table, you could do::
     
    header = ['pollutant', 'source', 'opmode', 'quantity']    
                                 
    import csv
    with open('table.csv', 'wb') as f:
        
        d = csv.DictWriter(f, header)
        
        d.writeheader()
        
        d.writerows(table)
        



**********************************
Moves Class Initializer Parameters
**********************************

Before you can run MOVES you need to construct the `<activity>` and `<options>` 
parameters
for the :class:`Moves` class initializer. Study this section to learn the structure for each.

.. glossary::
  :sorted:

  <volume>
    A real number giving the volume in vehicles per hour.  

  <activity>
    A mapping::

        {'county':<county_id>,
         'year':<year>,
         'month':<month>,
         'hour':<hour>,
         'day_type':<day_type_id>,
         'age_distr':<age_distr>
         'links':<links>}

    This is the root level of the `<activity>` parameter.
         
  <age>
    An integer between 0 and 30. Zero means new, and 30
    means 30 years old.  

        
  <age_distr>
    A mapping::

        {<source_type_id>:<source_type_age_distr>,
         ...,
        <source_type_id>:<source_type_age_distr>}  


  <county_id>
    An integer identifying the county. Find this in the county table of the MOVES database.   


  <day_type_id>
    An integer for the day type. 5 for weekday, and 2 for weekend. 


  <detail>
    One of ``'average'``, ``'opmode'``, or ``'driveschedule'``.
        

  <hour>
    An integer for the hour (0 = midnight).
        

  <length>
    A real number giving the length of the link in miles. This value (in miles) should always 
    be less than <speed> (in mph).

    .. note::
      If the value of `<length>` is greater than the value of `<speed>` the results will
      not be correct. A work-around is to adjust the values of `<length>` and `<volume>`
      so that their product remains constant and `<length>` is less than `<speed>`.

        
  <link>
    A mapping::

        {'road_type':<road_type_id>,
         'length':<length>,
         'volume':<volume>,
         'speed':<speed>,
         'grade':<grade>,
         'source_distr':<source_distr>,
         'opmode_distr':<opmode_distr>,
         'driveschedule':<driveschedule>}
        
    The ``'opmode_distr'`` key and its value are only required if the value for
    the ``'detail'`` key in the `<options>` dictionary is ``'opmode'``.
    The ``'driveschedule'`` key and its value are only required if the value for
    the ``'detail'`` key in the `<options>` dictionary is ``'driveschedule'``.


  <link_id>
    An arbitrary positive integer identifying the link


  <links>
    A mapping::

        {<link_id>:<link>,
         ...,
         <link_id>:<link>}
         
         
  <month>
    An integer for the month (1 = January).
       

  <opmode_distr>
    A mapping::

        {<source_type_id>:<source_type_opmode_distr>,
         ...,
         <source_type_id>:<source_type_opmode_distr>}
       
       
  <opmode_id>
    One of the following integers: 0,1,11,12,13,14,15,16,21,22,23,24,25,27,28,29,30,
    33,35,37,38,39,40,501. 

    .. note::
      Values of `<opmode_id>` must be calculated as by the `getOpMode` function in the
      movespy.trajectory module. Note in particular that when speed == 0.0 the opmode is
      always 501, regardless of the pollutant or process you may be interested in.

       
  <options>
    A mapping::

        {'detail':<detail>,
         'pollutants':<pollutants>,
         'breakdown':<breakdown_selections>}
         
    This is the root level of the `<options>` parameter. The `'pollutants'` key 
    is optional. If it is not included then all pollutants 
    will be calculated. The `'breakdown'` key 
    is optional. If it is not included the output will be disaggregated by link and pollutant
    only.     


  <pollutants>
    A sequence of integers identifying pollutants to be calculated. Find these in the pollutant 
    table in the MOVES database. If the list is empty, no pollutants will be calculated.

    .. note::
      The calculation of many pollutants depends on
      the calculation of other pollutants. To get correct results, all dependencies must
      be included in this sequence. Dependencies are not documented yet (at least not here). 
      To be safe,
      calculate all pollutants by not including the ``'pollutants'`` key in the `<options>`
      dictionary. 


  <proportion>
    A real number between 0 and 1. 


  <road_type>
    An integer identifying the road type. Find this in the table roadtype in the MOVES database.
    Note that :mod:`movespy` currently support only on-road analysis.
       
       
  <source_distr>
    A mapping::

        {<source_type_id>:<proportion>,
         ...,
         <source_type_id>:<proportion>}

    For keys not given the proportion is assumed to be zero. Proportions should sum to one.
       
        
  <source_type_age_distr>
    A mapping::

        {<age>:<proportion>,
         ...,
         <age>:<proportion>}

    For keys not included, the proportion is assumed to be zero. Proportion
    values should sum to one.


  <source_type_id>
    An integer identifying the source type. Find this in the sourceusetype table of the
    MOVES database.


  <source_type_opmode_distr>
    A mapping::

        {<opmode_id>:<proportion>,
         ...,
         <opmode_id>:<proportion>}

    For keys not given the proportion is assumed to be zero. Proportions should sum to one.


  <speed>
    A real number giving the average speed in miles per hour
    
  <breakdown_selections>
    An iterable::
    
        [<breakdown_selection>, ...]
        
    Specifies by which fields the output should be disaggregated.

  <breakdown_selection>
    One of `'model_year'`, `'fuel'`, `'process'`, or `'source'`. 
    
  <driveschedule>
    A sequence of tuples. Each tuple contains two items: Speed in miles per hour (a float), 
    and grade in percent (a float). Represents a vehicle trajectory. Must be sorted by time, and
    observations must be one second apart.    
  
  
      






