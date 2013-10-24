=======
movespy
=======

``movespy`` simplifies interaction with 
MOVES_ and traffic microsimulation for project-level analysis. 

.. _MOVES: http://www.epa.gov/otaq/models/moves/index.htm


Dependencies
------------

``movespy`` depends on:

  - `numpy <http://www.numpy.org/>`_
  - `MySQLdb <http://sourceforge.net/projects/mysql-python/>`_


Installation
------------

Download the installer_ and run it.

.. _installer: https://pypi.python.org/pypi/movespy


Also edit the ``movespy_settings.py`` file:

  - ``moves_dir``: a string that is the path to you MOVES installation directory
  - ``moves_db``: a string that is the name of your MOVES database (assumed to be local)



Usage
-----

The following code 
executes a complete MOVES run and calculates the total CO emissions::

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
        

        
This code calculates VSP and operating mode for a vehicle trajectory
dataset::

    veh = [1,1,1,1,2,2,2,3,3,3,3,3]
    speed = [3.,6.,1.,3.,8.,5.,6.,3.,9.,1.,3.,9.]
    grade = [1.,2.,-3.,1.,2.,1.,3.,1.,-2.,3.,-4.,-2.]
    mass, mass_factor, alpha, beta, gamma = 2., 1.5, 0.16, 0.0020, 0.00049    

    import movespy.trajectory

    vsp, opmode = movespy.trajectory.getVSPOpMode(veh, speed, grade, mass, 
        mass_factor, alpha, beta, gamma)
        
        
        
For detailed instructions and examples see the `user manual`_.

.. _user manual: http://ericstalbot.github.com/movespy/

         


    
