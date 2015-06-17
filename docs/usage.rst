===========
Usage Guide
===========

The :abbr:`AOIC (ANOPP2 OpenMDAO Interface Code)` contains two classes: `Anopp2Component` and `Anopp2Optimize`.  
The `Anopp2Component` class contains the essence of all interactions with ANOPP2. 
Details of the `Anopp2Component` class used in this specific example are provided herein.
Users desiring to use ANOPP2 for optimization through OpenMDAO are required to develop similar codes with appropriate ANOPP2 function calls and other necessary associated files (see ANOPP2 Manuals for more information). 
This example code is tested through a test code, `test_anopp2.py`.

In this case, the noise generated during the takeoff of a `Tube and Wing` aircraft is modeled through ANOPP2 and the noise along a sideline parallel to the takeoff direction on the ground is predicted.  
The location along the sideline at which the noise (measured through the acoustic metric :abbr:`EPNL (Effective Perceived Noise Level)`) reaches its maximum is determined through OpenMDAO. 
The details of this :abbr:`AOIC (ANOPP2 OpenMDAO Interface Code)` are explained here.

---------------
Anopp2Component
---------------

Initialization
==============

**Step 1. Initialize ANOPP2 API**: The ANOPP2 Command Executive API [LOPES2014A_] is initialized first through the following command: ``ANOPP2.a2py_exec_init_api ()``.

**Step 2. Initialize local variables**: Initialize the Atmosphere and Flight Path tags.

**Step 3. Create an Observer**: An observer [LOPES2014B_] is defined as a point cloud (a collection of several points in space, also referred to as `nodes`) along the sideline defined by its x (along the direction of the flight on the ground), y (perpendicular to the direction of flight on the ground), and z (perpendicular to the ground) axes. The observer is defined in a configuration file, `observer.config` placed in the current working folder.  This configuration file is provided below:

.. literalinclude:: observer.config
    :linenos:

The observer is created through the following ANOPP2 command:

::

    intSuccess =             \
      ANOPP2.a2py_obs_create \
       (pointer(self.intObserverTag), create_string_buffer (b"observer.config"))

Execution
=========

The `Anopp2.py` performs the following steps as part of its execution. 
Each of these steps are executed for each iteration to determine the noise (EPNL) corresponding to that observer location.

**Step 4. Create a New Observer Node**: A new node is introduced into the observer at a location whose ``x`` coordinate is provided by the optimizer and the ``y`` and ``z`` coordinates are those of the previous node. 
So, the number of nodes in the observer is first obtained through the following function call:

::

  intSuccess = ANOPP2.a2py_obs_number_of_nodes (self.intObserverTag, self.nNodes)

The position of the last node in the observer is obtained through the following function call:

::

    intSuccess =               \
      ANOPP2.a2py_obs_position \
        (self.intObserverTag, self.nNodes, 0.0, a2_global, self.fltPosition)

where, ``self.fltPosition`` is an array containing the ``x``, ``y``, and ``z`` coordinates of the position of the last node in the observer.

The first value of the Position array (x coordinate) is replaced with the value provided by the optimizer: ``self.fltPosition[0] = self.x``. 
A new node is added in the observer point cloud at the location corresponding to the values of the ``fltPosition`` array through the following function call:

::

  intSuccess = ANOPP2.a2py_obs_new_node (self.intObserverTag, self.fltPosition)
  
**Step 5. Create an AnoppComplete Functional Module**: In this case, ANOPP2's AnoppComplete Functional Module [LOPES2014C] is  used to predict the EPNL. 
This functional module is invoked in ANOPP2 through the following routine call:  

::

    intSuccess =                                                                         \
      ANOPP2.a2py_exec_create_functional_module                                          \
       (pointer(self.intAnoppCompleteTag),                                               \
        create_string_buffer (b"AnoppComplete.config"), self.nInputs, self.intInputTags, \
        pointer(self.intObserverTag), pointer(self.nResults), pointer(self.intResultTags))

The settings and details required for using this Functional Module are provided in the Configuration file, `AnoppComplete.config`. 
The contents of this file is provided here.

.. literalinclude:: AnoppComplete.config
    :linenos:

The name of an ANOPP input deck template, `Takeoff-Complete.inp`, is specified in the Configuration file, `AnoppComplete.config`. 
This input deck template is required for executing ANOPP as part of this functional module. 
This input deck template contains all the specifications of the aircraft frame and engine, as well as the ANOPP functional modules to be executed to obtain noise.  
The template contains the marker, ``$$$ A2_GROUND_OBSERVER`` that enables the AnoppComplete functional module to insert the current observer in the ANOPP input deck.  
The ground effects are turned off through the statement, ``PARAM GROUND = .FALSE. $`` in the template.  
The input deck template instructs ANOPP to execute and obtain noise from jet (JET), treated inlet (INLETT), treated aft fan (AFTFNT), GE Core (GECOR), gear (GEAR), flap (FLAP), and trailing edge (TRAL).  
It also instructs ANOPP to add the noise from all the sources and provide that as the Total noise, add JET, INLETT, AFTFNT, and GECOR as Engine noise, and add GEAR, FLAP, and TRAL as Airframe noise. The AnoppComplete functional module inserts the `Total`, `Engine`, and `Airframe` noise into the ANOPP2 Observer as the first, second, and the third result, respectively.

**Step 6. Creating an ANOPP2 Mission**: An ANOPP2 Mission is created through the following routine call:

::

    intSuccess =                                                                        \
      ANOPP2.a2py_exec_create_mission                                                   \
       (pointer(self.intMissionTag), create_string_buffer (b""), self.intAtmosphereTag, \
        self.intFlightPathTag, self.nSourceTimes,                                       \
        self.nMaximumSingleTimeFunctionalModules, self.nTimeSeriesFunctionalModules,    \
        self.fltSourceTimes, self.intSingleTimeFunctionalModuleTags,                    \
        self.intTimeSeriesFunctionalModulesTags)

This instructs ANOPP2 what functional module is to be executed and also provides the tags of all the inputs required for executing this mission. 

**Step 7. Execute an ANOPP2 Mission**: The ANOPP2 mission is executed through the following routine call:

::

    intSuccess = ANOPP2.a2py_exec_execute_mission (self.intMissionTag)

Upon execution, the acoustic data corresponding to the observer is calculated and placed in the Observer in terms of Octave Band :abbr:`SPL (Sound Pressure Level)`. 

**Step 8. Obtaining the Noise Data**: The acoustic data EPNL is calculated from the SPL through the following routine call:

::

    intSuccess =                                                                  \
      ANOPP2.a2py_obs_calc_metric                                                 \
       (self.intObserverTag, self.nResults.value, self.intResultTags, a2_aa_epnl, \
        a2_obs_complete)

The EPNL value corresponding to the last node added through Step 4 is obtained through the Observer API routine call as shown below.  
Because the intent is to find the location corresponding to maximum total noise, the EPNL corresponding to the first result, that is, the `Total` noise is obtained.

::

    intSuccess =                                                                      \
      ANOPP2.a2py_obs_get_epnl                                                        \
        (self.intObserverTag, self.intResultTags[0], self.nNodes.value, self.fltEpnl, \
         self.fltD, self.fltTimeRange)

The EPNL, the duration, and the time range are obtained for the observer position.

**Step 9. Getting the Optimizing Variable Value**: The goal of this AOIC is to find the position of maximum noise. 
This is equivalent to minimizing the reciprocal of the EPNdB value predicted. 
To avoid very small fractions, the reciprocal was multiplied with 1000. 
In this AOIC, the variable ``Epndb_inverse`` was minimized.

::

  self.Epndb_inverse = 1000.0/float(self.fltEpnl.value)

The EPNL values were exported to a Tecplot-friendly file, `Epnl.out.dat` through the following routine:

::

    intSuccess =                                                                 \
      ANOPP2.a2py_obs_export                                                     \
        (self.intObserverTag, self.intResultTags[0],                             \
         create_string_buffer(bytes(self.strOutputFile)), a2_aa_epnl, a2_global, \
         a2_formatted, a2_tecplot)

Finally, the result in the Observer is deleted because it is no longer needed.

::

    intSuccess =                     \
      ANOPP2.a2py_obs_delete_results \
        (self.intObserverTag, self.nResults.value, self.intResultTags, 0)

--------------
Anopp2Optimize
--------------

The Anopp2Optimize code should contain a function, `configure` that specifies the optimzer, the component, the objective variable, the design variable, as well as the optimizing parameters.

The driver, `CONMINdriver` is used in this optimization through the following statement:

::

    self.add('driver', CONMINdriver())

The component, `Anopp2Component` is introduced in the `configure` function as `anopp2`.  

::

    self.driver.workflow.add('anopp2')

The objective variable, `Epndb_inverse`  and the design variable, `x` defined in `Anopp2Component` are accessed in this function through `anopp2.Epndb_inverse` and `anopp2.x`. 

::

    self.driver.add_objective('anopp2.Epndb_inverse')
    self.driver.add_parameter('anopp2.x', low=2400., high=3500.0)

The CONMIN specific settings used in this optimization are as follows:

::

    self.driver.itmax = 30
    self.driver.fdch = 0.001
    self.driver.fdchm = 0.0001
    self.driver.ctlmin = 0.01
    self.driver.delfun = 0.01
    self.driver.conmin_diff = True
    self.iIteration = 0

------------
test_aoic.py
------------

The Python test code that runs the optimizer and iterates to find the location along the sideline that has maximum noise is `test_aoic.py`. 
This test code is executed after launching the OpenMDAO framework through the following command:

::

  python test_Anopp2_optimize.py

The Python code executes ANOPP2 iteratively with various values of the design variable (the observer x coordinate) and obtains the value of the objective variable to be minimzed. 
The optimizer stops on finding a location at which the noise is maximum.

-------
Results
-------

The EPNdB values at various locations along the sideline parallel to the flight path were independently obtained at intervals of 100m.  
An analysis of the EPNdB distribution along the sideline indicates that there exists a local maximum around the location where the aircraft takes off, at approximately 2500m from the aircraft starting location.  
The EPNdB values corresponding to observer positions along the sideline from 2400m to 2700m were independently obtained at intervals of 6m. 
The EPNdB values at various observer locations along the sideline were also obtained through this `AOIC`. 
These results are plotted as `EPNdB along a sideline`_.

.. _`EPNdB along a sideline`:

.. figure:: Optimized.png
   :align: center
   
   Variation of EPNL along a sideline showing the sequence of steps followed by OpenMDAO in arriving at the location corresponding to maximum EPNdB

The observer locations and the corresponding EPNdB values as obtained through `AOIC` are also plotted in `EPNdB along a sideline`_ as a sequence of steps (red lines and dots). 
The location as found by OpenMDAO that corresponds to maximum EPNdB value along the sideline is at **2538.5m**.


.. [LOPES2014A] Lopes, L. V. and Burley, C. L., *ANOPP2 Command Executive API Reference Manual*, National Aeronautics and Space Administration, version 1.0.0, July 2014.

.. [LOPES2014B] Lopes, L. V. and Burley, C. L., *ANOPP2 Observer API Reference Manual*, National Aeronautics and Space Administration, version 1.0.0, July 2014.

.. [LOPES2014C] Lopes, L. V. and Burley, C. L., *ANOPP2 Functional Module Manual*, National Aeronautics and Space Administration, version 1.0.0, July 2014.
