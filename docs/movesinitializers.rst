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
    Either ``'average'`` or ``'opmode'``.
        

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
         'opmode_distr':<opmode_distr>}
        
    The ``'opmode_distr'`` key and its value are only required if the value for
    the ``'detail'`` key in the `<options>` dictionary is ``'opmode'``.


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
  
      




