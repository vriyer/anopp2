#!/usr/bin/python
#
# The ANOPP2_api Module for ANOPP2.
#
# Import Modules:
import math

from ctypes import *
ANOPP2 = CDLL('../libANOPP2.so', RTLD_GLOBAL)

#
# Define Basic Constants used by the API.
#
false = c_bool(0)
true = c_bool(1)

#!/usr/bin/python
# -----------------------------------------------------------------------------------------
# This file is the interface file for the C++ subroutines in the ANOPP2
# Application Programming Interface (API).  This file should be copied to your local
# directory and an "include 'ANOPP2.api.h'" must be present in your
# program.  See anyone of the demonstrators provided with this API in the Demos
# directory.  For explanation of how to call and the theory behind each function, 
# please see the API manual provided with ANOPP2.
# -----------------------------------------------------------------------------------------
# @file ANOPP2.api.h
# @author The ANOPP2 Development Team
# @version 1.0.0
# -----------------------------------------------------------------------------------------



# =========================================================================================
# First part of this section of the contains interfaces into the available ANOPP2 API 
# functions.
# =========================================================================================



# -----------------------------------------------------------------------------------------
# This function initializes the ANOPP2 API by setting internal variables and function
# parameters that must exist before any other call to the API can be made.
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------
# This routine performs all the unit tests within the Command Executive.  An integer
# is returned that equals the number of fails in the system.  Zero indicates no
# failures.
# -----------------------------------------------------------------------------------------
# @result
#       A success integer that is equal to the number of failed asserts.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_exec_unit_test.restype = int



# -----------------------------------------------------------------------------------------
# This function call creates a Functional Module provided a set of input tags. The order
# and what tags are in the list is dependent on the Functional Module being created.  
# see Documentation for more information on what specific tags are included.
# -----------------------------------------------------------------------------------------
# @param intTag
#        This is the tag that will be returned to the user after the object has
#        been created.
# @param strConfigurationFile
#        This is a file that contains the inputs required for the object to be
#        created. This is typically a namelist file.
# @param nInputs
#        This is the number of inputs provided to this routine
# @param intInputTags
#        These are the tags of the inputs provided to the Functional Module
# @param intObserverTag
#        This is the tag associated with the observer data structure where the
#        results of the functional module will be cast.
# @param nResults
#        These are the number of results provided by executing the Functional Module.
# @param intResultTags
#        These are tags associated to the results provided by the Functional Module
# @result
#        An integer that is returned 0 when everything occurred correctly.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_exec_create_functional_module.restype = int
ANOPP2.a2py_exec_create_functional_module.argtypes =                        \
  [POINTER(c_int), c_char_p, c_int, POINTER(c_int), POINTER(c_int), POINTER \
    (c_int), POINTER(POINTER(c_int))]



# -----------------------------------------------------------------------------------------
# This function takes in an atmosphere tag, flight path tag, number of time steps in the
# Functional Module, the maximum number of time steps per Functional Module, an array of 
# waypoint times the size of which is the number of time steps, and a 2-dimensional
# array of predition tags.  The size of the first dimension of Functional Module tags 
# is equal to the number of time steps, and the size of the second dimension is equal
# to the maximum number of Functional Modules.  This function will create a mission in
# the ANOPP2 API. The mission class includes a list of Functional Module per time step.
# -----------------------------------------------------------------------------------------
# @param intMissionTag
#        This function returns a mission which can be accessed by this tag value.
# @param strConfigurationFile
#        This is a file that the mission uses for settings.
# @param intAtmisphereTag
#        A tag which is associated to the atmosphere that will be used to generate the
#        aircraft specific atmospheric properties.
# @param intFlightPathTag
#        A tag which is associated to the aircraft's flight path for this mission.
# @param nTimeSteps
#        The number of time steps for this Functional Module.
# @param nMaximumSingleTimeFunctionalModules
#        The maximum number of Functional Module per time step.
# @param nTimeSeriesFunctionalModules
#        The number of time series functional modules being executed.
# @param fltWayPointTimes
#        An array of WayPoint times.  The size of this array is equal to the number of
#        time steps.  These times must be increasing.  
# @param intSingleTimeFunctionalModuleTags
#        A two dimensional array, sized by the number of time steps and the number of
#        maximum Functional Modules, that contains tags associated to the time.  The 
#        Functional Module tags are used to access Functional Modules that occur at
#        those times.
# @param intTimeSeriesFunctionalModuleTags
#        This is an array of tags that represent the time series events that will be
#        performed.
# @result
#        An integer that is 0 if everything has occurred as expected.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_exec_create_mission.restype = int
ANOPP2.a2py_exec_create_mission.argtypes =                              \
  [POINTER(c_int), c_char_p, c_int, c_int, c_int, c_int, c_int, POINTER \
    (c_float), POINTER(c_int), POINTER(c_int)]



# -----------------------------------------------------------------------------------------
# This function performs all operations that have been previously set up in the mission.
# This includes executing all Functional Modules in the order the user has dicteted.
# -----------------------------------------------------------------------------------------
# @param intMissionTag
#        This tag is associated to the mission that is to be executed.
# @result
#        An integer that is 0 if everything has occurred as expected.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_exec_execute_mission.restype = int
ANOPP2.a2py_exec_execute_mission.argtypes = [c_int]



#!/usr/bin/python
# -----------------------------------------------------------------------------------------
#  This file is the interface file for the Fortran subroutines in the Atmosphere
#  Application Programming Interface (API).  This file should be copied to your local
#  directory and an "include 'ANOPP2.api.f90'" must be present in your
#  program.  See AcousticAnalysisAPIDemonstrator.cplusplus.cpp for an example including
#  using all present subroutines.
# -----------------------------------------------------------------------------------------
#   @file ANOPP2.api.h
#   @author The ANOPP2 Development Team
#   @version 1.0.0
# -----------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------
#  This subroutine initializes the ANOPP2.API and should be included at the very
#  start of your program (before any other subroutines are called).
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------
#  This routine executes the unit tests in the ANOPP2.API.  The unit 
#  tests execute all the tests implemented in the ANOPP2.API.
# -----------------------------------------------------------------------------------------
# @result
#         The total number of failed asserts encountered during unit testing.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_atm_unit_test.restype = int



# -----------------------------------------------------------------------------------------
#  This routine creates an atmosphere data structure in the ANOPP2 API.  A tag is 
#  returned which is used by the calling program to access that data structure.  The
#  input into this routine is the name of a settings file.  The settings file must 
#  contain one of the known types of atmopsheres.  See Documentation for more information
#  on the format of the settings file.
# -----------------------------------------------------------------------------------------
#  @param dmy_intTag
#         This is an integer that is returned by this function.  It is used to access
#         the data structure that is created.
#  @param dmy_strConfigurationFile
#         This is the name of the input file that contains the configuration for the new
#         atmosphere. See Documentation for more information.
#  @result
#         An integer that is returned 0 when everything occurred correctly.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_atm_create.restype = int
ANOPP2.a2py_atm_create.argtypes = [POINTER(c_int), c_char_p]



# -----------------------------------------------------------------------------------------
#  This function takes in a tag representing an atmosphere and returns true if it exists
#  in the API and false if it does not.
# -----------------------------------------------------------------------------------------
#  @param intTag
#         This is the tag associated to the atmosphere that is being searched for.
#  @result
#          A bool that returns true if the observer exists and false if it does not.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_atm_exists.restype = bool
ANOPP2.a2py_atm_exists.argtypes = [c_int]



# -----------------------------------------------------------------------------------------
#  This routine saves the atmosphere data structure in a preopened file by exporting
#  all internal data.  The file format is specific to the data structure being written
#  out.
# -----------------------------------------------------------------------------------------
#  @param dmy_intTag
#         This is an integer representation of the atmosphere to be saved
#  @param dmy_strRestartFile
#         This is the name of the file being created.
#  @result
#         An integer representing success of this function
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_atm_save.restype = int
ANOPP2.a2py_atm_save.argtypes = [c_int, c_char_p]



# -----------------------------------------------------------------------------------------
# This routine creates an atmosphere data structure in the ANOPP2 API.  A tag is
# returned which is used by the calling program to access that data structure.  The
# input into this routine is the name of a settings file.  The settings file must
# contain one of the known types of atmosphere.  See Documentation for more information
# on the format of the settings file.
# -----------------------------------------------------------------------------------------
#  @param dmy_intTag
#         This is the tag that will be returned to the user after the object has
#         been created.
#  @param dmy_enumAtmosphere
#         This is the enumeration of the atmosphere desired in the Catalog.
#  @param dmy_strRestartFile
#         This is the file name of the user supplied restart.  If the enumeration
#         provided does not exist, it will be loaded from this restart file.
#  @result
#         An integer that is returned 0 when everything occurred correctly.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_atm_load.restype = int
ANOPP2.a2py_atm_load.argtypes = [POINTER(c_int), c_int, c_char_p]



# -----------------------------------------------------------------------------------------
#  This routine returns the atmospheric properties at a given location and time. The
#  atmosphere tag is passed to this routine along with the location and time, and the
#  properties are returned.
# -----------------------------------------------------------------------------------------
#  @param intTag
#         This is the tag that is associated with the atmosphere in the library.
#  @param fltPosition
#         This is the XYZ location where the properties are desired.
#  @param fltTime
#         This is the time where the properties are desired.
#  @param fltSpeedOfSound
#         This is the speed of sound at the position and time.
#  @param fltAmbientTemperature
#         This is the ambient temperature at the position and time.
#  @param fltAmbientPressure
#         This is the ambient pressure at the position and time.
#  @param fltRelativeHumidity
#         This is the percent relative humidity at the position and time.
#  @param fltAmbientDensity
#         This is the ambient density at the position and time.
#  @result
#         An integer representing success of this operation.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_atm_get_properties.restype = int
ANOPP2.a2py_atm_get_properties.argtypes =                                  \
   [c_int, POINTER                                                             \
     (c_float), c_float, POINTER(c_float), POINTER(c_float), POINTER(c_float), \
    POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
#  This function accesses the ANOPP2.API and tells it to export the atmospheric
#  properties.  The function takes in an atmosphere tag and commands the ANOPP2.API 
#  to write out atmospheric data to a file.  The file can be of a specified format.
# -----------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         The tag that connects the application code to the ANOPP2 API.
#  @param strFileName
#         This is the name of the file to which the Export routine writes.
#  @param enumFormat
#         This is the format of the file: options may include formatted or binary.
#  @param enumProgram
#         This is the program that will eventually read the file.  This may include
#         Tecplot or NetCDF.
#  @result
#         An integer that is 0 if everything has occurred as expected.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_atm_export.restype = int
ANOPP2.a2py_atm_export.argtypes = [c_int, c_char_p, c_int, c_int]



#!/usr/bin/python
# =========================================================================================
#  Next part of this section of the interface file contains hardcoded enumerators used by
#  the user's program to communicate parameters and settings to the API.
# =========================================================================================



# -----------------------------------------------------------------------------------------
#  These enumerators are to communicate to the API, certain default objects that can be
#  loaded via the catalog.  This is optional.  A user may also specify an input
#  configuration file if they wish with more detail on the object to be constructed.
#  See User's Manual for more information.
# -----------------------------------------------------------------------------------------

# This enumerator is for an undefined atmosphere (not in the catalog)
a2_atm_undefined = 1

# conditions.
a2_atm_sea_level = 2

# the catalog.
a2_atm_standard_day = 3



# -----------------------------------------------------------------------------------------
#  These are the different types of atmospheres available in the ANOPP2.API.  These
#  include a uniform atmosphere and an altitude profile atmosphere.
# -----------------------------------------------------------------------------------------

# This enumerator is for the uniform atmosphere.
a2_atm_uniform = 1

# This enumerator is for the altitude profile.
a2_atm_altitude_profile = 2



#!/usr/bin/python
# 
# -----------------------------------------------------------------------------------------
#  This is the Flight Path API interface file.  It contains definitions for all the
#  functions available in the Flight Path API.  This includes initializations, creation,
#  insertion, exporting, etc.  See API manual for more information.
# ------------------------------------------------------------------------------------------
#  @file ANOPP2.api.f90
#  @author The ANOPP2 Development Team
#  @version 1.0.0
# -----------------------------------------------------------------------------------------
# 



# 
# =========================================================================================
#  First part of this section of the contains interfaces into the available ANOPP2 API 
#  functions.
# =========================================================================================
# 





# -----------------------------------------------------------------------------------------
#  This function initializes the ANOPP2 API by setting internal variables and function
#  parameters that must exist before any other call to the API can be made.
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------
#  This routine executes the unit tests in the Acoustic Analysis module.  The unit 
#  tests execute all the tests implemented in the Acoustic Analysis API.
# -----------------------------------------------------------------------------------------
#  @result
#         An integer that is the total number of failed asserts encountered during
#         unit testing.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_fp_unit_test.restype = int



# -----------------------------------------------------------------------------------------
#  This routine creates an flight path data structure in the ANOPP2 API.  A tag is 
#  returned which is used by the calling program to access that data structure.  The
#  input into this routine is the name of a settings file.  The settings file must 
#  contain one of the known types of flight paths.  See Documentation for more 
#  information on the format of the settings file.
# -----------------------------------------------------------------------------------------
#  @param intTag
#         This is an integer that is returned by this function.  It is used to access
#         the data structure that is created.
#  @param strSettingsFile
#         This is the name of the input file that contains the settings for the new
#         flight path. See Documentation for more information.
#  @param intAtmosphereTag
#         This is the tag associated to the atmosphere that the aircraft is flying
#         through.
#  @result
#         An integer that is returned 0 when everything occurred correctly.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_fp_create.restype = int
ANOPP2.a2py_fp_create.argtypes = [POINTER(c_int), c_char_p, c_int]



# -----------------------------------------------------------------------------------------
#  This function takes in a tag representing an flight path and returns true if it exists
#  in the API and false if it does not.
# -----------------------------------------------------------------------------------------
#  @param intTag
#         This is the tag associated to the flight path that is being searched for.
#  @result
#        A bool that returns true if the observer exists and false if it does not.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_fp_exists.restype = bool
ANOPP2.a2py_fp_exists.argtypes = [c_int]



# -----------------------------------------------------------------------------------------
#  This routine saves the flight path data structure in a preopened file by exporting
#  all internal data.  The file format is specific to the data structure being written
#  out.
# -----------------------------------------------------------------------------------------
#  @param intTag
#         This is an integer representation of the flight path to be saved
#  @param strRestartFile
#         This is the name of the file being created.
#  @result
#         An integer representing success of this function
# -----------------------------------------------------------------------------------------
# 
ANOPP2.a2py_fp_save.restype = int
ANOPP2.a2py_fp_save.argtypes = [c_int, c_char_p]



# -----------------------------------------------------------------------------------------
#  This routine creates a flight path data structure in the ANOPP2 API.  A tag is
#  returned which is used by the calling program to access that data structure.  The
#  input into this routine is the name of a settings file.  The settings file must
#  contain one of the known types of flight paths.  See Documentation for more information
#  on the format of the settings file.
# -----------------------------------------------------------------------------------------
#  @param dmy_intTag
#         This is the tag that will be returned to the user after the object has
#         been created.
#  @param dmy_enumFlightPath
#         This is the enumeration of the flight path desired in the Catalog.
#  @param dmy_intAtmosphereTag
#         This is the tag of the atmosphere to be used to create the flight path.
#  @param dmy_strRestartFile
#         This is the file name of the user supplied restart.  If the enumeration
#         provided does not exist, it will be loaded from this restart file.
#  @result
#         An integer that is returned 0 when everything occurred correctly.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_fp_load.restype = int
ANOPP2.a2py_fp_load.argtypes = [POINTER(c_int), c_int, c_int, c_char_p]



# -----------------------------------------------------------------------------------------
#  This routine returns the source times for the flight path associated with the tag.
# -----------------------------------------------------------------------------------------
#  @param dmy_intTag
#         This is an integer that is used to access the flight path data structure.
#  @param nTimes
#         The number of source times that are being returned.  This is equal to the size
#         of the dmy_fltSourceTimes Array
#  @param dmy_fltSourceTimes
#         This is the array of source times
#  @result
#         An integer that is returned 0 when everything occurred correctly.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_fp_get_source_times.restype = int
ANOPP2.a2py_fp_get_source_times.argtypes = \
   [c_int, POINTER(c_int), POINTER(POINTER(c_float))]



# -----------------------------------------------------------------------------------------
#  This routine returns the Source Times for the flight path associated with the tag.
# -----------------------------------------------------------------------------------------
#  @param dmy_intTag
#         This is an integer that is used to access the flight path data structure.
#  @param nFlightTimes
#         The number of flight times that are being returned.  This is equal to the size
#         of the dmy_fltFlightTimes Array
#  @param dmy_FlightTimes
#         This is the array of flight times
#  @result
#         An integer that is returned 0 when everything occurred correctly.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_fp_get_flight_times.restype = int
ANOPP2.a2py_fp_get_flight_times.argtypes = \
   [c_int, POINTER(c_int), POINTER(POINTER(c_float))]


# -----------------------------------------------------------------------------------------
#  This routine returns the flight data for the flight path associated with the tag.
# -----------------------------------------------------------------------------------------
#  @param intTag
#         This is an integer that is used to access the flight path data structure.
#  @param intIndex
#         This is the index where the values should be retrieved
#  @param fltFlightTime
#         This is the flight time at the given index
#  @param fltCgLocation
#         This is the location vector for the given index.  This is a one dimensional
#         array of size 3.
#  @param fltBodyToWindAngles
#         This is Body to Wind Angles vector for the given indexThis is a one dimensional
#         array of size 3.
#  @param fltEarthToBodyAngles
#         This is the Earth to Body Angles vector the given indexThis is a one dimensional
#         array of size 3.
#  @result
#         An integer that is returned 0 when everything occurred correctly.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_fp_get_flight_data_at_index.restype = int
ANOPP2.a2py_fp_get_flight_data_at_index.argtypes = \
   [c_int, c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
#  This routine returns the Flight Data for the flight path associated with the tag at
#  the time specified in the input argument.
# -----------------------------------------------------------------------------------------
#  @param intTag
#         This is an integer that is used to access the flight path data structure.
#  @param fltFlightTime
#         This is the time where the Flight Data is desired.
#  @param fltCgLocation
#         This is the location vector for the given time.  This is a one dimensional 
#         array of size 3.
#  @param fltBodyToWindAngles
#         This is Body to Wind Angles vector for the given time. This is a one 
#         dimensional array of size 3.
#  @param fltEarthToBodyAngles
#         This is the Earth to Body Angles vector the given time. This is a one 
#        dimensional array of size 3.
#  @result
#         An integer that is returned 0 when everything occurred correctly.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_fp_get_flight_data_at_time.restype = int
ANOPP2.a2py_fp_get_flight_data_at_time.argtypes = \
   [c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
#  This routine returns the flight cindition for the flight path associated with the tag.
# -----------------------------------------------------------------------------------------
#  @param intTag
#         This is an integer that is used to access the flight path data structure.
#  @param intIndex
#         This is the index where the values should be retrieved
#  @param fltTime
#         This is the time at the given index
#  @param dmy_fltPosition
#         This is a position at the flight condition.  It is a one dimension array of
#         size three, with the X, Y, and Z coordinates
#  @param intLandingGear
#         This is the Landing gear setting at the given index and is represented by a
#         logical value where false (0) corresponds to the landing gear up and true (1)
#         corresponds to the landing gear down
#  @param fltFlap
#         This is the flap setting at the given index
#  @param fltMach
#         This is the Mach Number at the given index
#  @param fltAngleOfAttack
#         This is the Angle of Attack at the given index
#  @result
#         An integer that is returned 0 when everything occurred correctly.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_fp_get_flight_condition_at_index.restype = int
ANOPP2.a2py_fp_get_flight_condition_at_index.argtypes =                           \
   [c_int, c_int, POINTER                                                             \
     (c_float), POINTER(c_float), POINTER(c_float), POINTER(c_int), POINTER(c_float), \
    POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
#  This routine returns the flight condition for the flight path associated with the tag
#  for the time specified as the input.  Note: This is not the Flight Condition object, 
#  but data consistant with the flight condition.
# -----------------------------------------------------------------------------------------
#  @param intTag
#         This is an integer that is used to access the flight path from the manager.
#  @param fltFlightTime
#         This is the time where the Flight Condition is desired.
#  @param fltPosition
#         This is a position at the flight condition.  It is a one dimension array of
#         size three, with the X, Y, and Z coordinates
#  @param fltThrottle
#         This is the throttle sitting at the given time
#  @param blnLandingGear
#         This is the Landing gear setting at the given time and is represented by a
#         logical value where false (0) corresponds to the landing gear up and true (1)
#         corresponds to the landing gear down
#  @param fltFlap
#         This is the flap setting at the given time
#  @param fltMach
#         This is the Mach Number at the given time
#  @param fltAngleOfAttack
#         This is the Angle of Attack at the given time
#  @result
#         An integer that is returned 0 when everything occurred correctly.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_fp_get_flight_condition_at_time.restype = int
ANOPP2.a2py_fp_get_flight_condition_at_time.argtypes =                            \
   [c_int, POINTER                                                                    \
     (c_float), POINTER(c_float), POINTER(c_float), POINTER(c_int), POINTER(c_float), \
    POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
#  This routine returns the Mach for the flight path associated with the tag at the
#  specified time.
# -----------------------------------------------------------------------------------------
#  @param intTag
#         This is an integer that is used to access the flight path from the manager.
#  @param fltFlightTime
#         This is the time where the Mach number is desired
#  @param fltMachNumber
#         This is the Mach number at the desired time
#  @result
#         An integer that is returned 0 when everything occurred correctly.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_fp_get_mach_number_at_time.restype = int
ANOPP2.a2py_fp_get_mach_number_at_time.argtypes = \
   [c_int, POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
#  This routine returns the velocity for the flight path associated with the tag at the
#  specified time.
# -----------------------------------------------------------------------------------------
#  @param intTag
#         This is an integer that is used to access the flight path from the manager.
#  @param fltFlightTime
#         This is the time where the velocity is desired
#  @param fltVelocity
#         This is the velocity at the desired time
#  @result
#         An integer that is returned 0 when everything occurred correctly.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_fp_get_velocity_at_time.restype = int
ANOPP2.a2py_fp_get_velocity_at_time.argtypes = \
   [c_int, POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
#  This routine writes out the information stored in the flight path to an external file.
#  The output includes information about the aircraft at way points time as well as those
#  defined at the flight time.
# -----------------------------------------------------------------------------------------
#  @param intTag
#         This is the tag value of the flight path being written out.
#  @param nCharsFlightData
#         The number of characters in the Flight Data file name
#  @param nCharsFlightCondition
#         The number of characters in the Flight Condition file name
#  @param strFlightDataFileName
#         This is the name of the file that will contain the Flight Data output.
#  @param strFlightConditionFileName
#         This is the name of the file that will contain the Flight Condition output.
#  @result
#         An integer representing success of this operation
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_fp_export.restype = int
ANOPP2.a2py_fp_export.argtypes = [c_int, c_char_p, c_char_p]



#!/usr/bin/python
# -----------------------------------------------------------------------------------------
#  These enumerators are to communicate to the API which built in flight path is to be 
#  loaded from the internal catalog.  This is optional, the user may wish to specify a
#  flight path config file and execute a module to generate a flight path. 
# -----------------------------------------------------------------------------------------

#  This enumerator is for an undefined flight path
a2_fp_undefined = 1

#  This enumerator is for a trivial flight path
a2_fp_trivial = 2

#  This enumerator is for a straight and level flight path using ANOPP.
a2_fp_straight_and_level = 3



#!/usr/bin/python
# -----------------------------------------------------------------------------------------
#  This file is the interface file for the fortran subroutines in the ANOPP2
#  Application Programming Interface (API).  This file should be copied to your local
#  directory and an "#include 'ANOPP2.api.h'" must be present in your
#  program.  See anyone of the demonstrators provided with this API in the Demos
#  directory.  For explanation of how to call and the theory behind each function, 
#  please see the API manual provided with ANOPP2.
# -----------------------------------------------------------------------------------------
#  @file ANOPP2.api.h
#  @author The ANOPP2 Development Team
#  @version 1.0.0
# -----------------------------------------------------------------------------------------



# =========================================================================================
#  First part of this section of the contains interfaces into the available ANOPP2 API 
#  functions.
# =========================================================================================



# -----------------------------------------------------------------------------------------
#  This function initializes the ANOPP2.API by setting internal variables and function
#  parameters that must exist before any other call to the API can be made.
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------
#  This routine executes the unit tests in the ANOPP2.Data Structure.  The unit 
#  tests execute all the tests implemented in the ANOPP2.API.
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_geo_unit_test.restype = bool



# -----------------------------------------------------------------------------------------
#  This routine creates an acoustic data surface in the ANOPP2.API.  A tag is returned
#  which is used by the calling program to access that data surface.  The input into
#  this routine is the name of a settings file.  The configuration file must contain 
#  one of the known types of acoustic data surfaces.  See Documentation for more 
#  information on the format of the settings file.
# -----------------------------------------------------------------------------------------
#  @param intTag
#         This is an integer that is returned by this function.  It is used to access
#         the data structure that is created.
#  @param strConfigurationFile
#         This is the name of the input file that contains the settings for the new
#         acoustic data surface. See Documentation for more information.
#  @result
#         An integer that is returned 0 when everything occurred correctly.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_geo_create.restype = int
ANOPP2.a2py_geo_create.argtypes = [POINTER(c_int), c_char_p]



# -----------------------------------------------------------------------------------------
#  This subroutine adds an offset to the acoustic data surface.  There are 3 offsets that
#  need to be accounted for.  The first is the flow data on the surface offset.  This
#  is typically used when blades are periodic, and the only difference between one blade
#  and another (in terms of flow data) is a time offset.  The second offset is similar
#  to the first and is the geometric offset.  This is only applicable if the geometry
#  is deforming and is typically the same as the flow data offset.  The last offset is
#  an angle offset.  This accounts for the position of the blade with respect to the
#  first blade.  This function takes in these 3 offset values and a tag of the original
#  data surface.  The function returns a new tag value that can be used to refer to the
#  offset acoustic data surface.
# -----------------------------------------------------------------------------------------
#  @param intNewTag
#         This is the tag value of the data surface that is being created inside the
#         API.  This will be the same as the data surface associated to the existing tag
#         with new offset paraeters.
#  @param intExistingTag
#         This is the tag value of the acoustic data surface being copied.
#  @param fltDataTimeOffset
#         This is the time value of the offset of the flow data applied to the surface.
#  @param fltANOPP2.imeOffset
#         This is the time value of the offset of the deformable geometry.
#  @param fltAngleOffset
#         This is the offset of the angle position of the new geometry.  The existing
#         acoustic data surface must have a periodic rotation frame of reference change
#         in order to correctly account for the position of the new data surface.
#  @result
#         An integer communicating success of this operation.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_geo_copy_ads.restype = int
ANOPP2.a2py_geo_copy_ads.argtypes = [POINTER(c_int), c_int, c_float, c_float, c_float]



# -----------------------------------------------------------------------------------------
#  This subroutine calculates integrated metrics from the geometry data structure.  This
#  includes such things as thrust and torque from surfaces representing a blade surface.
#  Currently, the function takes in an enumerator for the desired metric.  Examples are
#  a2_torque for torque or a2_force for integrated forces such as thrust. See
#  documentation for more information on the available metrics.
# -----------------------------------------------------------------------------------------
#  @param intTag
#         This is the tag representing the geometry data structure.
#  @param fltTime
#         This is the time that the metric will be calculated.
#  @param enumMetric
#         This enumerator is the desired metric for example a2_torque or
#         a2_force.
#  @param nDimensions
#         This is the number of dimensions in the metric to be calculated. For example, 
#         if force is the desired metric, this should be 3 corresponding to its 3 
#         components, Fx, Fy, and Fz.
#  @param fltMetric
#         This is an allocatable array that is allocated by this function and set to the
#         result.  For example, if force is specified, this is an array of size 3 and
#         the elements of the fltMetric array are set to Fx, Fy, and Fz.  
#  @result
#         An integer representing success of this operation.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_geo_calc_metric.restype = int
ANOPP2.a2py_geo_calc_metric.argtypes = \
   [c_int, c_float, c_int, c_int, POINTER(c_float)]



# -----------------------------------------------------------------------------------------
#  This routine creates an wing data structure in the ANOPP2 API.  A tag is returned
#  which is used by the calling program to access that data structure.  The input into
#  this routine is the name of a settings file.  The settings file must contain one of
#  the known types of wings.  See Documentation for more information on the format of 
#  the configuration file.
# -----------------------------------------------------------------------------------------
#  @param intTag
#         This is an integer that is returned by this function.  It is used to access
#         the data structure that is created.
#  @param strConfigurationFile
#         This is the name of the input file that contains the settings for the new
#         wing. See Documentation for more information.
#  @result
#         An integer that is returned 0 when everything occurred correctly.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_geo_create_wing.restype = int
ANOPP2.a2py_geo_create_wing.argtypes = [POINTER(c_int), c_char_p]



# ---------------------------------------------------------------------------------------
#  This function takes in a tag representing a geometry and returns true if it exists
#  in the API and false if it does not.
# ---------------------------------------------------------------------------------------
#  @param intTag
#         This is the tag associated to the geometry that is being searched for.
#  @result
#         A bool that is returned true if the geometry exists and false if it does not.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_geo_exists.restype = bool
ANOPP2.a2py_geo_exists.argtypes = [c_int]



# -----------------------------------------------------------------------------------------
#  This routine accesses the ANOPP2.API and tells it to export a ANOPP2.Data
#  Structure.  The routine accepts a geometry tag and an output file name and causes 
#  the ANOPP2.API to write out the data structure to the file in the specified format
#  for a given target application.
# -----------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         The tag that connects the application code to the ANOPP2 API.
#  @param strFileName
#         This is the name of the file that the Export routine writes.
#  @param enumFormat
#         This is the format of the file: options may include formatted or binary.
#  @param enumProgram
#         This is the program that will eventually read the file.  This may include
#         Tecplot or NetCDF.
#  @result
#         An integer that is 0 if everything has occurred as expected.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_geo_export.restype = int
ANOPP2.a2py_geo_export.argtypes = [c_int, c_char_p, c_int, c_int]



#!/usr/bin/python
# =========================================================================================
#  Next part of this section of the interface file contains hardcoded enumerators used by
#  the user's program to communicate parameters and settings to the API.
# =========================================================================================



# ---------------------------------------------------------------------------------------
#  These enumerators are to communicate to the API, certain default objects that can be
#  loaded via the catalog.  This is optional.  A user may also specify an input
#  configuration file if they wish with more detail on the object to be constructed.
#  See User's Manual for more information.
# ---------------------------------------------------------------------------------------
#  


#  The first enumerator is for the force of a surface. This is the integral of pressure time \
#   the normal vector for an impenetrable surface or p*nj + rho*ui*                          \
#    (un - vn) for an impenetrable surface.
a2_force = 1

#  This is the torque of a surface. It is the cross product of r times the force.
a2_torque = 2

#!/usr/bin/python
# -----------------------------------------------------------------------------------------
#  This is the ANOPP2.API interface file.  It contains definitions for all the
#  functions available in the observer API.  This includes initializations, creation,
#  insertion, exporting, etc.  See API manual for more information.
# -----------------------------------------------------------------------------------------
#  @file ANOPP2.api.f90
#  @author The ANOPP2 Development Team
#  @version 1.0.0
# -----------------------------------------------------------------------------------------



# =========================================================================================
#  First part of this section of the contains interfaces into the available ANOPP2.API
#  functions.
# =========================================================================================





# ---------------------------------------------------------------------------------------
#  This subroutine initializes the observer API and should be included at the very
#  start of your program (before any other subroutines are called).  The debug flag
#  turns on/off debugging for the entire system.
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------
#  This routine executes the unit tests in the ANOPP2.Data Structure.  The unit
#  tests execute all the tests implemented in the ANOPP2.API.
# ---------------------------------------------------------------------------------------
#  @result
#         An integer that is the total number of failed asserts during unit testing.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_unit_test.restype = int



# ---------------------------------------------------------------------------------------
#  This routine creates an ANOPP2.Data Structure in the ANOPP2.API.  A tag is
#  returned which is used by the calling program to access that Data Structure.  The
#  input into this routine is the name of a configuration file (also known as Settings
#  file).  The configuration file must contain one of the known types of observers. By
#  providing the values of several parameters in these configuration files, the Observer
#  API generates one or more nodes that define the geometry of the ANOPP2.
# ---------------------------------------------------------------------------------------
#  @param intTag
#         This is an integer that is returned by this function.  It is used to access
#         the data structure that is created.
#  @param strConfigurationFile
#         This is the name of the input file that contains the settings for the new
#         observer. See Documentation for more information.
#  @result
#         An integer that is returned 0 when everything occurred correctly.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_create.restype = int
ANOPP2.a2py_obs_create.argtypes = [POINTER(c_int), c_char_p]



# ---------------------------------------------------------------------------------------
#  This routine will destroy an observer in the ANOPP2.API. The entire data structure,
#  including any noise results, calculated metrics, geometric configurations, and
#  motion will be deleted.  The tag will be unassociated to any information within the
#  data structure.
# ---------------------------------------------------------------------------------------
#  @param intTag
#         This is the tag associated with the ANOPP2.API being destroyed.
#  @result
#         An integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_delete.restype = int
ANOPP2.a2py_obs_delete.argtypes = [POINTER(c_int)]



# ---------------------------------------------------------------------------------------
#  This routine saves the ANOPP2.API in a preopened file by exporting
#  all internal data.  The file format is specific to the data structure being written
#  out.
# ---------------------------------------------------------------------------------------
#  @param intTag
#         This is an integer representation of the observer to be saved
#  @param strRestartFile
#         This is the name of the file being created.
#  @result
#         An integer representing success of this function
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_save.restype = int
ANOPP2.a2py_obs_save.argtypes = [c_int, c_char_p]



# ---------------------------------------------------------------------------------------
#  This routine creates an ANOPP2.API in the ANOPP2 API.  A tag is
#  returned which is used by the calling program to access that data structure.  The
#  input into this routine is the name of a settings file.  The settings file must
#  contain one of the known types of observers.  See Documentation for more information
#  on the format of the settings file.
# ---------------------------------------------------------------------------------------
#  @param intTag
#         This is the tag that will be returned to the user after the object has
#         been created.
#  @param enumObserver
#         This is the enumeration of the observer desired in the Catalog.
#  @param strRestartFile
#         This is the file name of the user supplied restart file.  If the enumeration
#         provided does not exist, the data structure  will be created form this restart
#         file.
#  @param nResults
#         This is the size of the result tags array returned by this function.
#  @param intResultTags
#         If the observer is loaded from a restart file, this pointer array will point
#         to a number of integers that are the result tags.  This is left as null if the
#         observer is loaded from the catalog.
#  @result
#         An integer that is returned 0 when everything occurred correctly.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_load.restype = int
ANOPP2.a2py_obs_load.argtypes = \
   [POINTER(c_int), c_int, c_char_p, POINTER(c_int), POINTER(POINTER(c_int))]



# ---------------------------------------------------------------------------------------
#  This routine sends the noise results at a given node to a destination processor.
#  This routine will use the MPI library (if available) to send the data.  See MPI
#  library detail for more information on Message Passing Interface (MPI).
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         The ANOPP2 tag associated with the observer that contains the data.
#  @param intNode
#         The observer node of the data being sent.
#  @param intResultTag
#         The tag of the result being sent.
#  @param intDestination
#         The rank of the desination processor.
#  @param intMessageTag
#         The MPI tag of the message.
#  @result
#         An integer reprenting success of this operation
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_send.restype = int
ANOPP2.a2py_obs_send.argtypes = [c_int, c_int, c_int, c_int, c_int]



# ---------------------------------------------------------------------------------------
#  This routine receives the noise results at a given node from a source processor.
#  This routine will use the MPI library (if available) to receive the data.  See MPI
#  library detail for more information on Message Passing Interface (MPI).
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         The ANOPP2 tag associated with the observer that will contain the data.
#  @param intNode
#         The observer node of the data being received
#  @param intResultTag
#         The tag of the result being received.
#  @param intSource
#         The rank of the source processor.
#  @param intMessageTag
#         The MPI tag of the message.
#  @result
#         An integer reprenting success of this operation
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_receive.restype = int
ANOPP2.a2py_obs_receive.argtypes = [c_int, c_int, c_int, c_int, c_int]



# ---------------------------------------------------------------------------------------
#  This routine broadcasts the noise results on the observer inthe master process to the
#  the observers of all the slave processes. This routine will use the MPI library
#  (if available) to broadcast the data.  See MPI library detail for more information on
#  Message Passing Interface (MPI).
# ---------------------------------------------------------------------------------------
#  @param dmy_intANOPP2.ag
#         The ANOPP2 tag associated with the observer that contains the data.
#  @param dmy_nResults
#         The number of results in the results array.
#  @param dmy_intResultTags
#         An array of tags of the results being broadcast.
#  @result
#         An integer reprenting success of this operation
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_broadcast.restype = int
ANOPP2.a2py_obs_broadcast.argtypes = [c_int, c_int, POINTER(c_int)]



# ---------------------------------------------------------------------------------------
#  This function takes in a tag representing an observer and returns true if it exists
#  in the API and false if it does not.
# ---------------------------------------------------------------------------------------
#  @param intTag
#         This is the tag associated to the observer that is being searched for.
#  @result
#         A bool that is returned true if the observer exists and false if it does not.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_exists.restype = bool
ANOPP2.a2py_obs_exists.argtypes = [c_int]



# ---------------------------------------------------------------------------------------
#  This function takes in a tag representing an observer and observer result and returns
#  true if they exists in the API and false if it does not.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated to the observer that is being searched for.
#  @param intResultTag
#         This is the tag associated with the observer result.
#  @result
#         An integer that is returned 0 if the observer exists.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_result_exists.restype = int
ANOPP2.a2py_obs_result_exists.argtypes = [c_int, c_int]



# ---------------------------------------------------------------------------------------
#  This function returns a string of information about an observer structure in the
#  ANOPP2.API.  The information string will contain information such as geometric
#  parameters (number of points in certain directions), results and what metric are
#  available in each, etc.
# ---------------------------------------------------------------------------------------
#  @param intTag
#         The tag value associated to the data structure of interest.
#  @param strInformation
#         A string of information that is returned by this function.
#  @param nResults
#         This is the number of result tags provided
#  @param intResultTags
#         This is an array of Result Tags associated with each of the results.
#  @param nMetrics
#         This is the maximum number of results (second dimension of available metrics).
#  @param enumAvailableMetrics
#         This is a two-dimensional array of Available Metrics, the first dimension is
#         the results and the second is the maximum number of metrics available.
#  @result
#         An integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_info.restype = int
ANOPP2.a2py_obs_info.argtypes = \
   [c_int, c_char_p, POINTER     \
     (c_int), POINTER(c_int), POINTER(c_int), POINTER(POINTER(c_int))]



# ---------------------------------------------------------------------------------------
#  This function returns the number of nodes in an observer geometry.
# ---------------------------------------------------------------------------------------
#  @param intTag
#         This is the tag associated to the observer that is being accessed
#  @param nNodes
#         This is the number of nodes in the geometry of the observer.
#  @result
#         An integer that is returned 0 if the observer exists.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_number_of_nodes.restype = int
ANOPP2.a2py_obs_number_of_nodes.argtypes = [c_int, POINTER(c_int)]



# ---------------------------------------------------------------------------------------
#  This function returns the number of results that are in the observer API.
# ---------------------------------------------------------------------------------------
#  @param intTag
#         This is the tag of the observer in the API.
#  @param nResults
#         This is the number of results, returned by this function.
#  @result
#         An integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_number_of_results.restype = int
ANOPP2.a2py_obs_number_of_results.argtypes = [c_int, POINTER(c_int)]




# ---------------------------------------------------------------------------------------
#  This function returns the number of segments for a given result in an observer
#  structure.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated to the observer that is being accessed
#  @param intResultTag
#         This ist he tag associated with the result being accessed.
#  @param iNode
#         This is the node number of interest
#  @param nSegments
#         This is the number of segments in the geometry of the observer.
#  @result
#         An integer that is returned 0 if the observer exists.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_number_of_segments.restype = int
ANOPP2.a2py_obs_number_of_segments.argtypes = [c_int, c_int, c_int, POINTER(c_int)]



# ---------------------------------------------------------------------------------------
#  This routine initializes new results in the ANOPP2.API.  New results
#  must be initialized in the ANOPP2.API before noise can be added to it.
#  This routine takes in a tag representation of the observer and a number of results
#  that will be added into the ANOPP2.API.  An array is allocated to the
#  size of the number of results that will be added.  This array of result tags is then
#  used to insert noise later in the system.
# ---------------------------------------------------------------------------------------
#  @param intTag
#         This is an integer representation of the observer to be modified with a
#         new result (or several).
#  @param nChars
#         This is the length of the strings in the array of result names.
#  @param nResults
#         This is the number of results that are going to be added.
#  @param strResultNames
#         These are the names of the results that are being added to the system.  They
#         are stored in the ANOPP2.API and used when Exporting on the
#         results.
#  @param intResultTags
#         These are the tags of the results after they are initialized in the observer
#         data structure
#  @result
#         An integer representing success of the creation of the new result
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_new_results.restype = int
ANOPP2.a2py_obs_new_results.argtypes = \
   [c_int, c_int, c_int, c_char_p, POINTER(POINTER(c_int))]




# ---------------------------------------------------------------------------------------
#  This function inserts a node into the ANOPP2.API.  The arguments include
#  the position of the new node in the local frame of reference.  The new node will move
#  as defined by the kinematics list, similar to the already existing nodes in the data
#  structure.  The noise associated with the new node will not exist, no addition
#  acoustic data is created.  This routine may not work with all possible configurations
#  of the observer's geometry.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag that is associated with the ANOPP2.API being
#         modified.
#  @param fltPosition
#         This is an array of size 3 of single precision reals that is the position of the
#         new node.
#  @result
#         This is an integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_new_node.restype = int
ANOPP2.a2py_obs_new_node.argtypes = [c_int, POINTER(c_float)]



# ---------------------------------------------------------------------------------------
#  This routine deletes a result in the ANOPP2.API.  The result is removed
#  from memory and the data structure completely.  There is an optional argument that is
#  a node number.  If the node number is 0, results for all nodes will be deleted.  If
#  the node number is not 0 (and less than the total number of observer nodes) then only
#  the result at that node number is destroyed.
# ---------------------------------------------------------------------------------------
#  @param intTag
#         This is an integer representation of the observer to be modified by deleting
#         a result (or several).
#  @param nResults
#         This is the number of results that are there in the ANOPP2.Data Structure for
#         the node.
#  @param intResultTags
#         These are the tags of the results after they are deleted from the observer data
#         structure
#  @param intNodeNumber
#         This is the number of the node whose results are going to be deleted.  If this
#         is given as zero, all nodes will have their results deleted.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_delete_results.restype = int
ANOPP2.a2py_obs_delete_results.argtypes = [c_int, c_int, POINTER(c_int), c_int]


# ---------------------------------------------------------------------------------------
#  This function deletes a metric from a given result in the ANOPP2.API.
#  A tag is provided for the ANOPP2.API and the result.  An enumerator
#  for the metric to be deleted is also provided.
# ---------------------------------------------------------------------------------------
#  @param intTag
#         This is an integer representation of the observer to be modified by deleting
#         a metric.
#  @param intResultTags
#         These are the tags of the results after they are modified the observer data
#         structure
#  @param enumMetric
#         This is the enumerator for the metric that is to be deleted.  The list of
#         enumerators that are available are in this file.
#  @result
#         An integer represeting success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_delete_metric.restype = int
ANOPP2.a2py_obs_delete_metric.argtypes = [c_int, c_int, POINTER(c_int), c_int]



# ---------------------------------------------------------------------------------------
#  This routine returns the position of the ith node in the observer geometry.  The
#  function returns an array of size 3 that is the position of the observer in the global
#  frame.
# ---------------------------------------------------------------------------------------
#  @param intTag
#         The integer tag of the observer contained within the ANOPP2.API
#  @param iNode
#         This is the ith node index.
#  @param fltTime
#         This is the time that the positions are wanted.
#  @param enumFrame
#         This is an enumeration for the frame of reference of the position, it can be
#         either local or global
#  @param fltPosition
#         A two dimensional array that returns the 3 dimensional node locations
#  @result
#         An integer that is 0 if everything has occurred as expected.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_position.restype = int
ANOPP2.a2py_obs_position.argtypes = [c_int, c_int, c_float, c_int, POINTER(c_float)]



# ---------------------------------------------------------------------------------------
#  This routine returns the positions of the observer locations at a time.  It returns
#  an integer that is the number of positions and an array of the positions.  The
#  returned array has dimensions 3 by the number of observer nodes.
# ---------------------------------------------------------------------------------------
#  @param intTag
#         The integer tag of the observer contained within the ANOPP2.API
#  @param fltTime
#         This is the time that the positions are wanted.
#  @param nPositions
#         This is the number of positions that is returned by this function.
#  @param enumFrame
#         This is an enumeration for the frame of reference of the position, it can be
#         either local or global
#  @param fltPositions
#         A two dimensional array that returns the 3 dimensional node locations
#  @result
#         An integer that is 0 if everything has occurred as expected.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_positions.restype = int
ANOPP2.a2py_obs_positions.argtypes = \
   [c_int, c_float, c_int, POINTER(c_int), POINTER(POINTER(c_float))]



# ---------------------------------------------------------------------------------------
#  This routine inserts a list of acoustic pressure time history into the observer
#  data structure. A tag is provided that is the observer that is receiving the noise.
#  A list of prediction tags are provided for the results being inserted.  Reception
#  times are also provided for each observer position.  A list of time histories for
#  the acoustic pressure are given as well.  The SPLs are kept in a 3 dimensional array
#  of size number of results by number of observer by number of reception times.  A
#  success value is returned communicating the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nNodes
#         This is the number of nodes in the ANOPP2.Data Structure.
#  @param nTimes
#         This is the number of Reception Times in the Pressure-Time History array.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTimes
#         These are the segment times of the observers.  This time is recorded by the
#         observer data segment
#  @param fltReceptionTimes
#         These are the reception times of the pressure time history that is being
#         inserted into the ANOPP2.API.
#  @param fltAcousticPressures
#         These are the acoustic pressures.  This is a 3 dimensional array where the
#         first dimension is the number of unique predictions, second dimension is
#         number of observer points, and third is the number of reception times in the
#         pressure time history.
#  @param enumTimeHistoryGroup
#         This is an enumeration setting that tells the ANOPP2.API if this
#         is for a segment or for the entire time range.
#  @param enumNoiseLevelTypes
#         These are the characteristics of the results that define whether the noise
#         data is absolute or change in levels.
#  @param blnIncludesFlightEffects
#         This array of flags communicates whether the input being provided to this
#         routine includes the Doppler frequency shift and convective amplification.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_pressure.restype = int
ANOPP2.a2py_obs_insert_pressure.argtypes =                                         \
   [c_int, c_int, POINTER                                                          \
     (c_int), c_int, POINTER(c_float), c_int, POINTER(c_float), POINTER(c_float), \
    c_int, POINTER(c_int), POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine inserts a list of acoustic pressure time history for a node into the
#  ANOPP2.API. A tag is provided that is the observer that is receiving the
#  noise. A list of prediction tags are provided for the results being inserted.
#  Reception times are also provided for each observer position.  A list of time
#  histories for the acoustic pressures are given as well. The pressures are kept
#  in a 2 dimensional array of size number of results by number of reception times. A
#  success value is returned communicating the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nTimes
#         This is the number of Reception Times in the Pressure-Time History array.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTime
#         These is the segment times of the observers.  This time is recorded by the
#         ANOPP2.API.
#  @param fltReceptionTimes
#         These are the reception times of the pressure time history that is being
#         inserted into the ANOPP2.API.
#  @param fltAcousticPressures
#         These are the acoustic pressures.  This is a 2 dimensional array where the
#         first dimension is the number of unique predictions and the second dimension
#         is the number of reception times in the pressure time history.
#  @param intNodeNumber
#         This is the node number for which the pressure time history has to
#         inserted.
#  @param enumTimeHistoryGroup
#         This is an enumeration setting that tells the ANOPP2.API if this
#         is for a segment or for the entire time range.
#  @param enumNoiseLevelTypes
#         These are the characteristics of the results that define whether the noise
#         data is absolute or change in levels.
#  @param blnIncludesFlightEffects
#         This array of flags communicates whether the input being provided to this
#         routine includes the Doppler frequency shift and convective amplification.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_pressure_by_node.restype = int
ANOPP2.a2py_obs_insert_pressure_by_node.argtypes =                                \
   [c_int, c_int, POINTER                                                         \
     (c_int), c_float, c_int, POINTER(c_float), POINTER(c_float), c_int, c_int, \
    POINTER(c_int), POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine inserts a list of pressure sensitivity time history into the observer
#  data structure. A tag is provided that is the observer that is receiving the noise.
#  A list of prediction tags are provided for the results being inserted.  Reception
#  times are also provided for each observer position.  A list of time histories for
#  the pressure sensitivity are kept in a 4 dimensional array of size number of results
#  by number of observer by number of reception times by the total size of the
#  sensitivity array. The dimensions of the sensitivity matrix are provided.  A success
#  value is returned communicating the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nNodes
#         This is the number of nodes in the ANOPP2.Data Structure.
#  @param nTimes
#         This is the number of Reception Times in the Pressure-Time History array.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTimes
#         These are the segment times of the observers.  This time is recorded by the
#         observer data segment
#  @param fltReceptionTimes
#         These are the reception times of the pressure time history that is being
#         inserted into the ANOPP2.API.
#  @param nMatrix
#         This is the total size of the sensitivity matrix, the size of the fourth
#         dimension of the pressure sensitivity array.  This is equal to all elements
#         of the dimensions array multiplied together.
#  @param fltPressureSensitivity
#         These are the pressure sensitivities.  This is a 4 dimensional array where
#         the first dimension is the number of unique predictions, second dimension is
#         number of observer points, the third is the number of reception times in the
#         time history, and the fourth is the total size of the sensitivity matrix.
#  @param nDimensions
#         This is the size of the sensitivity dimensions array.
#  @param intSensitivityDimensions
#         An array of integers that are the dimensions of the sensitivity matrix.
#  @param enumTimeHistoryGroup
#         This is an enumeration setting that tells the ANOPP2.API if this
#         is for a segment or for the entire time range.
#  @param enumNoiseLevelTypes
#         These are the characteristics of the results that define whether the noise
#         data is absolute or change in levels.
#  @param blnIncludesFlightEffects
#         This array of flags communicates whether the input being provided to this
#         routine includes the Doppler frequency shift and convective amplification.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_pressure_sensitivity.restype = int
ANOPP2.a2py_obs_insert_pressure_sensitivity.argtypes =                   \
   [c_int, c_int, POINTER                                                \
     (c_int), c_int, POINTER(c_float), c_int, POINTER(c_float), c_int, \
    POINTER(c_float), c_int, POINTER(c_int), c_int, POINTER(c_int), POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine inserts a list of pressure sensitivity time history for a node into the
#  ANOPP2.API. A tag is provided that is the observer that is receiving the
#  noise. A list of prediction tags are provided for the results being inserted.
#  Reception times are also provided for each observer position.  A list of time
#  histories for the acoustic pressures are given as well. The pressures are kept
#  in a 3 dimensional array of size number of results by number of reception times by
#  the total size of the sensitivity matrix.  The dimensions of that matrix are also
#  provided.  A success value is returned communicating the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nTimes
#         This is the number of Reception Times in the Pressure-Time History array.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTime
#         These is the segment times of the observers.  This time is recorded by the
#         ANOPP2.API.
#  @param fltReceptionTimes
#         These are the reception times of the pressure time history that is being
#         inserted into the ANOPP2.API.
#  @param nMatrix
#         This is the total size of the sensitivity matrix, the size of the fourth
#         dimension of the pressure sensitivity array.  This is equal to all elements
#         of the dimensions array multiplied together.
#  @param fltPressureSensitivity
#         These are the pressure sensivitiy.  This is a 3 dimensional array where the
#         first dimension is the number of unique predictions, the second dimension
#         is the number of reception times in the pressure time history, and the
#         third dimensions is the total size of the sensitivity matrix.
#  @param nDimensions
#         This is the size of the sensitivity dimensions array.
#  @param intSensitivityDimensions
#         An array of integers that are the dimensions of the sensitivity matrix.
#  @param intNodeNumber
#         This is the node number for which the pressure time history has to
#         inserted.
#  @param enumTimeHistoryGroup
#         This is an enumeration setting that tells the ANOPP2.API if this
#         is for a segment or for the entire time range.
#  @param enumNoiseLevelTypes
#         These are the characteristics of the results that define whether the noise
#         data is absolute or change in levels.
#  @param blnIncludesFlightEffects
#         This array of flags communicates whether the input being provided to this
#         routine includes the Doppler frequency shift and convective amplification.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_pressure_sensitivity_by_node.restype = int
ANOPP2.a2py_obs_insert_pressure_sensitivity_by_node.argtypes =                    \
   [c_int, c_int, POINTER                                                         \
     (c_int), c_float, c_int, POINTER(c_float), c_int, POINTER(c_float), c_int, \
    POINTER(c_int), c_int, c_int, POINTER(c_int), POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine inserts a list of acoustic velocity time history into the observer
#  data structure. A tag is provided that is the observer that is receiving the noise.
#  A list of prediction tags are provided for the results being inserted.  Reception
#  times are also provided for each observer position.  A list of time histories for
#  the acoustic velocity are given as well.  The values are kept in a 4 dimensional array
#  of size number of results by number of observer by number of reception times by 3.  A
#  success value is returned communicating the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nNodes
#         This is the number of nodes in the ANOPP2.Data Structure.
#  @param nTimes
#         This is the number of Reception Times in the Pressure-Time History array.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTimes
#         These are the segment times of the observers.  This time is recorded by the
#         observer data segment
#  @param fltReceptionTimes
#         These are the reception times of the velocity time history that is being
#         inserted into the ANOPP2.API.
#  @param fltAcousticVelocity
#         These are the acoustic velocities.  This is a 4 dimensional array where the
#         first dimension is the number of unique predictions, second dimension is
#         number of observer points, and third is the number of reception times in the
#         velocity time history, and the fourth is 3.
#  @param enumTimeHistoryGroup
#         This is an enumeration setting that tells the ANOPP2.API if this
#         is for a segment or for the entire time range.
#  @param enumNoiseLevelTypes
#         These are the characteristics of the results that define whether the noise
#         data is absolute or change in levels.
#  @param blnIncludesFlightEffects
#         This array of flags communicates whether the input being provided to this
#         routine includes the Doppler frequency shift and convective amplification.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_velocity.restype = int
ANOPP2.a2py_obs_insert_velocity.argtypes =                                         \
   [c_int, c_int, POINTER                                                          \
     (c_int), c_int, POINTER(c_float), c_int, POINTER(c_float), POINTER(c_float), \
    c_int, POINTER(c_int), POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine inserts a list of acoustic velocity time history for a node into the
#  ANOPP2.API. A tag is provided that is the observer that is receiving the
#  noise. A list of prediction tags are provided for the results being inserted.
#  Reception times are also provided for each observer position.  A list of time
#  histories for the acoustic velocity are given as well. The velocities are kept
#  in a 3 dimensional array of size number of results by number of reception times. A
#  success value is returned communicating the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nTimes
#         This is the number of Reception Times in the Velocity-Time History array.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTime
#         These is the segment times of the observers.  This time is recorded by the
#         ANOPP2.API.
#  @param fltReceptionTimes
#         These are the reception times of the velocity time history that is being
#         inserted into the ANOPP2.API.
#  @param fltAcousticVelocity
#         These are the acoustic velocities.  This is a 3 dimensional array where the
#         first dimension is the number of unique predictions and the second dimension
#         is the number of reception times in the velocity time history, and the third
#         dimension is 3 for a vector quantity.
#  @param intNodeNumber
#         This is the node number for which the acoustic velocity time history has to
#         inserted.
#  @param enumTimeHistoryGroup
#         This is an enumeration setting that tells the ANOPP2.API if this
#         is for a segment or for the entire time range.
#  @param enumNoiseLevelTypes
#         These are the characteristics of the results that define whether the noise
#         data is absolute or change in levels.
#  @param blnIncludesFlightEffects
#         This array of flags communicates whether the input being provided to this
#         routine includes the Doppler frequency shift and convective amplification.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_velocity_by_node.restype = int
ANOPP2.a2py_obs_insert_velocity_by_node.argtypes =                                \
   [c_int, c_int, POINTER                                                         \
     (c_int), c_float, c_int, POINTER(c_float), POINTER(c_float), c_int, c_int, \
    POINTER(c_int), POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine inserts a list of velocity sensitivity time history into the observer
#  data structure. A tag is provided that is the observer that is receiving the noise.
#  A list of prediction tags are provided for the results being inserted.  Reception
#  times are also provided for each observer position.  A list of time histories for
#  the velocity sensitivity are kept in a 4 dimensional array of size number of results
#  by number of observer by number of reception times by the total size of the
#  sensitivity array. The dimensions of the sensitivity matrix are provided.  A success
#  value is returned communicating the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nNodes
#         This is the number of nodes in the ANOPP2.Data Structure.
#  @param nTimes
#         This is the number of Reception Times in the Velocity-Time History array.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTimes
#         These are the segment times of the observers.  This time is recorded by the
#         observer data segment
#  @param fltReceptionTimes
#         These are the reception times of the velocity time history that is being
#         inserted into the ANOPP2.API.
#  @param nMatrix
#         This is the total size of the sensitivity matrix, the size of the fourth
#         dimension of the velocity sensitivity array.  This is equal to all elements
#         of the dimensions array multiplied together.
#  @param fltVelocitySensitivity
#         These are the velocity sensitivities.  This is a 4 dimensional array where
#         the first dimension is the number of unique predictions, second dimension is
#         number of observer points, the third is the number of reception times in the
#         time history, and the fourth is the total size of the sensitivity matrix.
#  @param nDimensions
#         This is the size of the sensitivity dimensions array.
#  @param intSensitivityDimensions
#         An array of integers that are the dimensions of the sensitivity matrix.
#  @param enumTimeHistoryGroup
#         This is an enumeration setting that tells the ANOPP2.API if this
#         is for a segment or for the entire time range.
#  @param enumNoiseLevelTypes
#         These are the characteristics of the results that define whether the noise
#         data is absolute or change in levels.
#  @param blnIncludesFlightEffects
#         This array of flags communicates whether the input being provided to this
#         routine includes the Doppler frequency shift and convective amplification.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_velocity_sensitivity.restype = int
ANOPP2.a2py_obs_insert_velocity_sensitivity.argtypes =                   \
   [c_int, c_int, POINTER                                                \
     (c_int), c_int, POINTER(c_float), c_int, POINTER(c_float), c_int, \
    POINTER(c_float), c_int, POINTER(c_int), c_int, POINTER(c_int), POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine inserts a list of velocity sensitivity time history for a node into the
#  ANOPP2.API. A tag is provided that is the observer that is receiving the
#  noise. A list of prediction tags are provided for the results being inserted.
#  Reception times are also provided for each observer position.  A list of time
#  histories for the acoustic velocitys are given as well. The velocitys are kept
#  in a 3 dimensional array of size number of results by number of reception times by
#  the total size of the sensitivity matrix.  The dimensions of that matrix are also
#  provided.  A success value is returned communicating the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nTimes
#         This is the number of Reception Times in the Velocity-Time History array.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTime
#         These is the segment times of the observers.  This time is recorded by the
#         ANOPP2.API.
#  @param fltReceptionTimes
#         These are the reception times of the velocity time history that is being
#         inserted into the ANOPP2.API.
#  @param nMatrix
#         This is the total size of the sensitivity matrix, the size of the fourth
#         dimension of the velocity sensitivity array.  This is equal to all elements
#         of the dimensions array multiplied together.
#  @param fltVelocitySensitivity
#         These are the velocity sensivitiy.  This is a 3 dimensional array where the
#         first dimension is the number of unique predictions, the second dimension
#         is the number of reception times in the velocity time history, and the
#         third dimensions is the total size of the sensitivity matrix.
#  @param nDimensions
#         This is the size of the sensitivity dimensions array.
#  @param intSensitivityDimensions
#         An array of integers that are the dimensions of the sensitivity matrix.
#  @param intNodeNumber
#         This is the node number for which the velocity time history has to
#         inserted.
#  @param enumTimeHistoryGroup
#         This is an enumeration setting that tells the ANOPP2.API if this
#         is for a segment or for the entire time range.
#  @param enumNoiseLevelTypes
#         These are the characteristics of the results that define whether the noise
#         data is absolute or change in levels.
#  @param blnIncludesFlightEffects
#         This array of flags communicates whether the input being provided to this
#         routine includes the Doppler frequency shift and convective amplification.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_velocity_sensitivity_by_node.restype = int
ANOPP2.a2py_obs_insert_velocity_sensitivity_by_node.argtypes =                    \
   [c_int, c_int, POINTER                                                         \
     (c_int), c_float, c_int, POINTER(c_float), c_int, POINTER(c_float), c_int, \
    POINTER(c_int), c_int, c_int, POINTER(c_int), POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine inserts a list of pressure gradient time history into the observer
#  data structure. A tag is provided that is the observer that is receiving the noise.
#  A list of prediction tags are provided for the results being inserted.  Reception
#  times are also provided for each observer position.  A list of time histories for
#  the pressure gradients are given as well.  The values are kept in a 4 dimensional array
#  of size number of results by number of observer by number of reception times by 3.  A
#  success value is returned communicating the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nNodes
#         This is the number of nodes in the ANOPP2.Data Structure.
#  @param nTimes
#         This is the number of Reception Times in the Gradient-Time History array.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTimes
#         These are the segment times of the observers.  This time is recorded by the
#         observer data segment
#  @param fltReceptionTimes
#         These are the reception times of the pressure time history that is being
#         inserted into the ANOPP2.API.
#  @param fltPressureGradient
#         These are the pressure gradient.  This is a 4 dimensional array where the
#         first dimension is the number of unique predictions, second dimension is
#         number of observer points, and third is the number of reception times in the
#         pressure gradient time history, and the last is 3 for a vector quantity.
#  @param enumTimeHistoryGroup
#         This is an enumeration setting that tells the ANOPP2.API if this
#         is for a segment or for the entire time range.
#  @param enumNoiseLevelTypes
#         These are the characteristics of the results that define whether the noise
#         data is absolute or change in levels.
#  @param blnIncludesFlightEffects
#         This array of flags communicates whether the input being provided to this
#         routine includes the Doppler frequency shift and convective amplification.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_gradient.restype = int
ANOPP2.a2py_obs_insert_gradient.argtypes =                          \
   [c_int, c_int, POINTER(c_int), c_int, POINTER(c_float), c_int, \
    POINTER(c_float), POINTER(c_float), c_int, POINTER(c_int), POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine inserts a list of pressure gradient time history for a node into the
#  ANOPP2.API. A tag is provided that is the observer that is receiving the
#  noise. A list of prediction tags are provided for the results being inserted.
#  Reception times are also provided for each observer position.  A list of time
#  histories for the pressure gradients are given as well. The pressures are kept
#  in a 3 dimensional array of size number of results by number of reception times. A
#  success value is returned communicating the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nTimes
#         This is the number of Reception Times in the Gradient-Time History array.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTime
#         These is the segment times of the observers.  This time is recorded by the
#         ANOPP2.API.
#  @param fltReceptionTimes
#         These are the reception times of the pressure time history that is being
#         inserted into the ANOPP2.API.
#  @param fltPressureGradient
#         These are the pressure gradient.  This is a 3 dimensional array where the
#         first dimension is the number of unique predictions and the second dimension
#         is the number of reception times in the pressure time history, and the last
#         is 3 for vector quantity.
#  @param intNodeNumber
#         This is the node number for which the pressure time history has to
#         inserted.
#  @param enumTimeHistoryGroup
#         This is an enumeration setting that tells the ANOPP2.API if this
#         is for a segment or for the entire time range.
#  @param enumNoiseLevelTypes
#         These are the characteristics of the results that define whether the noise
#         data is absolute or change in levels.
#  @param blnIncludesFlightEffects
#         This array of flags communicates whether the input being provided to this
#         routine includes the Doppler frequency shift and convective amplification.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_gradient_by_node.restype = int
ANOPP2.a2py_obs_insert_gradient_by_node.argtypes =                     \
   [c_int, c_int, POINTER(c_int),                                     \
    c_float, c_int, POINTER(c_float), POINTER(c_float), c_int, c_int, \
    POINTER(c_int), POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine inserts a list of tone spectra into the ANOPP2.API.
#  A tag is provided that is the observer that is receiving the noise. A list of
#  prediction tags are provided for the results being inserted.  Segment times are
#  also provided for each observer position.  A list of frequencies for the octave
#  spectra are given as well.  The SPLs are kept in a 3 dimensional array of size
#  number of results by number of observer nodes by number of frequencies.  A success
#  value is returned communicating the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nNodes
#         This is the number of nodes in the ANOPP2.Data Structure.
#  @param nFreqs
#         This is the number of Frequencies in tone spectra.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTimes
#         These are the segment times of the observer nodes.  These times are recorded
#         by the observer data segment.
#  @param fltFrequencies
#         These are the frequencies of the SPL that is being inserted into the observer
#         data structure.
#  @param fltTones
#         These are the tone spectra.  This is a 3 dimensional array where the first
#         dimension is the number of unique predictions, second dimension is number of
#         observer nodes, and third is the number of tones in the spectra.
#  @param fltPhase
#         These are the phase values of the tones.  The size and shape of this array
#         is the same as the tones array.
#  @param enumNoiseLevelTypes
#         This is an enumeration setting that tells the ANOPP2.API if this
#         is absolute levels or change in levels.  This is of size equal to the number
#         of results.
#  @param blnIncludesFlightEffects
#         This flag communicates whether the input being provided to this routine
#         includes the Doppler frequency shift and convective amplification.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_tones.restype = int
ANOPP2.a2py_obs_insert_tones.argtypes =                                            \
   [c_int, c_int, POINTER                                                          \
     (c_int), c_int, POINTER(c_float), c_int, POINTER(c_float), POINTER(c_float), \
    POINTER(c_float), POINTER(c_int), POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine inserts a list of tone spectra into the ANOPP2.API for a
#  node. A tag is provided that is the observer that is receiving the noise. A list of
#  prediction tags are provided for the results being inserted.  Reception times are
#  also provided for the observer position.  A list of frequencies for the octave
#  spectra are given as well.  The SPLs are kept in a 2 dimensional array of size
#  number of results by number of frequencies.  A success value is returned communicating
#  the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nFreqs
#         This is the number of Frequencies in tone spectra.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTime
#         Thiis is the segment time at which the tones have to be inserted.  This time
#         is recorded by the ANOPP2.API.
#  @param fltFrequencies
#         These are the frequencies of the SPL that is being inserted into the observer
#         data structure.
#  @param fltTones
#         These are the tone spectra.  This is a 2 dimensional array where the
#         first dimension is the number of unique predictions and the second is the
#         number of tones in the spectra.
#  @param fltPhase
#         These are the phase values of the tones.  The size and shape of this array
#         is the same as the tones array.
#  @param intNodeNumber
#         This is the node number for which the octave band spectrum is to be inserted
#  @param enumNoiseLevelTypes
#         This is an enumeration setting that tells the ANOPP2.API if this
#         is absolute levels or change in levels.  This is of size equal to the number
#         of results.
#  @param blnIncludesFlightEffects
#         This flag communicates whether the input being provided to this routine
#         includes the Doppler frequency shift and convective amplification.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_tones_by_node.restype = int
ANOPP2.a2py_obs_insert_tones_by_node.argtypes =                                     \
   [c_int, c_int, POINTER                                                           \
     (c_int), c_float, c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float), \
    c_int, POINTER(c_int), POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine inserts a list of narrow band spectra into the ANOPP2.API.
#  A tag is provided that is the observer that is receiving the noise. A list of
#  prediction tags are provided for the results being inserted.  Segment times are
#  also provided for each observer position.  A list of frequencies for the octave
#  spectra are given as well.  The SPLs are kept in a 3 dimensional array of size
#  number of results by number of observer by number of frequencies.  A success value
#  is returned communicating the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nNodes
#         This is the number of nodes in the ANOPP2.Data Structure.
#  @param nFreqs
#         This is the number of Frequencies in Narrow Band spectra.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTimes
#         These are the segment times of the observers.  These times are recorded by the
#         observer data segment
#  @param fltFrequencies
#         These are the frequencies of the SPL that is being inserted into the observer
#         data structure.
#  @param fltNarrowband
#         These are the narrow band spectra.  This is a 3 dimensional array where
#         the first dimension is the number of unique predictions, second dimension is
#         number of observer points, and third is the number of bins in the spectra.
#  @param fltPhase
#         These are the phase values of the narrow band.  The size and shape of this
#         array is the same as the tones array.
#  @param enumNoiseLevelTypes
#         This is an enumeration setting that tells the ANOPP2.API if this
#         is absolute levels or change in levels.  This is of size equal to the number
#         of results.
#  @param blnIncludesFlightEffects
#         This flag communicates whether the input being provided to this routine
#         includes the Doppler frequency shift and convective amplification.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_narrowband.restype = int
ANOPP2.a2py_obs_insert_narrowband.argtypes =                        \
   [c_int, c_int, POINTER(c_int), c_int, POINTER(c_float), c_int, \
    POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_int), POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine inserts a list of narrow band spectra into the ANOPP2.API
#  for a node. A tag is provided that is the observer that is receiving the noise. A list
#  of prediction tags are provided for the results being inserted.  Reception times are
#  also provided for the observer position.  A list of frequencies for the
#  spectra are given as well.  The SPLs are kept in a 2 dimensional array of size
#  number of results by number of frequencies.  A success value is returned communicating
#  the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nFreqs
#         This is the number of Frequencies in Narrow Band spectra.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTime
#         These is the segment times of the observers.  This time is recorded by the
#         ANOPP2.API.
#  @param fltFrequencies
#         These are the frequencies of the SPL that is being inserted into the observer
#         data structure.
#  @param fltNarrowband
#         These are the narrow band spectra.  This is a 2 dimensional array where the
#         first dimension is the number of unique predictions and the second is the
#         number of bins in the spectra.
#  @param fltPhase
#         These are the phase values of the narrow band.  The size and shape of this
#         array is the same as the tones array.
#  @param intNodeNumber
#         This is the node number for which the narrow band spectrum is to be inserted
#  @param enumNoiseLevelTypes
#         This is an enumeration setting that tells the ANOPP2.API if this
#         is absolute levels or change in levels.  This is of size equal to the number
#         of results.
#  @param blnIncludesFlightEffects
#         This flag communicates whether the input being provided to this routine
#         includes the Doppler frequency shift and convective amplification.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_narrowband_by_node.restype = int
ANOPP2.a2py_obs_insert_narrowband_by_node.argtypes =                 \
   [c_int, c_int, POINTER(c_int), c_float, c_int, POINTER(c_float), \
    POINTER(c_float), POINTER(c_float), c_int, POINTER(c_int), POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine inserts a list of power spectral densities into the observer data
#  structure.  A tag is provided that is the observer that is receiving the noise. A list
#  of prediction tags are provided for the results being inserted.  Segment times are
#  also provided for each observer position.  A list of frequencies for the
#  spectra are given as well.  The SPLs are kept in a 3 dimensional array of size
#  number of results by number of observer by number of frequencies.  A success value
#  is returned communicating the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nNodes
#         This is the number of nodes in the ANOPP2.Data Structure.
#  @param nFreqs
#         This is the number of Frequencies in Power Spectral Densities.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTimes
#         These are the segment times of the observers.  These times are recorded by the
#         observer data segment
#  @param fltFrequencies
#         These are the frequencies of the SPL that is being inserted into the observer
#         data structure.
#  @param fltPowerSpectralDensity
#         These are the power spectral densities.  This is a 3 dimensional array where
#         the first dimension is the number of unique predictions, second dimension is
#         number of observer points, and third is the number of bins in the spectra.
#  @param fltPhase
#         These are the phase values of the power spectrum.  The size and shape of this
#         array is the same as the tones array.
#  @param enumNoiseLevelTypes
#         This is an enumeration setting that tells the ANOPP2.API if this
#         is absolute levels or change in levels.  This is of size equal to the number
#         of results.
#  @param blnIncludesFlightEffects
#         This flag communicates whether the input being provided to this routine
#         includes the Doppler frequency shift and convective amplification.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_psd.restype = int
ANOPP2.a2py_obs_insert_psd.argtypes =                                              \
   [c_int, c_int, POINTER                                                          \
     (c_int), c_int, POINTER(c_float), c_int, POINTER(c_float), POINTER(c_float), \
    POINTER(c_float), POINTER(c_int), POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine inserts a list of power spectral density into the ANOPP2.API
#  for a node. A tag is provided that is the observer that is receiving the noise. A list
#  of prediction tags are provided for the results being inserted.  Reception times are
#  also provided for the observer position.  A list of frequencies for the
#  spectra are given as well.  The SPLs are kept in a 2 dimensional array of size
#  number of results by number of frequencies.  A success value is returned communicating
#  the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nFreqs
#         This is the number of Frequencies in Power Spectral Densities.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTime
#         These is the segment times of the observers.  This time is recorded by the
#         ANOPP2.API.
#  @param fltFrequencies
#         These are the frequencies of the SPL that is being inserted into the observer
#         data structure.
#  @param fltPowerSpectralDensity
#         These are the power spectral density.  This is a 2 dimensional array where the
#         first dimension is the number of unique predictions and the second is the
#         number of bins in the spectra.
#  @param fltPhase
#         These are the phase values of the power spectrum.  The size and shape of this
#         array is the same as the tones array.
#  @param intNodeNumber
#         This is the node number for which the power spectral density is to be inserted
#  @param enumNoiseLevelTypes
#         This is an enumeration setting that tells the ANOPP2.API if this
#         is absolute levels or change in levels.  This is of size equal to the number
#         of results.
#  @param blnIncludesFlightEffects
#         This flag communicates whether the input being provided to this routine
#         includes the Doppler frequency shift and convective amplification.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_psd_by_node.restype = int
ANOPP2.a2py_obs_insert_psd_by_node.argtypes =                                       \
   [c_int, c_int, POINTER                                                           \
     (c_int), c_float, c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float), \
    c_int, POINTER(c_int), POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine inserts a list of octave band spectra into the ANOPP2.API.
#  A tag is provided that is the observer that is receiving the noise.  A list of
#  prediction tags are provided for the results being inserted.  Segment times are
#  also provided for each observer position.  A list of frequencies for the octave
#  spectra are given as well.  The SPLs are kept in a 3 dimensional array of size
#  number of results by number of observer by number of frequencies.  A success value
#  is returned communicating the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nNodes
#         This is the number of nodes in the ANOPP2.Data Structure.
#  @param nFreqs
#         This is the number of Frequencies in Octave Band Spectra.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTimes
#         These are the segment times of the observers.  These times are recorded by the
#         observer data segment
#  @param fltFrequencies
#         These are the frequencies of the SPL that is being inserted into the observer
#         data structure.
#  @param fltSoundPressureLevels
#         These are the sound pressure levels.  This is a 3 dimensional array where the
#         first dimension is the number of unique predictions, second dimension is
#         number of observer points, and third is the number of bands in the SPL.
#  @param fltOctaveNumber
#         This is the octave number.  For example: 3 for 1/3-Octave.
#  @param enumNoiseLevelTypes
#         This is an enumeration setting that tells the ANOPP2.API if this
#         is absolute levels or change in levels.  This is of size equal to the number
#         of results.
#  @param blnIncludesFlightEffects
#         This flag communicates whether the input being provided to this routine
#         includes the Doppler frequency shift and convective amplification.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_octave.restype = int
ANOPP2.a2py_obs_insert_octave.argtypes =                                           \
   [c_int, c_int, POINTER                                                          \
     (c_int), c_int, POINTER(c_float), c_int, POINTER(c_float), POINTER(c_float), \
    c_float, POINTER(c_int), POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine inserts a list of octave band spectra into the ANOPP2.API
#  for a node. A tag is provided that is the observer that is receiving the noise. A list
#  of prediction tags are provided for the results being inserted.  Reception times are
#  also provided for the observer position.  A list of frequencies for the octave
#  spectra are given as well.  The SPLs are kept in a 2 dimensional array of size
#  number of results by number of frequencies.  A success value is returned communicating
#  the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nFreqs
#         This is the number of Frequencies in Octave Band Spectra.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTime
#         These is the segment times of the observers.  This time is recorded by the
#         ANOPP2.API.
#  @param fltFrequencies
#         These are the frequencies of the SPL that is being inserted into the observer
#         data structure.
#  @param fltSoundPressureLevels
#         These are the sound pressure levels.  This is a 2 dimensional array where the
#         first dimension is the number of unique predictions and the second is the
#         number of bands in the SPL.
#  @param intNodeNumber
#         This is the node number for which the octave band spectrum is to be inserted
#  @param fltOctaveNumber
#         This is the octave number.  For example: 3 for 1/3-Octave.
#  @param enumNoiseLevelTypes
#         This is an enumeration setting that tells the ANOPP2.API if this
#         is absolute levels or change in levels.  This is of size equal to the number
#         of results.
#  @param blnIncludesFlightEffects
#         This flag communicates whether the input being provided to this routine
#         includes the Doppler frequency shift and convective amplification.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_octave_by_node.restype = int
ANOPP2.a2py_obs_insert_octave_by_node.argtypes =                                   \
   [c_int, c_int, POINTER                                                          \
     (c_int), c_float, c_int, POINTER(c_float), POINTER(c_float), c_int, c_float, \
    POINTER(c_int), POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine inserts a OASPL and OASPLA value into the ANOPP2.API.
#  A tag is provided that is the observer that is receiving the noise.  A list of
#  prediction tags are provided for the results being inserted. A list of reception times
#  are also provided for each observer position. The OASPL and OASPLa are kept in a 2
#  dimensional array of size number of results by number of observer.  A success value is
#  returned communicating the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nNodes
#         This is the number of nodes in the ANOPP2.Data Structure.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTimes
#         These are the segment times of the observers.  This time is recorded by the
#         observer data segment
#  @param fltOaspl
#         These are the overall sound pressure levels.  This is a 2 dimensional array
#         where the first dimension is the number of unique predictions and the second
#         dimension is number of observer points.
#  @param fltOaspla
#         These are the a-weighted overall sound pressure levels. This is a 2 dimensional
#         array where the first dimension is the number of unique predictions and the
#         second dimension is number of observer points.
#  @param enumNoiseLevelType
#         This is the noise level type of the tonal content spectrum.  This
#         enumeration is set to one of the available options for noise level type.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_oaspl.restype = int
ANOPP2.a2py_obs_insert_oaspl.argtypes =                                       \
   [c_int, c_int, POINTER(c_int), c_int, POINTER(c_float), POINTER(c_float), \
    POINTER(c_float), POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine inserts a OASPL and OASPLa that pertains to a single observer node into
#  ANOPP2.API. A tag is provided that is the observer that is receiving the
#  noise.  A list of prediction tags are provided for the results being inserted.
#  Reception time is also provided for the observer position.  The OASPL and OASPLa are
#  kept in a 1 dimensional array each, the size is the number of results.  A success
#  value is returned communicating the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTime
#         This is the segment times of the observers.  This time is recorded by the
#         observer data segment
#  @param fltFrequencies
#         These are the frequencies of the SPL that is being inserted into the observer
#         data structure.
#  @param fltOaspl
#         These are the overall sound pressure levels.  This is a 1 dimensional array
#         where the size is the number of unique predictions.
#  @param fltOaspla
#         These are the a-weighted overall sound pressure levels. This is a 1 dimensional
#         array where the size is the number of unique predictions.
#  @param intNodeNumber
#         This is the node number for which the acoustic pressure time history
#         has to be inserted.
#  @param enumNoiseLevelType
#         This is the noise level type of the tonal content spectrum.  This
#         enumeration is set to one of the available options for noise level type.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_oaspl_by_node.restype = int
ANOPP2.a2py_obs_insert_oaspl_by_node.argtypes =                                \
   [c_int, c_int, POINTER(c_int), c_float, POINTER(c_float), POINTER(c_float), \
    c_int, POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine inserts a PNL and PNLT value into the ANOPP2.API.
#  A tag is provided that is the observer that is receiving the noise.  A list of
#  prediction tags are provided for the results being inserted. A list of reception times
#  are also provided for each observer position. The PNLs and PNLTs are kept in a 2
#  dimensional array of size number of results by number of observer.  A success value is
#  returned communicating the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nNodes
#         This is the number of nodes in the ANOPP2.Data Structure.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTimes
#         These are the segment times of the observers.  This time is recorded by the
#         observer data segment
#  @param fltPNLs
#         These are the perceived noise levels.  This is a 2 dimensional array where the
#         first dimension is the number of unique predictions and the second dimension
#         is number of observer points.
#  @param fltPNLTs
#         These are the tone-corrected perceived noise levels.  This is a 2 dimensional
#         array where the first dimension is the number of unique predictions and the
#         second dimension is number of observer points.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_pnl.restype = int
ANOPP2.a2py_obs_insert_pnl.argtypes = \
   [c_int, c_int, POINTER             \
     (c_int), c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float)]



# ---------------------------------------------------------------------------------------
#  This routine inserts a PNL and PNLT that pertains to a single observer node into the
#  ANOPP2.API. A tag is provided that is the observer that is receiving the
#  noise.  A list of prediction tags are provided for the results being inserted.
#  Reception time is also provided for the observer position.  The PNLs and PNLTs are
#  kept in a 1 dimensional array each, the size is the number of results.  A success
#  value is returned communicating the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltSegmentTime
#         This is the segment times of the observers.  This time is recorded by the
#         observer data segment
#  @param fltFrequencies
#         These are the frequencies of the SPL that is being inserted into the observer
#         data structure.
#  @param fltPNLs
#         These are the perceived noise levels.  This is a 1 dimensional array where the
#         size is the number of unique predictions.
#  @param fltPNLTs
#         These are the tone-corrected perceived noise levels.  This is a 1 dimensional
#         array where the size is the number of unique predictions.
#  @param intNodeNumber
#         This is the node number for which the acoustic pressure time history
#         has to be inserted.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_pnl_by_node.restype = int
ANOPP2.a2py_obs_insert_pnl_by_node.argtypes = \
   [c_int, c_int, POINTER(c_int), c_float, POINTER(c_float), POINTER(c_float), c_int]



# ---------------------------------------------------------------------------------------
#  This routine inserts an EPNL value into the ANOPP2.API. A tag is provided that is
#  the observer that is receiving the noise.  A list of prediction tags are provided for
#  the results being inserted. The EPNLs are kept in a 2 dimensional array of size number
#  of results by number of observer.  A success value is returned communicating the
#  success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nNodes
#         This is the number of nodes in the ANOPP2.Data Structure.
#  @param fltEPNLs
#         These are the effective perceived noise levels.  This is a 2 dimensional array
#         where the first dimension is the number of unique predictions and the second
#         dimension is number of observer points.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_epnl.restype = int
ANOPP2.a2py_obs_insert_epnl.argtypes = \
   [c_int, c_int, POINTER(c_int), c_int, POINTER(c_float)]



# ---------------------------------------------------------------------------------------
#  This routine inserts an EPNL that pertains to a single observer node into the
#  ANOPP2.API. A tag is provided that is the observer that is receiving the
#  noise.  A list of prediction tags are provided for the results being inserted.
#  The EPNLs are kept in a 1 dimensional array each, the size is the number of results.
#  A success value is returned communicating the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltFrequencies
#         These are the frequencies of the SPL that is being inserted into the observer
#         data structure.
#  @param fltEPNLs
#         These are the effective perceived noise levels.  This is a 1 dimensional array
#         where the size is the number of unique predictions.
#  @param intNodeNumber
#         This is the node number for which the acoustic pressure time history
#         has to be inserted.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_epnl_by_node.restype = int
ANOPP2.a2py_obs_insert_epnl_by_node.argtypes = \
   [c_int, c_int, POINTER(c_int), POINTER(c_float), c_int]



# ---------------------------------------------------------------------------------------
#  This routine inserts an SEL value into the ANOPP2.API. A tag is provided that is
#  the observer that is receiving the noise.  A list of prediction tags are provided for
#  the results being inserted. The SELs are kept in a 2 dimensional array of size number
#  of results by number of observer.  A success value is returned communicating the
#  success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param nNodes
#         This is the number of nodes in the ANOPP2.Data Structure.
#  @param fltSELs
#         These are the sound exposure levels.  This is a 2 dimensional array
#         where the first dimension is the number of unique predictions and the second
#         dimension is number of observer points.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_sel.restype = int
ANOPP2.a2py_obs_insert_sel.argtypes = \
   [c_int, c_int, POINTER(c_int), c_int, POINTER(c_float)]



# ---------------------------------------------------------------------------------------
#  This routine inserts an SEL that pertains to a single observer node into the
#  ANOPP2.API. A tag is provided that is the observer that is receiving the
#  noise.  A list of prediction tags are provided for the results being inserted.
#  The SELs are kept in a 1 dimensional array each, the size is the number of results.
#  A success value is returned communicating the success of this operation.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the observer that is getting the result.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param intResultTags
#         These are the hash numbers that are associated to the prediction results stored
#         in the ANOPP2.API.
#  @param fltFrequencies
#         These are the frequencies of the SPL that is being inserted into the observer
#         data structure.
#  @param fltSELs
#         These are the sound exposure levels.  This is a 1 dimensional array
#         where the size is the number of unique predictions.
#  @param intNodeNumber
#         This is the node number for which the acoustic pressure time history
#         has to be inserted.
#  @result
#         An integer representing success of the insertion
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_insert_sel_by_node.restype = int
ANOPP2.a2py_obs_insert_sel_by_node.argtypes = \
   [c_int, c_int, POINTER(c_int), POINTER(c_float), c_int]



# ---------------------------------------------------------------------------------------
#  This routine returns the name of a given result associated with a tag.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag of the observer in the API.
#  @param intResultTag
#         This is the tag of the result at the observer in the API.
#  @param nChars
#         The length of the result name string.
#  @param strResultName
#         This is the name of the result.
#  @result
#         An integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_get_result_name.restype = int
ANOPP2.a2py_obs_get_result_name.argtypes = [c_int, c_int, c_int, c_char_p]



# ---------------------------------------------------------------------------------------
#  This routine returns the tag of a given result associated with an index.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag of the observer in the API.
#  @param intResultIndex
#         This is the index of the result at the observer in the API.
#  @param intResultTag
#         This is the tag of the result.
#  @result
#         An integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_get_result_tag.restype = int
ANOPP2.a2py_obs_get_result_tag.argtypes = [c_int, c_int, POINTER(c_int)]



# ---------------------------------------------------------------------------------------
# > This routine returns the includes Flight Effects logical array of a given result
# > associated with the input tag.
# ---------------------------------------------------------------------------------------
# > @param intANOPP2.ag
# >        This is the tag of the observer in the API.
# > @param intResultTag
# >        This is the tag of the result at the observer in the API.
# > @param blnIncludesFlightEffects
# >        This is the size 2 boolean array that indicates whether the result includes
# >        Flight Effects, with the first index being Doppler shift, and the second
# >        index being convective amplification.
# > @result
# >        An integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_get_includes_flight_effects.restype = int
ANOPP2.a2py_obs_get_includes_flight_effects.argtypes = [c_int, c_int, POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
# > This routine returns the noise level type enumerator of a given result associated
# > with the input tag.
# ---------------------------------------------------------------------------------------
# > @param intANOPP2.ag
# >        This is the tag of the observer in the API.
# > @param intResultTag
# >        This is the tag of the result at the observer in the API.
# > @param enumNoiseLevelType
# >        This is the enumerator of the noise level type.
# > @result
# >        An integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_get_noise_level_type.restype = int
ANOPP2.a2py_obs_get_noise_level_type.argtypes = [c_int, c_int, POINTER(c_int)]



# ---------------------------------------------------------------------------------------
#  This function returns an array of segment times for a given node and result.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag of the observer being accessed.
#  @param intResultTag
#         This ist he tag o the result being accessed.
#  @param iNode
#         This is the node number being accessed.
#  @param nSegmentTimes
#         This is the number of segment times that are in the fltSegmentTime array.
#  @param fltSegmentTime
#         This is a pointer to an array of segment times.
#  @result
#         An integer representing success of this operation
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_get_segment_time.restype = int
ANOPP2.a2py_obs_get_segment_time.argtypes = \
   [c_int, c_int, c_int, POINTER(c_int), POINTER(POINTER(c_float))]



# ---------------------------------------------------------------------------------------
#  This routine returns the acoustic pressure time history at a particular index in time
#  for an observer result.  Pointers are returned that are associated to the time
#  and pressure values.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag of the observer that is being accessed.
#  @param intResultTag
#         This is the tag for the result desired by the user.
#  @param iNode
#         This is the node index of the metric being returned.
#  @param iTime
#         This is the index in time desired by the user.  If the complete time history
#         is desired, this is set to 0.
#  @param nReceptionTimes
#         This is the size of the time and pressure arrays that are returned.
#  @param fltTime
#         This is a pointer to the time of the acoustic pressure time history.
#  @param fltAcousticPressure
#         This is a pointer to pressure values in the ANOPP2.API
#  @param enumNoiseLevelType
#         This is the noise level type of the acoustic pressure time history.  This
#         enumeration is set to one of the available options for noise level type.
#  @param blnIncludesFlightEffects
#         These flags communicate the flight effects of the spectrum.  The first is
#         for including Doppler frequency shift and the second is for convective
#         amplification.
#  @result
#         An integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_get_pressure.restype = int
ANOPP2.a2py_obs_get_pressure.argtypes =                                             \
   [c_int, c_int, c_int, c_int, POINTER                                           \
     (c_int), POINTER(POINTER(c_float)), POINTER(POINTER(c_float)), POINTER(c_int), \
    POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine returns the pressure sensitivity time history at a particular index in
#  time for an observer result.  Pointers are returned that are associated to the time
#  and pressure values.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag of the observer that is being accessed.
#  @param intResultTag
#         This is the tag for the result desired by the user.
#  @param iNode
#         This is the node index of the metric being returned.
#  @param iTime
#         This is the index in time desired by the user.  If the complete time history
#         is desired, this is set to 0.
#  @param nReceptionTimes
#         This is the size of the time and pressure arrays that are returned.
#  @param fltTime
#         This is a pointer to the time of the acoustic pressure time history.
#  @param fltPressureSensitivity
#         This is a pointer to pressure sensitivity values in the ANOPP2.API
#  @param intSensitivityDimensions
#         This is a pointer to an array of integers that are the dimensions of the
#         sensitivity matrix.
#  @param enumNoiseLevelType
#         This is the noise level type of the acoustic pressure time history.  This
#         enumeration is set to one of the available options for noise level type.
#  @param blnIncludesFlightEffects
#         These flags communicate the flight effects of the spectrum.  The first is
#         for including Doppler frequency shift and the second is for convective
#         amplification.
#  @result
#         An integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_get_pressure_sensitivity.restype = int
ANOPP2.a2py_obs_get_pressure_sensitivity.argtypes =                                 \
   [c_int, c_int, c_int, c_int, POINTER                                           \
     (c_int), POINTER(POINTER(c_float)), POINTER(POINTER(c_float)), POINTER(c_int), \
    POINTER(c_int), POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine returns the acoustic veocity time history at a particular index in time
#  for an observer result.  Pointers are returned that are associated to the time
#  and acoustic velocity values.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag of the observer that is being accessed.
#  @param intResultTag
#         This is the tag for the result desired by the user.
#  @param iNode
#         This is the node index of the metric being returned.
#  @param iTime
#         This is the index in time desired by the user.  If the complete time history
#         is desired, this is set to 0.
#  @param nReceptionTimes
#         This is the size of the time and velocity arrays that are returned.
#  @param fltTime
#         This is a pointer to the time of the acoustic velocity time history.
#  @param fltAcousticVelocity
#         This is a pointer to acoustic velocity values in the observer API.
#         The first dimension is returned as nReceptionTimes and the second is 3 for a
#         vector quantity.
#  @param enumNoiseLevelType
#         This is the noise level type of the acoustic pressure time history.  This
#         enumeration is set to one of the available options for noise level type.
#  @param blnIncludesFlightEffects
#         These flags communicate the flight effects of the spectrum.  The first is
#         for including Doppler frequency shift and the second is for convective
#         amplification.
#  @result
#         An integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_get_velocity.restype = int
ANOPP2.a2py_obs_get_velocity.argtypes =                                             \
   [c_int, c_int, c_int, c_int, POINTER                                           \
     (c_int), POINTER(POINTER(c_float)), POINTER(POINTER(c_float)), POINTER(c_int), \
    POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine returns the pressure gradient time history at a particular index in time
#  for an observer result.  Pointers are returned that are associated to the time
#  and pressure gradient values.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag of the observer that is being accessed.
#  @param intResultTag
#         This is the tag for the result desired by the user.
#  @param iNode
#         This is the node index of the metric being returned.
#  @param iTime
#         This is the index in time desired by the user.  If the complete time history
#         is desired, this is set to 0.
#  @param nReceptionTimes
#         This is the size of the time and velocity arrays that are returned.
#  @param fltTime
#         This is a pointer to the time of the pressure gradient time history.
#  @param fltPressureGradient
#         This is a pointer to pressure gradient values in the ANOPP2.API
#         The first dimension is returned as nReceptionTimes and the second is 3 for a
#         vector quantity.
#  @param enumNoiseLevelType
#         This is the noise level type of the acoustic pressure time history.  This
#         enumeration is set to one of the available options for noise level type.
#  @param blnIncludesFlightEffects
#         These flags communicate the flight effects of the spectrum.  The first is
#         for including Doppler frequency shift and the second is for convective
#         amplification.
#  @result
#         An integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_get_gradient.restype = int
ANOPP2.a2py_obs_get_gradient.argtypes =                                             \
   [c_int, c_int, c_int, c_int, POINTER                                           \
     (c_int), POINTER(POINTER(c_float)), POINTER(POINTER(c_float)), POINTER(c_int), \
    POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
#  This routine returns the tonal content spectrum at a particular index in time
#  for an observer result.  Pointers are returned that are associated to the frequency
#  and spectrum values.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag of the observer that is being accessed.
#  @param intResultTag
#         This is the tag for the result desired by the user.
#  @param iNode
#         This is the node index of the metric being returned.
#  @param iTime
#         This is the index in time desired by the user.
#  @param nFrequencies
#         This is the size of the frequencies and spectrum arrays.
#  @param fltFrequencies
#         This is a pointer to the frequencies of the tonal content spectrum
#         level.
#  @param cpxSpectrum
#         This is a pointer to tonal content spectrum in the ANOPP2.API
#  @param blnIncludesFlightEffects
#         These flags communicate the flight effects of the spectrum.  The first is
#         for including Doppler frequency shift and the second is for convective
#         amplification.
#  @param enumNoiseLevelType
#         This is the noise level type of the tonal content spectrum.  This
#         enumeration is set to one of the available options for noise level type.
#  @result
#         An integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_get_tones.restype = int
ANOPP2.a2py_obs_get_tones.argtypes =                                     \
   [c_int, c_int, c_int, c_int, POINTER                                \
     (c_int), POINTER(POINTER(c_float)), POINTER(POINTER((2 * c_float))), \
    POINTER(c_bool), POINTER(c_int)]



# ---------------------------------------------------------------------------------------
#  This routine returns the narrow band spectrum at a particular index in time
#  for an observer result.  Pointers are returned that are associated to the frequency
#  and spectrum values.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag of the observer that is being accessed.
#  @param intResultTag
#         This is the tag for the result desired by the user.
#  @param iNode
#         This is the node index of the metric being returned.
#  @param iTime
#         This is the index in time desired by the user.
#  @param nFrequencies
#         This is the size of the frequencies and spectrum arrays.
#  @param fltFrequencies
#         This is a pointer to the bin frequencies of the narrow band spectrum
#         level.
#  @param cpxSpectrum
#         This is a pointer to narrow band spectrum in the ANOPP2.API
#  @param blnIncludesFlightEffects
#         These flags communicate the flight effects of the spectrum.  The first is
#         for including Doppler frequency shift and the second is for convective
#         amplification.
#  @param enumNoiseLevelType
#         This is the noise level type of the narrow band spectrum.  This
#         enumeration is set to one of the available options for noise level type.
#  @result
#         An integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_get_narrowband.restype = int
ANOPP2.a2py_obs_get_narrowband.argtypes =                                \
   [c_int, c_int, c_int, c_int, POINTER                                \
     (c_int), POINTER(POINTER(c_float)), POINTER(POINTER((2 * c_float))), \
    POINTER(c_bool), POINTER(c_int)]



# ---------------------------------------------------------------------------------------
#  This routine returns the power spectral density at a particular index in time
#  for an observer result.  Pointers are returned that are associated to the frequency
#  and spectrum values.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag of the observer that is being accessed.
#  @param intResultTag
#         This is the tag for the result desired by the user.
#  @param iNode
#         This is the node index of the metric being returned.
#  @param iTime
#         This is the index in time desired by the user.
#  @param nFrequencies
#         This is the size of the frequencies and spectrum arrays.
#  @param fltFrequencies
#         This is a pointer to the bin frequencies of the power spectral density
#         level.
#  @param cpxSpectrum
#         This is a pointer to power spectral density in the ANOPP2.API
#  @param blnIncludesFlightEffects
#         These flags communicate the flight effects of the spectrum.  The first is
#         for including Doppler frequency shift and the second is for convective
#         amplification.
#  @param enumNoiseLevelType
#         This is the noise level type of the power spectral density.  This
#         enumeration is set to one of the available options for noise level type.
#  @result
#         An integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_get_psd.restype = int
ANOPP2.a2py_obs_get_psd.argtypes =                                       \
   [c_int, c_int, c_int, c_int, POINTER                                \
     (c_int), POINTER(POINTER(c_float)), POINTER(POINTER((2 * c_float))), \
    POINTER(c_bool), POINTER(c_int)]



# ---------------------------------------------------------------------------------------
#  This routine returns the octave sound pressure level at a particular index in time
#  for an observer result.  Pointers are returned that are associated to the frequency
#  and sound pressure levels.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag of the observer that is being accessed.
#  @param intResultTag
#         This is the tag for the result desired by the user.
#  @param iNode
#         This is the node index of the metric being returned.
#  @param iTime
#         This is the index in time desired by the user.
#  @param nFrequencies
#         This is the size of the frequencies and spectrum arrays.
#  @param fltFrequencies
#         This is a pointer to the center band frequencies of the octave sound pressure
#         level.
#  @param fltSoundPressureLevels
#         This is a pointer to sound pressure levels in the ANOPP2.API
#  @param fltOctaveNumber
#         This is the octave number of the octave sound pressure level.
#  @param blnIncludesFlightEffects
#         These flags communicate the flight effects of the spectrum.  The first is
#         for including Doppler frequency shift and the second is for convective
#         amplification.
#  @param enumNoiseLevelType
#         This is the noise level type of the octave sound pressure level.  This
#         enumeration is set to one of the available options for noise level type.
#  @result
#         An integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_get_octave.restype = int
ANOPP2.a2py_obs_get_octave.argtypes =                                                \
   [c_int, c_int, c_int, c_int, POINTER                                            \
     (c_int), POINTER(POINTER(c_float)), POINTER(POINTER(c_float)), POINTER(c_float), \
    POINTER(c_bool), POINTER(c_int)]



# ---------------------------------------------------------------------------------------
#  This routine returns the overall sound pressure level at a particular index in time
#  for an observer result.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag of the observer that is being accessed.
#  @param intResultTag
#         This is the tag for the result desired by the user.
#  @param iNode
#         This is the node index of the metric being returned.
#  @param iTime
#         This is the index in time desired by the user.
#  @param fltOaspl
#         This is the value of the overall sound pressure level.
#  @param fltOaspla
#         This is the value of the a-weighted overall sound pressure level.
#  @result
#         An integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_get_oaspl.restype = int
ANOPP2.a2py_obs_get_oaspl.argtypes = \
   [c_int, c_int, c_int, c_int, POINTER(c_float), POINTER(c_float)]



# ---------------------------------------------------------------------------------------
#  This routine returns the perceived noise level at a particular index in time
#  for an observer result.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag of the observer that is being accessed.
#  @param intResultTag
#         This is the tag for the result desired by the user.
#  @param iNode
#         This is the node index of the metric being returned.
#  @param iTime
#         This is the index in time desired by the user.
#  @param fltPnl
#         This is the value of the perceived noise level.
#  @param fltPnlt
#         This is the value of the tone-corrected perceived noise level.
#  @param fltBandFrequency
#         This is the 1/3rd-Octave SPL center band frequency that accrues the tone penalty
#  @param fltToneCorrection
#         This is the value of the tone correction penalty
#  @result
#         An integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_get_pnl.restype = int
ANOPP2.a2py_obs_get_pnl.argtypes =        \
   [c_int, c_int, c_int, c_int, POINTER \
     (c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float)]



# ---------------------------------------------------------------------------------------
#  This routine returns the sound exposure level at a particular node index.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag of the observer that is being accessed.
#  @param intResultTag
#         This is the tag for the result desired by the user.
#  @param iNode
#         This is the node index of the metric being returned.
#  @param fltSel
#         This is the value of the sound exposure level.
#  @param fltD
#         This is the duration factor determined when calculating SEL.
#  @param fltTimeRange
#         This is the minimum and maximum time of the SEL integration.
#  @result
#         An integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_get_sel.restype = int
ANOPP2.a2py_obs_get_sel.argtypes = \
   [c_int, c_int, c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float)]



# ---------------------------------------------------------------------------------------
#  This routine returns the effective perceived noise level at a particular node index.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag of the observer that is being accessed.
#  @param intResultTag
#         This is the tag for the result desired by the user.
#  @param iNode
#         This is the node index of the metric being returned.
#  @param fltEpnl
#         This is the value of the effective percieved noise level.
#  @param fltD
#         This is the duration factor determined when calculating EPNL.
#  @param fltTimeRange
#         This is the minimum and maximum time of the EPNL integration.
#  @result
#         An integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_get_epnl.restype = int
ANOPP2.a2py_obs_get_epnl.argtypes = \
   [c_int, c_int, c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float)]



# ---------------------------------------------------------------------------------------
#  This function adds two observer predictions together.  The inputs into this function
#  are a tag for the observer to be modified, a list of tags to be added together,
#  and the name of the result.  The output of this funciton a tag of the result in the
#  ANOPP2.API.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated to the observer that is being modified.
#  @param nInputs
#         This is the number of Predictions whose results have to be added.
#  @param intInputTags
#         This is a list of tags that are associated to predictions that will be
#         combined.
#  @param enumMetric
#         This is the metric in the input that will be added and made available in the
#         the result observer associated by the result tag.
#  @param strResultName
#         This is the name of the result of this function
#  @param intResultTag
#         This is a tag returned by the ANOPP2.API that is used to associate
#         to the combination of the inputs.
#  @result
#         An integer representing success of the addition.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_add.restype = int
ANOPP2.a2py_obs_add.argtypes = \
   [c_int, c_int, POINTER(c_int), c_int, c_char_p, POINTER(c_int)]



# ----------------------------------------------------------------------------------------
#  This routine copies a result in the ANOPP2.API associated with an observer tag.  The
#  calling program must specify an observer tag and a result tag to which is associated
#  the results that are going to be copied.  This routine retuns a new result tag that
#  can be used to access the copied results.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag associated with the ANOPP2.Data Structure within the
#         ANOPP2.API.  It contains the result to be copied and will contain the new
#         result once it is copied from the existing result.
#  @param intExistingResultTag
#         This is a tag associated with the result within the ANOPP2.Data Structure.
#  @param enumMetric
#         If this input is specified as non-zero, it will copy ONLY this metric in the
#         observer data structure.  All other noise metrics from the existing result will
#         not exist in the new result.  If all metrics are to be copied over, set this to
#         zero.  These metrics are defined in the Acoustic Analysis API.
#  @param intNewResultTag
#         This is a tag that will be set by this routine once a result has been created
#         from a copy of the old result.
#  @param strResultName
#         This is a string representing the name of the result created by copying an
#         existing result.
#  @result
#         An integer representing success of this operation.
# ----------------------------------------------------------------------------------------
ANOPP2.a2py_obs_copy_result.restype = int
ANOPP2.a2py_obs_copy_result.argtypes = \
   [c_int, c_int, c_int, c_char_p, POINTER(c_int)]



# ----------------------------------------------------------------------------------------
#  This routine calculates a noise metric in an ANOPP2.API.  The metric
#  that is calculated is communicated by the enumeration of the metric the user would
#  like to calculate.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is a tag that is used to associated to the observer being modified.
#  @param nResults
#         This is the number of results in the ANOPP2.Data Structure.
#  @param intResultTags
#         These are the tags associated to the results being modified.  This is an array
#         of result tags, one for each result.
#  @param enumMetric
#         This is the enumerator of the metric that the user would like to calculate.
#  @param enumTimeHistoryGroup
#         This is a setting of whether the acoustic pressure will be segmented or
#         analyzed as a whole.  Options are either segment or complete.
#  @result
#         This is an integer that is used to communicate success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_calc_metric.restype = int
ANOPP2.a2py_obs_calc_metric.argtypes = [c_int, c_int, POINTER(c_int), c_int, c_int]




# ---------------------------------------------------------------------------------------
#  This function filters noise metrics within an observer result.  The filter function
#  is a simple top hat filter where anything lower than a certain frequency is removed
#  and anything above a higher frequency is removed.  These frequencies are provided
#  in the filter frequencies array.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         This is the tag that is associated to the ANOPP2.Data Structure within the
#         ANOPP2.API.
#  @param intResultTag
#         This is the tag associated to the result that is to be filterd.
#  @param fltFilterFrequencies
#         This is an array of dimension 2 that includes the high pass and low pass
#         filter frequencies.
#  @result
#         This is an integer that is used to communicate success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_filter_result.restype = int
ANOPP2.a2py_obs_filter_result.argtypes = [c_int, c_int, POINTER(c_float)]



# ---------------------------------------------------------------------------------------
# > This routine sets the includes Flight Effects logical array of a given result
# > associated with the input tag.
# ---------------------------------------------------------------------------------------
# > @param intANOPP2.ag
# >        This is the tag of the observer in the API.
# > @param intResultTag
# >        This is the tag of the result at the observer in the API.
# > @param blnIncludesFlightEffects
# >        This is the size 2 boolean array that indicates whether the result includes
# >        Flight Effects, with the first index being Doppler shift, and the second
# >        index being convective amplification.
# > @result
# >        An integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_set_includes_flight_effects.restype = int
ANOPP2.a2py_obs_set_includes_flight_effects.argtypes = [c_int, c_int, POINTER(c_bool)]



# ---------------------------------------------------------------------------------------
# > This routine sets the noise level type enumerator of a given result associated
# > with the input tag.
# ---------------------------------------------------------------------------------------
# > @param intANOPP2.ag
# >        This is the tag of the observer in the API.
# > @param intResultTag
# >        This is the tag of the result at the observer in the API.
# > @param enumNoiseLevelType
# >        This is the enumerator of the noise level type.
# > @result
# >        An integer representing success of this operation.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_set_noise_level_type.restype = int
ANOPP2.a2py_obs_set_noise_level_type.argtypes = [c_int, c_int, POINTER(c_int)]



# ---------------------------------------------------------------------------------------
#  This function access an observer and tells it to export the noise.  The function
#  takes in an observer tag and a metric tag and commands the observer to write out
#  a given result to a file.  The file can be of a specified format and for a given
#  program.
# ---------------------------------------------------------------------------------------
#  @param intANOPP2.ag
#         The tag that connets the working code to the ANOPP2 API.
#  @param intResultTag
#         This tag communicates what result is desired in the output file.
#  @param strFileName
#         This is the file file name that the Export will go in.
#  @param enumMetric
#         A tag that communicates to the observer what metric to calculate and Export on.
#         These are defined in the Acoustic Analysis API.
#  @param enumFrameOfReference
#         This is an enumeration for the frame of reference of the output geometry.
#         This can be in either local or global frame of reference.
#  @param enumFormat
#         This is the format of the file: options may include formatted or binary.
#  @param enumProgram
#         This is the program that will eventually read the file.  This may include
#         Tecplot or NetCDF.
#  @result
#         An integer that is 0 if everything has occurred as expected.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_obs_export.restype = int
ANOPP2.a2py_obs_export.argtypes = \
   [c_int, c_int, c_char_p, c_int, c_int, c_int, c_int]

#!/usr/bin/python
# =========================================================================================
#  Next part of this interface file contains hardcoded enumerators used by the user's
#  program.
# =========================================================================================



# -----------------------------------------------------------------------------------------
#  This enum is a list of potential observers that can be loaded from the catalog.  The
#  first is actually a 'does not exist' enumeration which tells the system to use a
#  restart file.  The other's do not require a restart file.
# -----------------------------------------------------------------------------------------

#  This enumerator is for an undefined observer (not in the catalog)
a2_obs_undefined = 1

#  This enumeration if for an observer that is at 0.0,0.0,0.0 (the origin).
a2_obs_origin = 2

#  Use this enumerator to receive an observer that is a polar arc.
a2_obs_polar_arc = 3

#  This enumeration if for a surface of observer micriphone locations in the shape of a
#  hemisphere. 
a2_obs_hemisphere = 4

#  This is an empty point cloud. It contains no nodes and the a2f_obs_new_node function can
#  be used to insert nodes.
a2_obs_empty_point_cloud = 5



# -----------------------------------------------------------------------------------------
#  This enumeration is for the pressure time history. The pressure time history can be
#  cast on a segment or on the entire time range.
# -----------------------------------------------------------------------------------------

#  This is the enumeration for casting the pressure time history on a segment
a2_obs_segment = 1

#  This is the enumeration for casting the pressure time history on the entire time range
a2_obs_complete = 2



# -----------------------------------------------------------------------------------------
#  This enumerator group are the different types of observer within the ANOPP2.API.
#  This includes point, line, surface, point cloud, and sphere.
# -----------------------------------------------------------------------------------------

#  This is the enumerator for an observer point
a2_obs_point = 1

#  This is the enumerator for an observer line
a2_obs_line = 2

#  This is the enumerator for an observer surface
a2_obs_surface = 3

#  This is the enumerator for an observer volume
a2_obs_volume = 4

#  This is the enumerator for an observer sphere
a2_obs_sphere = 5

#  This is the enumerator for an observer point cloud
a2_obs_point_cloud = 6



#!/usr/bin/python
# -----------------------------------------------------------------------------------------
# This file is the ANOPP2.API interface file. It contains definitions for all the
# routines available in the ANOPP2.API.
# Please see the API manual provided with ANOPP2.
# -----------------------------------------------------------------------------------------
# @file ANOPP2.api.f90
# @author The ANOPP2 Development Team
# @version 1.0.0
# -----------------------------------------------------------------------------------------



# =========================================================================================
# First part of this section contains interfaces into the available ANOPP2.API
# routines.
# =========================================================================================



# -----------------------------------------------------------------------------------------
# This subroutine initializes the ANOPP2.API by setting internal variables and
# function parameters that must exist before any other call to the API can be made.
# This routine should be the first call in all programs.
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------
# This routine executes the unit tests defined for the ANOPP2.api.
# -----------------------------------------------------------------------------------------
# @result
#        An integer that contains the number of failed asserts during unit testing.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_ps_unit_test.restype = bool




# -----------------------------------------------------------------------------------------
# This routine creates a propulsion data structure in the ANOPP2.API.  A tag is
# returned which is used by the calling program to access that data structure.  The
# input into this routine is the name of a settings file.  The settings file must
# contain one of the known types of propulsion systems.  See Documentation for more
# information on the format of the settings file.
# -----------------------------------------------------------------------------------------
# @param intTag
#        This is the tag that will be returned to the user after the object has
#        been created.
# @param strConfigurationFile
#        This is a file that contains the inputs required for the object to be
#        created. This is typically a namelist file.
# @result
#        An integer that is returned 0 when everything occurred correctly.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_ps_create.restype = int
ANOPP2.a2py_ps_create.argtypes = [POINTER(c_int), c_char_p]



# ---------------------------------------------------------------------------------------
#  This function takes in a tag representing a propulsion and returns true if it exists
#  in the API and false if it does not.
# ---------------------------------------------------------------------------------------
#  @param intTag
#         This is the tag associated to the propulsion that is being searched for.
#  @result
#         A bool that is returned true if the propulsion exists and false if it does not.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_ps_exists.restype = bool
ANOPP2.a2py_ps_exists.argtypes = [c_int]



# -----------------------------------------------------------------------------------------
# This function returns the characterstics of the propulsions system
# -----------------------------------------------------------------------------------------
# @param intTag
#        The tag that identifies ANOPP2.System.
# @param fltReferenceArea
#        The (fan) reference area used to non-dimensinoalize the data
# @param fltScaleFactor
#        The engine scale factor (area base) used to estimate effect of engine sizing
#        on noise. This input typically is determined via an airplane sizing analysis
#        (e.g., Flops). It is used to make crude corrections to area-based parmeterters
#        (e.g. , massflow, thrust, areas, etc. ).
# @result
#        An integer that is 0 if everything has occurred as expected.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_ps_get_characteristics.restype = int
ANOPP2.a2py_ps_get_characteristics.argtypes = \
  [c_int, POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This function returns the requested engine performance properties at a particular
# state
# -----------------------------------------------------------------------------------------
# @param intTag
#        The tag that identifies ANOPP2.System.
# @param fltAltitude
#        The altitude at which the data represents
# @param fltMachNumber
#        The Mach number at which the data represents
# @param fltThrottle
#        The throttle in percent at which the data represents
# @param nParameters
#        This is the size of the enumerator and float parameters array.
# @param enumParameters
#        An array holding the requested performance data to be returned. Please see the
# @param fltParameters
#        An array of the requested engine performance properties at the identified
#        state.
# @result
#        An integer that is 0 if everything has occurred as expected.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_ps_get_state.restype = int
ANOPP2.a2py_ps_get_state.argtypes = \
  [c_int, c_float, c_float, c_float, c_int, POINTER(c_int), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This function returns the requested geometry properties.
# -----------------------------------------------------------------------------------------
# @param intTag
#        The tag that identifies ANOPP2.System.
# @param nParameters
#        This is the size of the enumerator and float parameters array.
# @param enumParameters
#        An array holding the requested geometry data to be returned. Please see the
# @param fltParameters
#        An array of the requested geometry data.
# @result
#        An integer that is 0 if everything has occurred as expected.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_ps_get_geometry.restype = int
ANOPP2.a2py_ps_get_geometry.argtypes = \
  [c_int, c_int, POINTER(c_int), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This function sets the geometric properties of the propulsion system to the given
# values.  A list of enumerators are specified with a list of values.  The Propulsion
# System API takes those values and assigns them to the ANOPP2.System associated
# with the provided tag.
# -----------------------------------------------------------------------------------------
# @param intTag
#        The tag that identifies ANOPP2.System.
# @param nParameters
#        This is the size of the enumerator and float parameters array.
# @param enumParameters
#        An array holding the requested geometry data to be returned. Please see the
# @param fltParameters
#        An array of the requested geometry data.
# @result
#        An integer that is 0 if everything has occurred as expected.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_ps_set_geometry.restype = int
ANOPP2.a2py_ps_set_geometry.argtypes = \
  [c_int, c_int, POINTER(c_int), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This function exports all the properties in a propulsion system to an output file.
# -----------------------------------------------------------------------------------------
# @param intTag
#        The tag that identifies ANOPP2.System.
# @param strStateFile
#        This is the export file name to contain the state information.
# @param strGeometryFile
#        This is the name of the file that will contain the geometric information.
# @param enumFormat
#        This is the format of the file: options may include formatted or binary.
# @param enumProgram
#        This is the program that will eventually read the file.  This may include
#        Tecplot or NetCDF.
# @result
#        An integer that is 0 if everything has occurred as expected.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_ps_export.restype = int
ANOPP2.a2py_ps_export.argtypes = [c_int, c_char_p, c_char_p, c_int, c_int]



#!/usr/bin/python
# =========================================================================================
#   Next part of this section of the interface file contains hardcoded enumerators used by
#   the user's program to communicate parameters and settings to the API.
# =========================================================================================
# =========================================================================================



# -----------------------------------------------------------------------------------------
#  These enumerations determine what type of geometric quantities are stored in the
#  ANOPP2.API.  The enumerations are listed out here and grouped by component.  The
#  components include Fan, Turbine, Core, and Jet.
# -----------------------------------------------------------------------------------------

# This is the fan face reference area
a2_ps_fan_fra = 1

# This is the fan hub diameter.
a2_ps_fan_hd = 2

# This is the fan outer diameter.
a2_ps_fan_od = 3

# This is the fan diameter ratio (Hub/Outer).
a2_ps_fan_dr = 4

# This is the fan flow area.
a2_ps_fan_fa = 5

# This is the fan design tangential tip Mach number.
a2_ps_fan_dttmn = 6

# This is the fan design helical tip Mach number.
a2_ps_fan_dhtmn = 7

# This is the fan face design Mach number.
a2_ps_fan_fdmn = 8

# This is the number of fan rotor blades.
a2_ps_fan_nb = 9

# This is the number of fan exit guide vanes.
a2_ps_fan_nv = 10

# This is the fan rotor-stator spacing in meters.
a2_ps_fan_rss = 11

# This is the ratio of the fan rotor-stator spacing to the fan
a2_ps_fan_rssr = 12

# This is the average fan blade axial length.
a2_ps_fan_abal = 13

# This is the average fan blade chord length
a2_ps_fan_abcl = 14

# This is the tip fan blade axial length.
a2_ps_fan_tbal = 15

# This is the tip fan blade chord length
a2_ps_fan_tbcl = 16

# This is the fan blade projected axial chord length
a2_ps_fan_bpacl = 17

# This is the fan blade aspect ratio
a2_ps_fan_bar = 18

# This is the design rotor rate.
a2_ps_fan_drr = 19

# This is the axial length of the inlet.
a2_ps_fan_ial = 20

# This is the axial length of the inlet treated area.
a2_ps_fan_ital = 21

# This is the axial length of the aft treated area.
a2_ps_fan_atal = 22

# This is the average inlet radius of treated region.
a2_ps_fan_aitr = 23

# This is the average duct height of aft treated region.
a2_ps_fan_atadh = 24

# This is the primary nozzle plug diameter at the throat.
a2_ps_prim_ptd = 25

# This is the primary nozzle outer diameter at throat.
a2_ps_prim_otd = 26

# This is the plug diameter at the exit.
a2_ps_prim_ped = 27

# This is the primary nozzle outer diameter at exit.
a2_ps_prim_oet = 28

# This is the distance from the core nozzle exit to the tip.
a2_ps_prim_ett = 29

# This is the ratio of the wetted perimeter with chevrons to without.
a2_ps_prim_wpr = 30

# This is the radius of curvative of the plug tip.
a2_ps_prim_ptrc = 31

# This is the height of the jet (if rectangular).
a2_ps_prim_h = 32

# This is the width of the jet (if rectangular).
a2_ps_prim_w = 33

# This is the fan nozzle inner diameter at the throat.
a2_ps_sec_itd = 34

# This is the fan nozzle outer diameter at the throat.
a2_ps_sec_otd = 35

# This is the fan nozzle inner diameter at the exit.
a2_ps_sec_ied = 36

# This is the fan nozzle outer diameter at the exit.
a2_ps_sec_oed = 37

# This is the distance from the secondary exit to the primary exit.
a2_ps_sec_dtp = 38

# This is the ratio of the wetted perimeter with chevrons to without.
a2_ps_sec_wpr = 39

# This is the combustor inlet inner radius
a2_ps_comb_iir = 40

# This is the combustor inlet outer radius
a2_ps_comb_ior = 41

# This is the combustor inlet area
a2_ps_comb_ia = 42

# This is the combustor exit area.
a2_ps_comb_ea = 43

# This is the speed of sound based on the tailpipe mean static temperature.
a2_ps_comb_tsos = 44

# This is the diameter of the tailpipe.
a2_ps_comb_td = 45

# This is the LPT stage count.
a2_ps_turb_sc = 46

# This is the number of turbine rotor blades.
a2_ps_turb_nb = 47

# This is the turbine rotor spacing.
a2_ps_turb_rs = 48

# This is the turbine rotor diameter
a2_ps_turb_rd = 49

# This is the turbine final stage tip diameter.
a2_ps_turb_fstp = 50

# This is the turbine final stage hub diameter
a2_ps_turb_fshd = 51

# This is the turbine exit area.
a2_ps_turb_ea = 52

# ---------------------------------------------------------------------------------------
#  These enumerators list out the supported state properties that may be available
#  within the ANOPP2.API.  Not all state properties are supported by all propulsion
#  systems.  For instance, a ANOPP2.System Data Structure created with ANOPP Engine
#  State Table will not have as many state variables as a Data Structure created with
#  an NPSS data set.  See manual for complete list.
# ---------------------------------------------------------------------------------------

# This is the gross thrust of the engine.
a2_ps_gt = 1

# This is the ram drag of the engine.
a2_ps_rd = 2

# This is the net thrust of the engine.
a2_ps_nt = 3

# This is the max net thrust of the engine.
a2_ps_mnt = 4

# This is the power code of the engine.
a2_ps_pc = 5

# This is the fuel mass flow rate
a2_ps_fmfr = 6

# This is the fan bypass ratio.
a2_ps_br = 7

# The ambient pressure.
a2_ps_amb_p = 8

# The ambient temperature.
a2_ps_amb_t = 9

# The ambient specific heat ratio
a2_ps_amb_shr = 10

# The ambient density.
a2_ps_amb_d = 11

# The ambient speed of sound.
a2_ps_amb_sos = 12

# Fan mass flow rate.
a2_ps_fan_mfr = 13

# This is the shaft speed of the fan
a2_ps_fan_ss = 14

# This is the maximum shaft speed of the fan.
a2_ps_fan_mss = 15

# This is the shaft speed fraction.
a2_ps_fan_ssf = 16

# This is the fan tip speed.
a2_ps_fan_ts = 17

# This is the fan inlet total temperature.
a2_ps_fan_itt = 18

# This is the fan exit total temperature.
a2_ps_fan_ett = 19

# This is the fan pressure ratio.
a2_ps_fan_pr = 20

# This is the fan adiabatic efficiency.
a2_ps_fan_ae = 21

# Primary nozzle total temperature
a2_ps_prim_tt = 22

# Primary nozzle total pressure
a2_ps_prim_tp = 23

# Primary nozzle pressure ratio
a2_ps_prim_pr = 24

# Primary nozzle exit ideal velocity
a2_ps_prim_iv = 25

# Primary nozzle exit area
a2_ps_prim_ea = 26

# Primary nozzle mass flow rate
a2_ps_prim_mfr = 27

# Primary nozzle specific heat ratio
a2_ps_prim_shr = 28

# Primary nozzle exit static density
a2_ps_prim_sd = 29

# Primary nozzle exit Mach number
a2_ps_prim_m = 30

# Secondary nozzle total temperature
a2_ps_sec_tt = 31

# Secondary nozzle total pressure
a2_ps_sec_tp = 32

# Secondary nozzle pressure ratio
a2_ps_sec_pr = 33

# Secondary nozzle ideal velocity
a2_ps_sec_iv = 34

# Secondary nozzle exit area
a2_ps_sec_ea = 35

# Secondary nozzle mass flow rate
a2_ps_sec_mft = 36

# Secondary nozzle specific heat ratio
a2_ps_sec_shr = 37

# Secondary nozzle exit static density
a2_ps_sec_sd = 38

# Secondary nozzle exit Mach number
a2_ps_sec_m = 39

# Combustor mass flow rate 
a2_ps_comb_mfr = 40

# Combustor inlet total pressure
a2_ps_comb_itp = 41

# Combustor inlet total temperature
a2_ps_comb_itt = 42

# Combustor exit total pressure
a2_ps_comb_etp = 43

# Combustor exit total temperature
a2_ps_comb_ett = 44

# Low pressure turbine exit total temperature
a2_ps_turb_ett = 45

# Temperature drop through turbines
a2_ps_turb_td = 46

#!/usr/bin/python
# -----------------------------------------------------------------------------------------
# This is an Application Program Interface (API) that works directly with the user's  
# code such that the user does not interact with the source code.  This API
# contains the routines that the user will need to create  frame changes and
# calculate the position, velocity, acceleration, jerk, or snap.  This interface calls
# the routines that calculate these values.
# -----------------------------------------------------------------------------------------
# @file ANOPP2.api.h
# @author ANOPP2 Development Team
# @version 1.0.0
# -----------------------------------------------------------------------------------------



# =========================================================================================
# First part of this section contains interfaces into the available routines included in
# this API.
# =========================================================================================



# -----------------------------------------------------------------------------------------
# This subroutine initializes the ANOPP2.API and all modules it depends
# on.
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------
# This routine executes the unit tests in the ANOPP2.API.  The unit 
# tests execute all the tests implemented in the ANOPP2.API.
# -----------------------------------------------------------------------------------------
# @result
#        The number of failed asserts found while performing unit tests.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_unit_test.restype = int



# ---------------------------------------------------------------------------------------
#  This function takes in a tag representing a frame of reference list and returns true if
#  it exists in the API and false if it does not.
# ---------------------------------------------------------------------------------------
#  @param intTag
#         This is the tag associated to the frame of reference that is being searched for.
#  @result
#         A bool that is returned true if the frame of reference  exists and false if it
#         does not.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_kine_exists_for.restype = bool
ANOPP2.a2py_kine_exists_for.argtypes = [c_int]



# -----------------------------------------------------------------------------------------
# This routine creates of a frame of reference list and inserts it into the registry.
# This routine then returns a tag value that is kept by the user and provided whenever
# that frame of reference list is to be accessed.
# -----------------------------------------------------------------------------------------
# @param inputFile 
#        The name of the file that contains the necessary data-values describing how 
#        the object moves (rotation, translation, and their time derivatives). 
#        This is usually a .config file.  This file should only
#        contain one object's motion. Multiple objects will not be read in. A 
#        single file will need to be read in for each of the different configurations. 
#        This parameter is a C-C++ string and will need to be converted to a 
#        Fortran string before it is used by the modules.
# @param tag
#        An integer that correlates a number in the registry to a specific FoR that 
#        contains data that is used in the program. 
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_create_for.restype = int
ANOPP2.a2py_kine_create_for.argtypes = [c_char_p, POINTER(c_int)]




# -----------------------------------------------------------------------------------------
# This routine appends FrameChanges to an existing frame of reference list by
# reading them from a file in a similar way that the Create routine operates
# -----------------------------------------------------------------------------------------
# @param strSettingsFile
#        The name of the file that contains the necessary data-values describing how
#        the object moves (rotation, translation, and their time derivatives).
#        This is usually a .config file.  This file should only
#        contain one object's motion. Multiple objects will not be read in. A
#        single file will need to be read in for each of the different configurations.
#        This parameter is a C-C++ string and will need to be converted to a
#        Fortran string before it is used by the modules.
# @param intTag
#        This is an integer that is returned by this routine.  It be used to access
#        the Frame of Reference list that was appended.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_append_for.restype = int
ANOPP2.a2py_kine_append_for.argtypes = [c_char_p, POINTER(c_int)]



# -----------------------------------------------------------------------------------------
# This routines takes in a tag value and sets the for that will be operated on.  This
# is stored in the module so the calculations can be fast.
# -----------------------------------------------------------------------------------------
# @param tag
#        An integer representing the For list we want to set as the one that will
#        be operated on 
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_set_for.restype = int
ANOPP2.a2py_kine_set_for.argtypes = [c_int]



# -----------------------------------------------------------------------------------------
# This routine destroys an FoR element in the FoR registry.  This is because
# the user no longer needs the FoR that is stored in the registry.
# -----------------------------------------------------------------------------------------
# @param tag
#        An integer that is associated with the FoR that will be destroyed.  After
#        this destruction, the integer will have no meaning in the registry.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_destroy_for.restype = int
ANOPP2.a2py_kine_destroy_for.argtypes = [c_int]



# -----------------------------------------------------------------------------------------
# This routine creates a transformation object by reducing a FoR at a single time.
# The transformation object can be of type position, velocity, acceleration, jerk,
# or snap depending on the argument provided by the user.
# -----------------------------------------------------------------------------------------
# @param time
#        This is the time setting when the FoR linked list will be reduced to a 
#        single transformation.  The FoR linked list represents all motion throughout 
#        all time, a transformation is instantaneous.  This time value is the 
#        instantaneous value when the FoR linked list will be reduced to a single 
#        transformation. 
# @param transType
#        This refers to the type of transformation that is to be performed 
#        (i.e.. position, velocity, acceleration, jerk, or snap). \n
#        position     => 1 \n
#        velocity     => 2 \n
#        acceleration => 3 \n
#        jerk         => 4 \n 
#        snap         => 5
# @param transTag
#        An integer, stored in the registry, that is assigned to the transformation
#        created by this routine.  The user will have no access to the transformation
#        created here unless it is through this tag value.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_create_transformation.restype = int
ANOPP2.a2py_kine_create_transformation.argtypes = [c_float, c_int, POINTER(c_int)]



# ---------------------------------------------------------------------------------------
#  This function takes in a tag representing a transformation and returns true if it
#  exists in the API and false if it does not.
# ---------------------------------------------------------------------------------------
#  @param intTag
#         This is the tag associated to the transformation that is being searched for.
#  @result
#         A bool that is returned true if the transformation exists and false if it
#         does not.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_kine_exists_transformation.restype = bool
ANOPP2.a2py_kine_exists_transformation.argtypes = [c_int]



# -----------------------------------------------------------------------------------------
# This routines takes in a tag value and sets the for that will be operated on.  This
# is stoed in the module so the calculations can be fast.
# -----------------------------------------------------------------------------------------
# @param tag
#        An integer representing the transformation we want to set as the one that will
#        be operated on 
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_set_transformation.restype = int
ANOPP2.a2py_kine_set_transformation.argtypes = [c_int]



# -----------------------------------------------------------------------------------------
# This routine deletes a transformation object in the transformation
# registry.  This passes in a tag value from the user, passes the tag value to
# the registry, then the registry then finds the associated transformation
# object, and deltets the registry entry for that object.
# -----------------------------------------------------------------------------------------
# @param tag
#        The tag value associated with the transformation object that we want to 
#        destroy.  This tag value was provided to the user by the transformation
#        create routine (above).  The tag value is given to the registry which
#        deletes the associated transformation object.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_destroy_transformation.restype = int
ANOPP2.a2py_kine_destroy_transformation.argtypes = [c_int]



# -----------------------------------------------------------------------------------------
# This routine redefines the vectors such that they are all in the same frame of    
# reference.  In this case the frame of reference is the ground frame.
# -----------------------------------------------------------------------------------------
# @param xLocal
#        This is the local coordinates for the current frame of reference.
# @param xGlobal
#        This is the local coordinates transformed into the global frame of 
#        reference, also referred to as the ground frame of reference.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_global_reorient.restype = int
ANOPP2.a2py_kine_global_reorient.argtypes = [POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This routine redefines the vectors such that they are all in the same frame of    
# reference.  In this case the frame of reference is the ground frame.
# -----------------------------------------------------------------------------------------
# @param xLocal
#        This is the local coordinates for the current frame of reference.
# @param xGlobal
#        This is the local coordinates transformed into the global frame of 
#        reference, also referred to as the ground frame of reference.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_local_reorient.restype = int
ANOPP2.a2py_kine_local_reorient.argtypes = [POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This routine calculates the position of each of the frames of reference in the 
# global or ground frame.  This routine returns the position of a point in the 
# global frame. 
# -----------------------------------------------------------------------------------------
# @param xLocal
#       This is the local coordinates for the current frame of reference.
# @param xGlobal
#       This is the local position transformed into the global frame of 
#       reference, also referred to as the ground frame of reference.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_position.restype = int
ANOPP2.a2py_kine_position.argtypes = [POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This routine derives the necessary values from the position vector to calculate  
# the velocity vector in the global frame (ground frame).  This routine returns 
# the velocity of a point in the global frame. In this routine the motion of the 
# point in the local frame is stationary.
# -----------------------------------------------------------------------------------------
# @param xLocal
#        This is the local coordinates for the current frame of reference.
# @param vGlobal
#        This is the velocity vector in the global frame or the ground frame.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_velocity.restype = int
ANOPP2.a2py_kine_velocity.argtypes = [POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This routine derives the necessary values from the position vector to calculate  
# the acceleration vector in the global frame (ground frame).  This routine returns 
# the acceleration of a point in the global frame.  This routine assumes the source
# does not move in the local frame of reference.
# -----------------------------------------------------------------------------------------
# @param xLocal
#        This is the local coordinates for the current frame of reference.
# @param aGlobal
#        This is the acceleration vector in the global frame or the ground frame.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_acceleration.restype = int
ANOPP2.a2py_kine_acceleration.argtypes = [POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This routine derives the necessary values from the position vector to calculate  
# the jerk vector in the global frame (ground frame).  This routine returns the 
# jerk of a source point in the global frame of reference.  
# -----------------------------------------------------------------------------------------
# @param xLocal
#        This is the local coordinates for the current frame of reference.
# @param jGlobal
#        This is the jerk vector in the global frame or the ground frame.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_jerk.restype = int
ANOPP2.a2py_kine_jerk.argtypes = [POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This routine derives the necessary values from the position vector to calculate  
# the snap vector in the global frame (ground frame).  This routine returns the 
# snap of a source point in the global frame of reference.  
# -----------------------------------------------------------------------------------------
# @param xLocal
#        This is the local coordinates for the current frame of reference.
# @param jGlobal
#        This is the snap vector in the global frame or the ground frame.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_snap.restype = int
ANOPP2.a2py_kine_snap.argtypes = [POINTER(c_float), POINTER(c_float)]



#!/usr/bin/python
# =========================================================================================
# Next part of this interface file contains hardcoded enumerators used by the user's
# program.
# =========================================================================================



# -----------------------------------------------------------------------------------------
#  This enumeration is for the geometry of the output file.  The geometry can be in
#  a global frame of reference or a local frame of reference.
# -----------------------------------------------------------------------------------------


#  This is the enumeration for a global frame of reference 
a2_global = 1

#  This is the enumeration for a local frame of reference
a2_local = 2



# -----------------------------------------------------------------------------------------
# This file is the interface file for the Fortran subroutines in the acoustic analysis
# Application Programming Interface (API).  This file should be copied to your local
# directory and an "include 'ANOPP2.odule.api.f90'" must be present in your
# program.  See ANOPP2.PIDemonstrator.cplusplus.cpp for an example including
# using all present subroutines.
# -----------------------------------------------------------------------------------------
# @file ANOPP2.api.h
# @author The ANOPP2 Development Team
# @version 1.0.0
# -----------------------------------------------------------------------------------------



# =========================================================================================
# First part of this section contains interfaces into the available Propulsion API
# routines.
# =========================================================================================



# -----------------------------------------------------------------------------------------
# This subroutine initializes the acoustic analysis API and should be included at
# the very start of your program (before any other acoustic analysis subroutines
# are called).
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------
# This routine executes the unit tests in the Acoustic Analysis module.  The unit
# tests execute all the tests implemented in the Acoustic Analysis API.
# -----------------------------------------------------------------------------------------
# @result
#        An integer of the number of failed asserts that occurred during testing.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_aa_unit_test.restype = int



# -----------------------------------------------------------------------------------------
# This routine converts an input from one unit to another.  The supported units are
# defined in the acoustic units enumeration list and include pressure, pressure squared,
# and decibels.
# -----------------------------------------------------------------------------------------
# @param enumInput
#        This is the enumerator for the units of the input.
# @param fltInput
#        This is the value of the input in the units defined by enumInput.  This
#        will be converted to a different unit defined by enumOutput.
# @param enumOutput
#        This is the enumeration of the desired units.  fltInput will be converted
#        to these units.
# @param fltOutput
#        This is the result of this routine: fltInput which is in units enumInput
#        converted to the units defined by enumOutput.
# @result
#        An integer representing success of this operation.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_aa_convert.restype = int
ANOPP2.a2py_aa_convert.argtypes = [c_int, c_float, c_int, POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This routine returns a segment of a long pressure time history.  This routine takes
# in the long acoustic pressure time history (including the time and pressure values)
# and desired segment size, step size, and the segment number wanted.  This routine
# returns the size of the new segment and the time and function of the segment.
# This routine returns a logical success flag that is returned as false if the
# segmentation has failed.  This can occur if the segment size or step size are less
# than zero, or the segment number requested is less than 1.  \n
# If the segment size or segment step size do not fall on exact values of the discrete
# time samples in the long time and long func arrays, they are 'fudged' slightly to
# fall on exact samples.
# -----------------------------------------------------------------------------------------
# @param intNl
#        The size of the long acoustic pressure time history.  This is the size of the
#        longTime and longFunc arrays.
# @param fltLongTime
#        The long acoustic pressure time history.  This is used to create the segment.
# @param fltLongFunction
#        The long acoustic pressure time history.  This is the acoustic pressure at
#        the time samples in the long time array.
# @param fltTs
#        The size of the segment requested.  This number might be 'fudged' slightly to
#        fall on a sample in the long time and long func arrays.  This is returned
#        modified.
# @param fltS
#        The size of the incremental step between segments.  This can be less than or
#        greater than the segment size.  This number may be 'fudged' slightly if the
#        size is not exactly divisible by the time step size in the long time array.
# @param intN
#        The segment number in the long time history wanted.  This number must be
#        greater than 1 and less than the maximum number of segments possible.
# @param intNs
#        This is the size of the resultant segmented time and function arrays.  This
#        is returned by this subroutine.
# @param fltSegmentTime
#        The time array of the segment data.  This array is allocated by this routine
#        to size M (param m).  The last time step minimum the first time step should be
#        equal to the 'fudged' segment size.
# @param fltSegmentFunction
#        The function array of the segmented data.  This is the function at the time
#        steps in the segment time array.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_aa_segment.restype = int
ANOPP2.a2py_aa_segment.argtypes =                                          \
     [c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float), \
      c_int, POINTER(c_int), POINTER(POINTER(c_float)), POINTER(POINTER(c_float))]



# -----------------------------------------------------------------------------------------
# This routine windows an acoustic pressure time history.  The window function is
# chosen via an enumerator passed to the routine as the first argument.  The size of the
# time array and function must be the same.  A logical success parameter is returned
# by the function.  This is true if the routine succeeded, and false if it failed.
# -----------------------------------------------------------------------------------------
# @param enumWindow
#        The enumerated value of the window function to be applied.
# @param intN
#        The size of the function and time arrays.
# @param fltTime
#        The time where the acoustic pressure is sampled.  This must be an evenly
#        spaced array.
# @param fltFunction
#        The array of acoustic pressure to be windowed.  These values in is the
#        function at the time in the time array.  This is overwritten by the
#        windowed function.
# @result
#        An integer representation of success.  0 indicates no errors.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_aa_window.restype = int
ANOPP2.a2py_aa_window.argtypes = \
     [c_int, c_int, POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This routine applies a high and low pass filter to a Pressure Time History
# -----------------------------------------------------------------------------------------
# @param intN
#        This is the size of the Time and Pressure arrays.
# @param fltTime
#        This is the array of times for the Time History.
# @param fltPressure
#        This is the array of pressures for the Time History
# @param fltHighPassFrequency
#        This is the frequency for the low pass filter, which will set all lower
#        frequencies to zero.
# @param fltLowPassFrequency
#        This is the frequency for the high pass filter, which will set all higher
#        frequencies to zero.
# @result
#        A logical success flag.  If the routine succeeded, this is returned as
#        true.  If it failed, this is returned as false.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_aa_filter.restype = int
ANOPP2.a2py_aa_filter.argtypes = \
     [c_int, POINTER(c_float), POINTER(c_float), c_float, c_float]



# -----------------------------------------------------------------------------------------
# This routine calculates the narrowband spectrum for three types of input. The
# input types may be a pressure time history, an octave sound pressure level, or
# a power spectral density.  The power spectral density may have units of dB/Hz or
# Pascals squared per Hz.  If the input is a pressure time history, the independent
# variable will be time and the dependent variable will be acoustic pressure.  If the
# input is an octave sound pressure level or a power spectral density with units of
# dB/Hz, the independent variable will be frequency and the dependent variable will be
# decibels.  If the input is a power spectral density with units of Pascals squared per
# Hz, the independent variable will be frequency and the dependent variable will be
# acoustic pressure.  The parameter enumInputType  identifies the input type.  The
# integer intM is the size of the result arrays of frequency and narrowband spectrum.
# If the input is pressure time history, intM is returned as INT(intN/2) because of
# the Nyquist criteria.  If the input is octave SPL or a power spectral density, intM is
# input for the size of the resultant narrowband spectrum.
# -----------------------------------------------------------------------------------------
# @param dmy_enumMetric
#        This input parameter identifies the input type of the independent and dependent
#        variables.  This must be one of the supported metrics in the enumeration for
#        metrics.  Supported metrics include: a2_aa_apth, a2_aa_psd, and a2_aa_octave.
# @param dmy_enumUnits
#        These are the units of the input.  Supported units include a2_aa_ap, a2_aa_msp,
#        and a2_aa_db.  Not all combinations of metric and units are supported.  An
#        a2_aa_apth must be accompanied by a2_aa_ap.  An a2_aa_psd can be in either
#        a2_aa_msp or a2_aa_db.  An a2_aa_octave must be accompanied by a2_aa_db.
# @param intN
#        Dimension of the independent and dependent arrays
# @param fltIndepedent
#        The independent variable will be time when the input type is a pressure time
#        series.  The independent variable will be frequencies when dependent variable
#        is an octave sound pressure level or a power spectral density. The independent
#        variable must be evenly spaced times when the input type is a pressure time
#        history or a power spectral density. The independent variable is not required to
#        be evenly spaced when the input type is an octave sound pressure level.
# @param fltDependent
#        The dependent variable is an array of pressures squared or decibels depending
#        on the value of the parameter enumInputType.
# @param intM
#        The dimension of the resultant frequency and narrowband spectrum.  This number
#        is returned by this routine if the input is an acoustic pressure time series.
#        This number is input if the input is an octave sound pressure level or power
#        spectral density.
# @param fltFrequency
#        The frequencies of the result narrowband spectrum.  This array is filled and
#        returned by this routine.
# @param fltNbsMsp
#        The narrowband spectrum.  This array is filled, and returned by this routine.
# @param fltPhase
#        The phase of the narrowband spectrum.
# @result
#        An integer success flag.  If the routine succeeded, this is returned as
#        0.  If it failed, this is returned as a non-zero number
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_aa_nbs.restype = int
ANOPP2.a2py_aa_nbs.argtypes =                                        \
     [c_int, c_int, c_int, POINTER(c_float), POINTER(c_float), POINTER(c_int), \
      POINTER(POINTER(c_float)), POINTER(POINTER(c_float)), POINTER(POINTER(c_float))]



# -----------------------------------------------------------------------------------------
# This routine calculates the power spectral density for three types of input. The
# input types may be a pressure time history, an octave sound pressure level, or
# a narrowband spectrum.  The narrowband spectrum may have units of dB/Hz or Pascals
# squared per Hz.  If the input is a pressure time history, the independent variable
# will be time and the dependent variable will be acoustic pressure.  If the input is an
# octave sound pressure level or a power spectral density with units of dB/Hz, the
# independent variable will be frequency and the dependent variable will be decibels.
# If the input is  a narrowband spectrum with units of Pascals squared per Hz, the
# independent variable will be frequency and the dependent variable will be acoustic
# pressure.  The parameter Input  identifies the input type.  The integer intM is the
# size of the result arrays of frequency and narrowband spectrum.  If the input is
# pressure time history, M is returned as INT(N/2) because of the Nyquist criteria.
# If the input is octave SPL or a narrowband spectrum, M  is input for the size of the
# resultant narrowband spectrum.\n
# This is the Fortran binding of this routine.
# -----------------------------------------------------------------------------------------
# @param dmy_enumMetric
#        This input parameter identifies the input type of the independent and dependent
#        variables.  This must be one of the supported metrics in the enumeration for
#        metrics.  Supported metrics include: a2_aa_apth, a2_aa_nbs, and a2_aa_octave.
# @param dmy_enumUnits
#        These are the units of the input.  Supported units include a2_aa_ap, a2_aa_msp,
#        and a2_aa_db.  Not all combinations of metric and units are supported.  An
#        a2_aa_apth must be accompanied by a2_aa_ap.  An a2_aa_nbs can be in either
#        a2_aa_msp or a2_aa_db.  An a2_aa_octave must be accompanied by a2_aa_db.
# @param intN
#        The size of the time and pressure arrays provided to this routine.
# @param fltIndepedent
#        The independent variable will be time when the input type is a pressure time
#        series.  The independent variable will be frequencies when the dependent
#        variable is an octave sound pressure level or a narrowband spectrum. The
#        independent  variable must be evenly spaced times when the input type is a
#        pressure time history or a power spectral density. The independent variable is
#        not required to be evenly spaced when the input type is an octave sound
#        pressure level.
# @param fltDependent
#        The acoustic pressure at the time values in the time array or the SPL values
#        of the octave sound pressure level.
# @param intM
#        The size of the resultant frequency and PSD arrays.  This number is returned
#        by this routine if the input is an acoustic pressure time series.  This number
#        is input if the input was an octave SPL.
# @param fltFrequency
#        The frequencies of the result power spectral density.  This array is filled
#        and allocated by this routine.
# @param fltNbsMsp
#        The power spectral density of the pressure time history.  This array is
#        allocated, filled, and returned by this routine.
# @param fltPhase
#        The phase of the power spectral density
# @result
#        An integer success flag.  If the routine succeeded, this is returned as
#        0.  If it failed, this is returned as a non-zero number
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_aa_psd.restype = int
ANOPP2.a2py_aa_psd.argtypes =                                        \
     [c_int, c_int, c_int, POINTER(c_float), POINTER(c_float), POINTER(c_int), \
      POINTER(POINTER(c_float)), POINTER(POINTER(c_float)), POINTER(POINTER(c_float))]



# -----------------------------------------------------------------------------------------
# This routine alters a function as to a frequency weighting parameter.  Possible
# weighting functions are: A, B, C, and none.  This function takes in a frequency
# and noise array and an enumerator for the weighting function.  At each frequency
# a weight is calculated.  This weight is multiplied times the function which is
# overwritten and returned.  This routine also returns a success flag which can
# be false if the weight function is invalid.
# -----------------------------------------------------------------------------------------
# @param enumWeight
#        An integer representing the weighting that is applied.  Refer to the manual
#        for specifics on the enumeration options of frequency weighting.
# @param enumMetric
#        This is an enumeration for the acoustic metric that is provided as input.  The
#        options include a2_aa_nb for Narrowband Spectrum, a2_aa_psd for Power Spectral
#        Density, and a2_aa_octave for 1/3rd-Octave Sound Pressure Level.  If the
#        input is a 1/3rd-Octave then each band is separated into 7 subbands which are
#        weighted separately then summed.
# @param enumUnits
#        An enumeration identifying the units of the input function.  This is specified
#        via the units enumerations.
# @param intM
#        The size of the function that is to be weighted.  This integer is the size
#        of the following 2 arguments.
# @param fltFrequencies
#        The frequencies of the spectrum that is to be weighted.  This is used to
#        calculate the weighting function at that frequency that is applied to the
#        function
# @param fltFunction
#        The function that is to be weighted.  The weighting parameter is a function
#        of frequency.  For each frequency, that weighting function is multiplied
#        time the function.  The result is placed into this array.
# @result
#        An integer representing the success of this program.  This will be returned
#        as non zero if this routine fails.  Reason for failing may be an unknown
#        weight parameter.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_aa_weight.restype = int
ANOPP2.a2py_aa_weight.argtypes = \
     [c_int, c_int, c_int, c_int, POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This routine calculates the octave band spectrum given a power spectral density or a
# narrowband spectrum.  The psd can be input with units of dB/Hz of Pascals squared/Hz.
# Similarly, the narrowband spectrum can be input with units of dB/Bin of Pascals
# squared/Bin.  This routine calculates the center frequencies based on the octave
# number requested and the band type.  The result is returned in two arrays that are
# allocated by this routine.  The arrays are filled with the center band frequencies and
# octave band levels that were able to be calculated by this routine.  The number and
# spacing of the octave band center frequencies are determined by the octave number (3
# for 1/3, etc.).
# -----------------------------------------------------------------------------------------
# @param enumMetric
#        This input parameter identifies the input type of the independent and dependent
#        variables.  This must be one of the supported metrics in the enumeration for
#        metrics.  Supported metrics include: a2_aa_nbs and a2_aa_psd.
# @param enumUnits
#        These are the units of the input.  Supported units include a2_aa_msp and
#        a2_aa_db.
# @param intM
#        The dimension of the spectrum and frequency arrays.
# @param fltInputFrequencies
#        The frequencies of the input spectrum.  The frequency array must be
#        an evenly spaced array.  This array will be used to calculate the lower
#        and upper limits of the lower and upper most octave band.  If a band does
#        not contain enough information (frequency content) to fill a band, it is
#        not returned.
# @param fltInputSpectrum
#        The input spectrum used to calculate the octave band spectrum.
#        The values are at the frequencies given in the inputFrequencies array.
#        An integral of this array over the bounds of the octave bin is used to
#        calculate the value at the octave center band frequency.
# @param fltOctaveNumber
#        The octave number, ex. 3 for 1/3rd, etc.  This number must be greater than
#        zero. (See Notes: #1, VALUE attribute)
# @param enumBandType
#        This enumeration will set the octave center band frequency approximation
#        algorithm. This means the code will use an approximate algorithm instead of
#        the exact algorithm.  a2_aa_exact for exact, a2_aa_approximate for approximate,
#        and, a2_aa_preferred for preferred.
# @param intNb
#        The size of the frequency and noise arrays of the result octave band
#        spectrum (next two arguments).
# @param fltObsFrequencies
#        The frequency arrays of the octave band spectrum.  This is the center band
#        frequencies of each bin in the octave spectrum.  Each bin represents a range
#        of frequencies, these center frequencies are only set if enough information
#        is present to integrate over the entire band.
# @param fltObs
#        The integrated psd over the band width for each center frequency. This array
#        is the same size as the octave frequencies array (m).
# @result
#        An integer representing success of this operation.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_aa_octave.restype = int
ANOPP2.a2py_aa_octave.argtypes =                                     \
     [c_int, c_int, c_int, POINTER(c_float), POINTER(c_float), c_float, c_int, \
      POINTER(c_int), POINTER(POINTER(c_float)), POINTER(POINTER(c_float))]



# -----------------------------------------------------------------------------------------
# This routine calculates the overall sound pressure level from a power spectral
# density spectrum or an octave spectrum (1/3rd, 1/8th, etc).  The inputs to this
# function are N, the size of the input arrays, a noise spectrum which can be
# a power spectral density or an octave spectrum, a frequency array and units of the
# noise.  If the units are set to 0, the noise argument is the power
# spectral density.  If the units are provided at 1, the noise argument is
# an octave spectrum (1/3rd, 1/8th, etc.).  The result is the overall sound pressure
# level, overall the frequencies.  An integer is returned that is the success of this
# routine. \n
# -----------------------------------------------------------------------------------------
# @param dmy_enumMetric
#        This input parameter identifies the input type of the independent and dependent
#        variables.  This must be one of the supported metrics in the enumeration for
#        metrics.  Supported metrics include: a2_aa_psd and a2_aa_nb.
# @param dmy_enumUnits
#        These are the units of the input.  Supported units include a2_aa_msp and
#        a2_aa_db.
# @param intM
#        The size of the noise and frequencies array.
# @param fltFrequencies
#        If this array is specified, this is the frequencies of the power spectral
#        density provided in the noise argument.  It has to be the same size as the
#        noise array.
# @param fltNnoise
#        Either the power spectral density or octave spectrum.  If the units are 0
#        this is the power spectral density and the overall level is calculated by
#        integrating over frequency.  If the units are 1 than this is the octave
#        spectrum (1/3rd, 1/8th, etc).  Since that is already integrated, the overall
#        level is the sum of the spectrum.
# @param fltL
#        The overall sound pressure level of the spectrum.  This is returned
#        by this routine.
# @result
#        A integer success flag that is zero if this routine has succeeded and
#        non-zero if it has not.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_aa_oaspl.restype = int
ANOPP2.a2py_aa_oaspl.argtypes = \
     [c_int, c_int, c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This routine calculates the perceived noise level and tone-corrected perceived
# noise level from a given 1/3rd-octave sound pressure level array.  The SPL array
# must exist over the standard 24 1/3rd octave bins.  These are from 50Hz to 10kHz.
# -----------------------------------------------------------------------------------------
# @param fltSPL
#        The 24 1/3rd-octave sound pressure level array.  These the SPL values at
#        the 1/3rd-octave center band frequencies from 50 to 10,000 Hz.
# @param blnIgnoreTones800HzAndBelow
#        Logical flag to ignore tones of 800 Hz and below
# @param fltPnl
#        The perceived noise level calculated from the 1/3-rd octave SPL.
# @param fltPnlt
#        The tone-corrected perceived noise level calculated from the 1/3rd-octave
#        sound pressure level.
# @param fltBandFrequency
#        This is the 1/3rd-Octave Band SPL frequency that causes the highest tone
#        correction penalty.
# @param fltToneCorrection
#        This is the value of the tone correction at the above frequency.
# @result
#        A success integer that is returned 0 if this routine has succeeded.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_aa_pnl_pnlt.restype = int
ANOPP2.a2py_aa_pnl_pnlt.argtypes =                                          \
     [POINTER(c_float), c_bool, POINTER(c_float), POINTER(c_float), POINTER(c_float), \
      POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This routine calculates the effective perceived noise level from a series of
# tone-corrected perceived noise levels.  Inputs into this routine are the size of
# the time and PNLT arrays, a time array, and a PNLT array.  The result is a real
# value for the effective perceived noise level.  This routine returns a success
# parameter that is true if the routine has succeeded and false if it has failed.
# -----------------------------------------------------------------------------------------
# @param intN
#        The size of the time and tone-corrected perceived noise arrays.
# @param fltTime
#        An array of time where the PNLT values are computed.  This does not have to
#        evenly spaced in time.
# @param fltPnlt
#        Tone-corrected perceived noise level at the times in the time array.
# @param fltEpnl
#        Output Effective Perceived Noise Level.
# @param fltDuration
#        This is the duration factor D, calculated during the EPNL calculation.
# @param fltTimeRange
#        This is the minimum and maximum time of the EPNL calculation.
# @result
#        An integer that is returned 0 if this routine has succeeded.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_aa_epnl.restype = int
ANOPP2.a2py_aa_epnl.argtypes =                                             \
     [c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float), \
      POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This routine calculates the sound exposure level given a time array and an array
# of overall sound pressure levels.  This calculates the sound exposure level and
# returns a logical for success.
# -----------------------------------------------------------------------------------------
# @param intN
#        The size of the time and overall sound pressure level arrays
# @param fltTime
#        An array of time variables.  This are the time locations of the overall sound
#        pressure levels.  This does not have to be evenly spaced.
# @param fltL
#        An array of overall sound pressure levels at the time in the time array.
# @param fltSEL
#        Output Sound Exposure Level.
# @param fltDuration
#        This is the duration factor D, calculated during the SEL calculation.
# @param fltTimeRange
#        This is the minimum and maximum time of the SEL calculation.
# @result
#        An integer that is returned 0 if this routine has succeeded.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_aa_sel.restype = int
ANOPP2.a2py_aa_sel.argtypes =                                              \
     [c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float), \
      POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This routine calculates the contour area using the zeroth order interpolation
# method or the Delaunay triangulation method.
# -----------------------------------------------------------------------------------------
# @param intN
#        Integer number of X nodes
# @param intM
#        Integer number of Y nodes
# @param fltX
#        Two dimensional array of X coordinates
# @param fltY
#        Two dimensional array of Y coordinates
# @param fltL
#        Two dimensional array of noise levels (typically SEL or EPNL)
# @param fltContour
#        Contour level within which the area is to be calculated
# @param fltMaxLength
#        Maximum length of a triangle side
# @param enumMethod
#        Contour area method enumeration.
# @param fltArea
#        The area in square kilometers of all rectangles with center noise levels
#        greater than or equal to the noise level specified by Contour.
# @result
#        An integer result that returns 0 if the area calculation is successfully
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_aa_exposure_area.restype = int
ANOPP2.a2py_aa_exposure_area.argtypes =                                  \
     [c_int, c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float), c_float, \
      c_float, c_int, POINTER(c_float)]



# =========================================================================================
#  The next part of this interface file contains enumerators for the Acoustic Analysis API.
# =========================================================================================



# -----------------------------------------------------------------------------------------
#  This enumeration grouping is to convey what type of noise metric.  Each enumerator is
#  equivalient to a type of noise metric such as Acoustic Pressure Time History or
#  Power Spectral Density.
# -----------------------------------------------------------------------------------------

# The initial post process level is just for acoustic pressure time history
a2_aa_apth = 1

# This enumerator is for the acoustic velocity time history.
a2_aa_avth = 2

# This enumerator is for pressure gradient time history.
a2_aa_pgth = 3

# This enumerator is for pure tones
a2_aa_tones = 4

# This enumerator is for narrow band spectrum
a2_aa_nbs = 5

# The next post processing level is for the power spectral density spectrum
a2_aa_psd = 6

# The next is for octave sound pressure levels
a2_aa_octave = 7

# The next is for overall sound pressure levels
a2_aa_oaspl = 8

# The next is for perceived noise level
a2_aa_pnl = 9

# The is for the sound exposure noise level
a2_aa_sel = 10

# An enumerator for the effective perceived noise level
a2_aa_epnl = 11

# An enumerator for the surface area under a limit of dB.
a2_aa_ea = 12



# -----------------------------------------------------------------------------------------
#  This enumeration grouping is to determine what characteristic of the noise is included
#  by the metric.  Options include absolute levels (such as a noise measurement) or
#  change in levels (such as a suppression).
# -----------------------------------------------------------------------------------------

# These are the default, which is an unknown level.
a2_aa_unknown_levels = 1

# This is the enumeration of absolute levels
a2_aa_absolute_levels = 2

# This is the enumeration of change in levels
a2_aa_change_in_levels = 3



# -----------------------------------------------------------------------------------------
#  These enumerations are to convery what type of units the noise metrics are in.  These
#  are passed to the Acoustic Analysis API routines with the metric so the Acoustic
#  Analysis computations are performed correctly.
# -----------------------------------------------------------------------------------------

# This enumerator is for pressure in Pascals.
a2_aa_pa = 1

# This enumerator is for mean squared pressure (MSP).
a2_aa_msp = 2

# This enumerator is for decibels.
a2_aa_db = 3



# -----------------------------------------------------------------------------------------
#  These enumerators are for the different time-domain windows that are available in the
#  acoustic analysis API.  As of now there are 5 different window types available:
#  No window, Blackman, flat top, Hanning, and Hamming windows.
# -----------------------------------------------------------------------------------------

# This enumerator is for no window.
a2_aa_no_window = 1

# This enumerator is for the Blackman window.
a2_aa_blackman_window = 2

# This enumerator is for the flat top window.
a2_aa_flat_top_window = 3

# This enumerator is for the Hanning window.
a2_aa_hanning_window = 4

# This enumerator is for the Hamming window.
a2_aa_hamming_window = 5



# -----------------------------------------------------------------------------------------
#  These enumerators are for the frequency weighting of narrowband spectra, power
#  spectral densities, and 1/3rd-Octave sound pressure levels.  There are 4 different
#  weighting functions: no-weighting, a-weighting, b-weighting, and c-weighting.  Refer
#  to the  Acoustic Analysis API Manual for more information.
# -----------------------------------------------------------------------------------------

# This enumerator is for no-weight
a2_aa_no_weight = 1

# This enumerator is for a-weight
a2_aa_a_weight = 2

# This enumerator is for b-weight
a2_aa_b_weight = 3

# This enumerator is for c-weight
a2_aa_c_weight = 4



# -----------------------------------------------------------------------------------------
#  These enumerators are for the different types of calculating the octave band center,
#  lower limit, and upper limit frequencies.  Currently, there are 3 methods: exact,
#  preferred, and approximate.  Please see documentation on the different methods.
# -----------------------------------------------------------------------------------------

# This enumerator is for the exact method.
a2_aa_exact = 1

# This is for the preferred method.
a2_aa_preferred = 2

# This is for the approximate method.
a2_aa_approximate = 3



# -----------------------------------------------------------------------------------------
#  This enumerator group defines the different methods for determining a contour area.
#  Currently 2 options exist: Zeroth order interpolation and Delauney triangulation.
# -----------------------------------------------------------------------------------------

# This enumerator is for the zeroth order interpolation.
a2_aa_zeroth = 1

# Thie enumerator is for the Delaunay triangulation.
a2_aa_delaunay = 2



# =========================================================================================
#  These are the parameters defined in the Acoustic Analysis API.
# =========================================================================================



# -----------------------------------------------------------------------------------------
#  This array contains the standard 24 1/3rd-Octave Sound Pressure Level center band
#  frequencies ranging from 50 to 10,000 Hz.
# -----------------------------------------------------------------------------------------
a2_aa_std_center_frequencies =                                                           \
     (c_float * 24)(*[50.0, 63.0, 80.0, 100.0, 125.0, 160.0, 200.0, 250.0, 315.0, 400.0, \
        500.0, 630.0, 800.0, 1000.0, 1250.0, 1600.0, 2000.0, 2500.0, 3150.0, 4000.0,     \
        5000.0, 6300.0, 8000.0, 10000.0])

# -----------------------------------------------------------------------------------------
#  Reference pressure in Pascals, used to calculate sound pressure levels
# -----------------------------------------------------------------------------------------
a2_aa_reference_pressure = c_float(20.0e-6)



#!/usr/bin/python
# -----------------------------------------------------------------------------------------
# This is an Application Program Interface (API) that works directly with the user's  
# code such that the user does not interact with the source code.  This API
# contains the routines that the user will need to create  frame changes and
# calculate the position, velocity, acceleration, jerk, or snap.  This interface calls
# the routines that calculate these values.
# -----------------------------------------------------------------------------------------
# @file ANOPP2.api.h
# @author ANOPP2 Development Team
# @version 1.0.0
# -----------------------------------------------------------------------------------------



# =========================================================================================
# First part of this section contains interfaces into the available routines included in
# this API.
# =========================================================================================



# -----------------------------------------------------------------------------------------
# This subroutine initializes the ANOPP2.API and all modules it depends
# on.
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------
# This routine executes the unit tests in the ANOPP2.API.  The unit 
# tests execute all the tests implemented in the ANOPP2.API.
# -----------------------------------------------------------------------------------------
# @result
#        The number of failed asserts found while performing unit tests.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_unit_test.restype = int



# ---------------------------------------------------------------------------------------
#  This function takes in a tag representing a frame of reference list and returns true if
#  it exists in the API and false if it does not.
# ---------------------------------------------------------------------------------------
#  @param intTag
#         This is the tag associated to the frame of reference that is being searched for.
#  @result
#         A bool that is returned true if the frame of reference  exists and false if it
#         does not.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_kine_exists_for.restype = bool
ANOPP2.a2py_kine_exists_for.argtypes = [c_int]



# -----------------------------------------------------------------------------------------
# This routine creates of a frame of reference list and inserts it into the registry.
# This routine then returns a tag value that is kept by the user and provided whenever
# that frame of reference list is to be accessed.
# -----------------------------------------------------------------------------------------
# @param inputFile 
#        The name of the file that contains the necessary data-values describing how 
#        the object moves (rotation, translation, and their time derivatives). 
#        This is usually a .config file.  This file should only
#        contain one object's motion. Multiple objects will not be read in. A 
#        single file will need to be read in for each of the different configurations. 
#        This parameter is a C-C++ string and will need to be converted to a 
#        Fortran string before it is used by the modules.
# @param tag
#        An integer that correlates a number in the registry to a specific FoR that 
#        contains data that is used in the program. 
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_create_for.restype = int
ANOPP2.a2py_kine_create_for.argtypes = [c_char_p, POINTER(c_int)]




# -----------------------------------------------------------------------------------------
# This routine appends FrameChanges to an existing frame of reference list by
# reading them from a file in a similar way that the Create routine operates
# -----------------------------------------------------------------------------------------
# @param strSettingsFile
#        The name of the file that contains the necessary data-values describing how
#        the object moves (rotation, translation, and their time derivatives).
#        This is usually a .config file.  This file should only
#        contain one object's motion. Multiple objects will not be read in. A
#        single file will need to be read in for each of the different configurations.
#        This parameter is a C-C++ string and will need to be converted to a
#        Fortran string before it is used by the modules.
# @param intTag
#        This is an integer that is returned by this routine.  It be used to access
#        the Frame of Reference list that was appended.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_append_for.restype = int
ANOPP2.a2py_kine_append_for.argtypes = [c_char_p, POINTER(c_int)]



# -----------------------------------------------------------------------------------------
# This routines takes in a tag value and sets the for that will be operated on.  This
# is stored in the module so the calculations can be fast.
# -----------------------------------------------------------------------------------------
# @param tag
#        An integer representing the For list we want to set as the one that will
#        be operated on 
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_set_for.restype = int
ANOPP2.a2py_kine_set_for.argtypes = [c_int]



# -----------------------------------------------------------------------------------------
# This routine destroys an FoR element in the FoR registry.  This is because
# the user no longer needs the FoR that is stored in the registry.
# -----------------------------------------------------------------------------------------
# @param tag
#        An integer that is associated with the FoR that will be destroyed.  After
#        this destruction, the integer will have no meaning in the registry.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_destroy_for.restype = int
ANOPP2.a2py_kine_destroy_for.argtypes = [c_int]



# -----------------------------------------------------------------------------------------
# This routine creates a transformation object by reducing a FoR at a single time.
# The transformation object can be of type position, velocity, acceleration, jerk,
# or snap depending on the argument provided by the user.
# -----------------------------------------------------------------------------------------
# @param time
#        This is the time setting when the FoR linked list will be reduced to a 
#        single transformation.  The FoR linked list represents all motion throughout 
#        all time, a transformation is instantaneous.  This time value is the 
#        instantaneous value when the FoR linked list will be reduced to a single 
#        transformation. 
# @param transType
#        This refers to the type of transformation that is to be performed 
#        (i.e.. position, velocity, acceleration, jerk, or snap). \n
#        position     => 1 \n
#        velocity     => 2 \n
#        acceleration => 3 \n
#        jerk         => 4 \n 
#        snap         => 5
# @param transTag
#        An integer, stored in the registry, that is assigned to the transformation
#        created by this routine.  The user will have no access to the transformation
#        created here unless it is through this tag value.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_create_transformation.restype = int
ANOPP2.a2py_kine_create_transformation.argtypes = [c_float, c_int, POINTER(c_int)]



# ---------------------------------------------------------------------------------------
#  This function takes in a tag representing a transformation and returns true if it
#  exists in the API and false if it does not.
# ---------------------------------------------------------------------------------------
#  @param intTag
#         This is the tag associated to the transformation that is being searched for.
#  @result
#         A bool that is returned true if the transformation exists and false if it
#         does not.
# ---------------------------------------------------------------------------------------
ANOPP2.a2py_kine_exists_transformation.restype = bool
ANOPP2.a2py_kine_exists_transformation.argtypes = [c_int]



# -----------------------------------------------------------------------------------------
# This routines takes in a tag value and sets the for that will be operated on.  This
# is stoed in the module so the calculations can be fast.
# -----------------------------------------------------------------------------------------
# @param tag
#        An integer representing the transformation we want to set as the one that will
#        be operated on 
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_set_transformation.restype = int
ANOPP2.a2py_kine_set_transformation.argtypes = [c_int]



# -----------------------------------------------------------------------------------------
# This routine deletes a transformation object in the transformation
# registry.  This passes in a tag value from the user, passes the tag value to
# the registry, then the registry then finds the associated transformation
# object, and deltets the registry entry for that object.
# -----------------------------------------------------------------------------------------
# @param tag
#        The tag value associated with the transformation object that we want to 
#        destroy.  This tag value was provided to the user by the transformation
#        create routine (above).  The tag value is given to the registry which
#        deletes the associated transformation object.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_destroy_transformation.restype = int
ANOPP2.a2py_kine_destroy_transformation.argtypes = [c_int]



# -----------------------------------------------------------------------------------------
# This routine redefines the vectors such that they are all in the same frame of    
# reference.  In this case the frame of reference is the ground frame.
# -----------------------------------------------------------------------------------------
# @param xLocal
#        This is the local coordinates for the current frame of reference.
# @param xGlobal
#        This is the local coordinates transformed into the global frame of 
#        reference, also referred to as the ground frame of reference.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_global_reorient.restype = int
ANOPP2.a2py_kine_global_reorient.argtypes = [POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This routine redefines the vectors such that they are all in the same frame of    
# reference.  In this case the frame of reference is the ground frame.
# -----------------------------------------------------------------------------------------
# @param xLocal
#        This is the local coordinates for the current frame of reference.
# @param xGlobal
#        This is the local coordinates transformed into the global frame of 
#        reference, also referred to as the ground frame of reference.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_local_reorient.restype = int
ANOPP2.a2py_kine_local_reorient.argtypes = [POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This routine calculates the position of each of the frames of reference in the 
# global or ground frame.  This routine returns the position of a point in the 
# global frame. 
# -----------------------------------------------------------------------------------------
# @param xLocal
#       This is the local coordinates for the current frame of reference.
# @param xGlobal
#       This is the local position transformed into the global frame of 
#       reference, also referred to as the ground frame of reference.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_position.restype = int
ANOPP2.a2py_kine_position.argtypes = [POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This routine derives the necessary values from the position vector to calculate  
# the velocity vector in the global frame (ground frame).  This routine returns 
# the velocity of a point in the global frame. In this routine the motion of the 
# point in the local frame is stationary.
# -----------------------------------------------------------------------------------------
# @param xLocal
#        This is the local coordinates for the current frame of reference.
# @param vGlobal
#        This is the velocity vector in the global frame or the ground frame.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_velocity.restype = int
ANOPP2.a2py_kine_velocity.argtypes = [POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This routine derives the necessary values from the position vector to calculate  
# the acceleration vector in the global frame (ground frame).  This routine returns 
# the acceleration of a point in the global frame.  This routine assumes the source
# does not move in the local frame of reference.
# -----------------------------------------------------------------------------------------
# @param xLocal
#        This is the local coordinates for the current frame of reference.
# @param aGlobal
#        This is the acceleration vector in the global frame or the ground frame.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_acceleration.restype = int
ANOPP2.a2py_kine_acceleration.argtypes = [POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This routine derives the necessary values from the position vector to calculate  
# the jerk vector in the global frame (ground frame).  This routine returns the 
# jerk of a source point in the global frame of reference.  
# -----------------------------------------------------------------------------------------
# @param xLocal
#        This is the local coordinates for the current frame of reference.
# @param jGlobal
#        This is the jerk vector in the global frame or the ground frame.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_jerk.restype = int
ANOPP2.a2py_kine_jerk.argtypes = [POINTER(c_float), POINTER(c_float)]



# -----------------------------------------------------------------------------------------
# This routine derives the necessary values from the position vector to calculate  
# the snap vector in the global frame (ground frame).  This routine returns the 
# snap of a source point in the global frame of reference.  
# -----------------------------------------------------------------------------------------
# @param xLocal
#        This is the local coordinates for the current frame of reference.
# @param jGlobal
#        This is the snap vector in the global frame or the ground frame.
# @result
#        An integer representation of success.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_kine_snap.restype = int
ANOPP2.a2py_kine_snap.argtypes = [POINTER(c_float), POINTER(c_float)]



#!/usr/bin/python
# =========================================================================================
# Next part of this interface file contains hardcoded enumerators used by the user's
# program.
# =========================================================================================



# -----------------------------------------------------------------------------------------
#  This enumeration is for the geometry of the output file.  The geometry can be in
#  a global frame of reference or a local frame of reference.
# -----------------------------------------------------------------------------------------


#  This is the enumeration for a global frame of reference 
a2_global = 1

#  This is the enumeration for a local frame of reference
a2_local = 2



#!/usr/bin/python
# -----------------------------------------------------------------------------------------
# The error API contains a list of functions for tracking errors and reporting them
# to a log file.  There is a registry in the ANOPP2.odule that contains all the errors
# in the current run.
# -----------------------------------------------------------------------------------------
# @author The ANOPP2 Development Team
# @version 1.0.0
# @file ANOPP2.api.h
# -----------------------------------------------------------------------------------------



# =========================================================================================
# First part of this section contains interfaces into the available routines included in
# this API.
# =========================================================================================



# -----------------------------------------------------------------------------------------
# This initializes the error API. This creates the internal registry and makes the
# error enumerators available.
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------
# This routine executes the unit tests in the ANOPP2.module.  The unit
# tests execute all the tests implemented in the ANOPP2.API.
# -----------------------------------------------------------------------------------------
# @result
#         The number of failed asserts found during unit testing.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_error_unit_test.restype = int



# -----------------------------------------------------------------------------------------
# This functions reports an error to the log file.  The file name is passed to this
# routine with the line numbers, error enumerator and a message.
# -----------------------------------------------------------------------------------------
# @param  strFileName
#         A character string containing the name of the file where the error occurred
# @param  intLineNumber
#         An integer containing the line number where the error has occured
# @param  enumError
#         An integer that indicates what kind of error has occured
# @param  strMessage
#         A character string containing a message that should be displayed with the
#         error
# @result
#         An integer that if positive represents an error tag and if negative indicates
#         that an error has occurred
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_error_report.restype = int
ANOPP2.a2py_error_report.argtypes = [c_char_p, c_int, c_int, c_char_p]



# -----------------------------------------------------------------------------------------
# This clears the error registry of any errors.
# -----------------------------------------------------------------------------------------
# @result
#         An integer that indicates the success of the operation
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_error_clear.restype = int



# -----------------------------------------------------------------------------------------
# This returns the number of errors in the registry.
# -----------------------------------------------------------------------------------------
# @result
#         An integer indicating the number of errors in the registry or if negative
#         indicates that the operation was not successful
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_error_count.restype = int



# -----------------------------------------------------------------------------------------
# This prints a list of errors to the screen instead of the log file.
# -----------------------------------------------------------------------------------------
# @result
#         An integer indicating the success of the operation
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_error_print.restype = int



# -----------------------------------------------------------------------------------------
# Sets where the errors should be reported to, logfile, screen, network
# -----------------------------------------------------------------------------------------
# @param blnLogFile
#        Logical value indicating if the errors should be reported to the log file
# @param blnStdOut
#        Logical value indicating if the errors should be reported to the standard out
# @param blnNetwork
#        Logical value indicating if the errors should be reported to a blnNetwork
#        connection
# @result
#        An integer less than 0 that communciates failure of the code.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_error_outputs.restype = int
ANOPP2.a2py_error_outputs.argtypes = [c_bool, c_bool, c_bool]



# -----------------------------------------------------------------------------------------
# Sets the filename to write output to
# -----------------------------------------------------------------------------------------
# @result
#        An integer indicating the success of the operation
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_error_file.restype = int
ANOPP2.a2py_error_file.argtypes = [c_char_p]



#!/usr/bin/python
# ---------------------------------------------------------------------------------------
#  These are the standard error values included by the error module.  The calling
#  function uses these as input to the ANOPP2.function which logs the output to a .log
#  file.
# ---------------------------------------------------------------------------------------
#  


#  This is a standard error for a generic failure and is the error constants equivalent \
#   to -1
a2_error_operation_failed = 1

#  This is a standard error level for out of bounds. This is passed to the error \
#   function and written out to the log file.
a2_error_out_of_bounds = 2

#  This enumerator is for divide by zero. A divide by zero error is a common error that \
#   can be thrown by code that uses this module.
a2_error_divide_by_zero = 3

#  This enumerator communicates that an array that should not have been allocated or \
#   associated is allocated or assiciated
a2_error_already_allocated = 4

#  This error occurs when a select case is used with an invalid option.
a2_error_invalid_option = 5

#  This error is for a feature that should be implemented but is as of yet not.
a2_error_not_implemented = 6

#  This error is when 2 arrays that should be the same size are not the same size.
a2_error_array_size_mismatch = 7

#  This error occurs when a string that should contain data is empty
a2_error_empty_string = 8

#  This error occurs if a function, \
#   class or other code block is not ready to perform its task
a2_error_not_ready = 9

#  This error occurs when a namelist fails to be read properly
a2_error_namelist_read_failure = 10

#  This error occurs when an object is trying to be retrieved from a data structure \
#   manager but was not found.
a2_error_object_not_found = 11

#  This error is for failing to open a file.
a2_error_io_failure = 12

#  This warning occurs when atmosphere data and NPSS input data do not reference the \
#   same properties for an altitude.
a2_error_condition_mismatch = 13

#  This is the enumeration for an allocation failure.
a2_error_failed_allocation = 14

#  This is the enumeration for an deallocation failure.
a2_error_failed_deallocation = 15

#  This is an enumerator for a parallel problem.
a2_error_parallel_failure = 16

# -----------------------------------------------------------------------------------------
# The input/output API contains routines, enumerators, and constants for input and output.
# -----------------------------------------------------------------------------------------
#  @file ANOPP2.api.f90
#  @author The ANOPP2 Development Team
#  @version 1.0.0:
# -----------------------------------------------------------------------------------------



# =========================================================================================
#  Next part of this file contains hardcoded enumerators used by the user's program.
# =========================================================================================



# -----------------------------------------------------------------------------------------
#  These enumeration are for the output file format options.  They are communicated to
#  the Export function.  The Export function then writes out the information in
#  the specified file format.
# -----------------------------------------------------------------------------------------

# This is the enumeration of formatted file format 
a2_formatted = 1

# This is the enumeration of binary file format 
a2_binary = 2

# This is the enumeration for unformatted file format 
a2_unformatted = 3



# -----------------------------------------------------------------------------------------
#  This enumeration is for the program that will read the output file generated by the
#  Export function.  Options may include Tecplot or NetCDF.
# -----------------------------------------------------------------------------------------

# This is the enumeration of Tecplot formatted file 
a2_tecplot = 1

# This is the enumeration of NetCDF formatted file format 
a2_netcdf = 2



# -----------------------------------------------------------------------------------------
#  This file is the interface file for the Fortran subroutines in the memory management
#  Application Programming Interface (API).  These routines are used to deallocate memory
#  that has been allocated by any of the APIs within ANOPP2.  These are required because
#  when an ANOPP2 API allocated memory and the user then deallocates that memory, an
#  inconsistency may arise that would cause memory leaks.  When called thousands of times,
#  even a small memory leak can become a large problem.  Use these routines to ensure that
#  memory is consistent between ANOPP2's APIs and the user's User Code.  See 'Memory
#  Management' section of the API manual.
# -----------------------------------------------------------------------------------------
#  @file ANOPP2.api.py
#  @author The ANOPP2 Development Team
#  @version 1.0.0:
# -----------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------
#  The a2py_deallocate_int_ptr function deallocates an allocated integer array
#  pointed to by intArray.
# -----------------------------------------------------------------------------------------
#  @param intArray
#         One dimensional array of integer values
#  @result
#         An integer returned with zero indicating success and non-zero indicating an
#         error condition.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_mm_deallocate_int_ptr.restype = int
ANOPP2.a2py_mm_deallocate_int_ptr.argtypes = [POINTER(POINTER(c_int))]



# -----------------------------------------------------------------------------------------
#  The a2py_deallocate_float_ptr function deallocates an allocated real array pointed
#  to by fltArray.
# -----------------------------------------------------------------------------------------
#  @param fltArray
#         One dimensional array of real values
#  @result
#         An integer returned with zero indicating success and non-zero indicating an
#         error condition.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_mm_deallocate_float_ptr.restype = int
ANOPP2.a2py_mm_deallocate_float_ptr.argtypes = [POINTER(POINTER(c_float))]



# -----------------------------------------------------------------------------------------
#  The a2py_deallocate_char_ptr function deallocates an allocated character array pointed
#  to by strArray.
# -----------------------------------------------------------------------------------------
#  @param strArray
#         One dimensional array of characters
#  @result
#         An integer returned with zero indicating success and non-zero indicating an
#         error condition.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_mm_deallocate_char_ptr.restype = int
ANOPP2.a2py_mm_deallocate_char_ptr.argtypes = [POINTER(POINTER(c_char))]



# -----------------------------------------------------------------------------------------
#  The a2py_deallocate_bool_ptr function deallocates an allocated boolean array pointed
#  to by blnArray.
# -----------------------------------------------------------------------------------------
#  @param blnArray
#         One dimensional array of boolean values
#  @result
#         An integer returned with zero indicating success and non-zero indicating an
#         error condition.
# -----------------------------------------------------------------------------------------
ANOPP2.a2py_mm_deallocate_bool_ptr.restype = int
ANOPP2.a2py_mm_deallocate_bool_ptr.argtypes = [POINTER(POINTER(c_bool))]



