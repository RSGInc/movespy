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

''' Functions for calculating VSP and operating mode from trajectory data.


Users typically use only one function from this module: getVSPOpMode.
The arguments to this function can be viewed as different columns
from a single data table. Each argument is typically a
one-dimensional numpy array, but may also be a single value that
is then broadcast. The function returns two values: an array of vsp values,
and an array of operating mode values.

An example with 3 separate vehicles and 12 vehicle-seconds:


>>> veh = [1,1,1,1,2,2,2,3,3,3,3,3]
>>> speed = [3.,6.,1.,3.,8.,5.,6.,3.,9.,1.,3.,9.]
>>> grade = [1.,2.,-3.,1.,2.,1.,3.,1.,-2.,3.,-4.,-2.]
>>> mass, mass_factor, alpha, beta, gamma = 2., 1.5, 0.16, 0.0020, 0.00049
>>> vsp, opmode = getVSPOpMode(veh, speed, grade, mass, mass_factor, alpha, beta, gamma)
>>> opmode
array([12, 13,  0, 12, 12,  0, 12, 12, 16,  0, 12, 16])
>>> vsp[:5].round(2)
array([ 0.15,  5.8 , -1.46,  1.92,  0.41])
'''



from __future__ import division
import numpy

MPH2MPS = 0.44704
MPS2MPH = 1. / MPH2MPS


def _getVSP(speed_mps, accel_mpsps, mass_tonnes, mass_factor, alpha, beta, gamma):
    '''Calculates VSP

    Parameters:

      - `speed_mps`: the current speed of the vehicle (meters per second)
      - `accel_mpsps`: the current acceleration including acceleration from gravity (mpsps)
      - `grade_percent`: the roadway grade (percent)
      - `mass_tonnes`: mass of the vehicle (metric tons) 
      - `mass_factor`: the fixed mass factor 
      - `alpha, beta, gamma`: parameters to the VSP equation

    All parameters should be usable as numpy arrays. Numpy broadcasting
    may be used.

    The mass_factor values and VSP equation parameters are in the
    sourceusetype table in the MOVES database.

    Returns:

      - VSP (kW / tonne ?)


    Source:

    MOVES20120410\gov\epa\otaq\moves\master\implementation\ghg\
    LinkOperatingModeDistributionGenerator.java

    '''
            
    vsp =   (((alpha * speed_mps) +
             (beta * speed_mps ** 2) +
             (gamma * speed_mps ** 3) +
             (mass_tonnes * speed_mps * accel_mpsps)) /
             mass_factor)
    return vsp
    




@numpy.vectorize
def _getOpMode(speed_mph,accel_mphps_t0,accel_mphps_t1,accel_mphps_t2,vsp):
    '''Calculates the operating mode

    Paramaters:

      - `speed`: the current speed of the vehicle in miles per hour
      - `accel_t0`: the current acceleration including acceleration
                    from gravity (miles per hour per second)
      - `accel_t1`: the acceleration one second ago including acceleration
                    from gravity (mphps)
      - `accel_t2`: the acceleration two seconds ago including acceleration
                    from gravity (mphps)
      - `vsp`: the current vehicle specific power (kW/tonne?)

    All parameters should be usable as numpy arrays. Numpy broadcasting
    may be used.

    Returns:

      - the operating mode (an integer)

    Source:

    MOVES20120410\gov\epa\otaq\moves\master\implementation\ghg\LinkOperatingModeDistributionGenerator.java
    lines 695 - 726, in `calculateOpModeFractionsCore`

    '''

    #todo: make this faster; don't use vectorize

    if speed_mph < 1e-9:
        return 501

    if speed_mph < 1.0:
        return 1

    if accel_mphps_t0 <= -2.0:
        return 0

        

    if all([accel_mphps_t0 < -1.,
            accel_mphps_t1 < -1.,
            accel_mphps_t2 < -1.]):
        return 0

    speed_bin = min(speed_mph // 25, 2)
    vsp_bin = max(-1,min(vsp // 3, 10))


    opmode_lookup = {0:dict(zip(range(-1,11),[11,12,13,14,15,16,16,16,16,16,16,16])),
                    1:dict(zip(range(-1,11),[21,22,23,24,25,27,27,28,28,29,29,30])),
                    2:dict(zip(range(-1,11),[33,33,33,35,35,37,37,38,38,39,39,40]))}


    return opmode_lookup[speed_bin][vsp_bin]



def _getAccel(veh, speed_mps, grade_percent, simple = False):
    ''' Calculate accelerations

    Parameters:

      - `veh`: a sequence of vehicle IDs
      - `speed_mps`: current speed (meters per second)
      - `current`: current grade (percent)

    All three parameters must be of equal length and
    sorted to correspond to each other.
    
    The parameters must be sorted so that all rows from
    a vehicle are grouped together, and sorted within
    each group by time.
    
    Rows must correspond to observations taken one second apart.

    All parameters should be usable as one-dimensional numpy arrays.
    Numpy broadcasting may be used.

    Returns:

      - A tuple of three acceleration arrays for the current acceleration,
        the acceleration one second ago, and the acceleration two seconds
        ago, all in meters per second per second.

    For cases where the lagged speed or grade is not available, the acceleration
    is set to zero following the calculations in MOVES.

    If `simple` is True then a simplified calculation will be used to
    determine the effect of grade on acceleration. This eliminates
    two trigonometric functions and results in relative errors of less
    than two percent for grades between -20 and 20. 
    
    
    '''


    def lag1(seconds, x):
        return numpy.append(numpy.array([numpy.nan]*seconds), x[:-seconds])

    def lag2(seconds, veh, x):
        lagged_x = lag1(seconds, x)
        lagged_veh = lag1(seconds, veh)
        lagged_x[~ (veh == lagged_veh)] = numpy.nan
        return lagged_x

    speeds = [speed_mps[:]]+[lag2(seconds, veh, speed_mps) for seconds in [1,2,3]]

    grades = [grade_percent[:]]+[lag2(seconds, veh, grade_percent) for seconds in [1,2]]


    if simple:
        def get_grade_effect(grade):
            return grade / 100.
    else:
        def get_grade_effect(grade):
            return numpy.sin(numpy.arctan(grade/100.0))


    def get_accel(speed_a, speed_b, grade):
        accel = (speed_a - speed_b) + 9.81*get_grade_effect(grade)
        accel[numpy.isnan(speed_a) | numpy.isnan(speed_b) | numpy.isnan(grade)] = 0.0
        return accel

    accels_mpsps = [get_accel(sa, sb, g) for sa, sb, g in zip(speeds[:-1], speeds[1:], grades)]

    return accels_mpsps



def getVSPOpMode(veh, speed_mph, grade_percent, mass_tonnes, mass_factor, alpha, beta, gamma, simple = False):
    ''' Calculates VSP and OpMode
    Parameters:

      - `veh`: a sequence of vehicle IDs
      - `speed_mph`: current speed (miles per hour)
      - `grade_percent`: current grade (percent)
      - `mass_tonnes`: mass of the vehicle (metric tons) 
      - `mass_factor`: the fixed mass factor 
      - `alpha, beta, gamma`: parameters to the VSP equation
      - `simple`: Boolean indicating whether to use simplified grade calculation

    All parameters must be broadcastable to one-dimensional arrays
    with equal length and
    sorted to correspond to each other.
    
    The parameters must be sorted so that all rows from
    a vehicle are grouped together, and sorted within
    each group by time.
    
    Rows must correspond to observations taken one second apart.

    The mass_factor values and VSP equation parameters are in the
    sourceusetype table in the MOVES database.

    If `simple` is True then a simplified calculation will be used to
    determine the effect of grade on acceleration. This eliminates
    two trigonometric functions and results in relative errors of less
    than two percent for grades between -20 and 20. 
    
    '''

    veh = numpy.array(veh)
    speed_mph = numpy.array(speed_mph)
    grade_percent = numpy.array(grade_percent)
    mass_tonnes = numpy.array(mass_tonnes)
    mass_factor = numpy.array(mass_factor)
    alpha = numpy.array(alpha)
    beta = numpy.array(beta)
    gamma = numpy.array(gamma)

    speed_mps = speed_mph * MPH2MPS

    accel_mpsps_t0, accel_mpsps_t1, accel_mpsps_t2 = _getAccel(veh, speed_mps, grade_percent, simple)

    vsp = _getVSP(speed_mps, accel_mpsps_t0, mass_tonnes, mass_factor, alpha, beta, gamma)

    accel_mphps_t0 = accel_mpsps_t0 * MPS2MPH
    accel_mphps_t1 = accel_mpsps_t1 * MPS2MPH
    accel_mphps_t2 = accel_mpsps_t2 * MPS2MPH

    opmode = _getOpMode(speed_mph, accel_mphps_t0, accel_mphps_t1, accel_mphps_t2, vsp)

    return vsp, opmode




if __name__ == '__main__':
    import doctest
    doctest.testmod()
    #doctest.testfile("trajectory_tests.rst")



    



    

    

