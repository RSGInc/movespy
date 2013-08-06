
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

***************   
Getting Started
***************

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


**************************************
Using :mod:`movespy` to run MOVES
**************************************

Simple Example
==============

We'll start with a simple example. Let's say we would like to estimate emissions for vehicle traffic on a single link. First some details about the link:

  - This link has a volume of 400 vehicles per hour, a length of 0.25 miles, and an average speed of 34 mph. 
  - It's an urban surface street (not a freeway) and it's one-way and has a grade of -1.2 percent in the direction of travel. 
  - The link is in Windsor County, Vermont and we want to do the analysis for 4:00 pm on a weekday in June in 2015. 
  - Just to make things easy, all the vehicles on the link are passenger cars, and they are all five years old.
  
To set up this analysis we first construct a `links` dictionary that holds 
just one key-value pair. The key is the ID for the link, which in this case 
is ``1``. The 
value is another dictionary that has that has strings for keys and our input 
data for values, like so::

    links = {1: {'grade': -1.2,
                 'length': 0.25,
                 'road_type': 5, #5 is the ID for an urban non-freeway
                 'source_distr': {21: 1.0}, #21 is the ID for passenger vehicles
                 'speed': 34,
                 'volume': 400}}
                 
Next we construct an `activity` dictionary, like so::

    activity =  {'age_distr': {21: {5: 1.0}},
                 'county': 50027, #50027 is the ID for Windsor County, Vermont
                 'day_type': 5, #5 is the ID for weekdays
                 'hour': 16,
                 'month': 6,
                 'year': 2015,
                 'links': links} #notice that the links dictionary is included here

So now we have the `activity` dictionary, which contains the `links` dictionary. Between the two dictionaries, we've included all the input data that we listed at the beginning. There's just one more dictionary that we need to make before we can run MOVES, and that's the `options` dictionary::

    options = {'detail': 'average'}
    
This dictionary specifies that we want to use the average speed analysis approach in MOVES (rather than the operating mode distribution approach).

Now we're ready. To run MOVES we first import :mod:`movespy.moves`::

    import movespy.moves
    
Then we initialize an instance of the :class:`Moves` class, passing the `activity` and `options` dictionaries as parameters::

    moves = movespy.moves.Moves(activity, options)

Then we call the :meth:`run` method on the :class:`Moves` instance::

    emissions_out, activity_out = moves.run()
    
This kicks-off the MOVES run. When the run is done, the results are returned and assigned to the `emissions_out` and `activity_out` variables. Now we can inspect the results. Let's say we want to know the total carbon monoxide emissions. We can type::

    # 2 is the ID for carbon monoxide 
    total_CO = sum([row.quantity for row in emissions_out if row.pollutant == 2])


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
    emissions_out, activity_out = moves.run()
    total_CO = sum([row.quantity for row in emissions_out if row.pollutant == 2])
                 

How It Works
============
                 
The core component of :mod:`movespy` is the :class:`Moves` class. Instances of the :class:`Moves`
class are initialized with activity and options parameters which completely 
specify a MOVES run. Calling the :meth:`run` method of a :class:`Moves` instance executes a 
complete MOVES run, including creating all necessary input files, importing them to 
an input database,
executing the run, and cleaning up temporary files and databases. The :meth:`run` method 
returns the results of the run in a Python list for easy inspection and 
manipulation.


.. include:: movesinitializers.rst


********************************************************
Using :mod:`movespy` to calculate VSP and Operating Mode
********************************************************

A Simple Example
================

We'll start with a simple example. Let's say we have a vehicle trajectory
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

Next we import the trajectory module::

    import movespy.trajectory
    
Finally, we run the getVSPOpMode function::

    vsp, opmode = movespy.trajectory.getVSPOpMode(veh, speed, grade, mass, 
        mass_factor, alpha, beta, gamma)

                                              
