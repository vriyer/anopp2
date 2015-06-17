__all__ = ['Anopp2']

# Import the Component class from the OpenMDAO Main API.
from openmdao.main.api import Component

# Import Float class from the Datatypes library in OpenMDAO.
from openmdao.lib.datatypes.api import Float

# Import the OpenMDAO library components. We need to import the External Code.
from openmdao.lib.components.external_code import ExternalCode

# Import the FileParser and InputFileGeneration functions residing in Filewrap utility
# in OpenMDAO
from openmdao.util.filewrap import FileParser, InputFileGenerator

# Import the Float datatype defined in OpenMDAO library required in AOIC.
from openmdao.lib.datatypes.api import Float

# Import Numpy as np
import numpy as np

# Import the ANOPP2 API python interface.
from ANOPP2_api import *

# Import the ctypes.
from ctypes import *

# Import the OS.
import os

from openmdao.main.api import Assembly
#from openmdao.lib.drivers.api import SLSQPdriver

# Import the Constrained Optimizer driver from the OpenMDAO Optimizers library.
from openmdao.lib.drivers.api import CONMINdriver



#====================================================================================
# This is the Anopp2Component class that receives the External code. This class is 
# the crux of AOIC. This uses ANOPP2 function calls to perform various tasks for 
# predicting noise.  Details of these functions, their syntax, purpose, and usage are
# explained in several ANOPP2 Manuals.  Users of ANOPP2 in OpenMDAO are required to
# develop this Anopp2Component specific to their problem. 
#
# In this problem, the location of the Observer along a sideline parallel to the
# aircraft takeoff on the ground was determined at which the noise (Effective 
# Perceived Noise Levels (EPNL)) is maximum. This determination is made using 
# OpenMDAO by minimizing the reciprocal of the EPNL.
#====================================================================================
class Anopp2Component(ExternalCode):
  """
  All ANOPP2-capable components should be subclasses of Anopp2Component.
   
  By subclassing Anopp2Component, any component should have easy access to ANOPP2's
  subcomponents, such as Observer, FlightPath, etc.
  Refer to Documentation under Anopp2Component for additional information.
  """

  # This is the starting x location of the observer along the sideline, in terms of 
  # meters. This is set as 2,410 m, the origin being the location at which the flight
  # originates.
  x = Float(2410.0, iotype='in', desc='The variable along the direction of flight')
  
  # This is the inverse of the EpndB. This is the variable that will be optimized or
  # minimized.  This variable will be returned by this class.
  Epndb_inverse = Float(iotype='out', desc='The inverse of the EPNdB')

  # Tags for the Atmosphere and Flight Path Data Structures. Although these Data 
  # Structures will not be used in this demo, the variables are still required as 
  # input for the routine that creates the mission.
  intAtmosphereTag = c_int(0)
  intFlightPathTag = c_int(0)
  
  #  A tag for the observer, which will hold the noise results parsed from the ANOPP
  #  output.
  intObserverTag = c_int(0)
  
  # A tag for the Functional Module.  For this demonstration program the Funtional 
  # Module AnoppComplete will be used. A tag name must be declared as follows. This 
  # tag is set by the a2py_exec_create_functional_module routine call.
  intAnoppCompleteTag = c_int(0)
  
  # This is the number of input Data Structure tags that are required for the 
  # Functional Module.  In this case, for the AnoppComplete Functional Module there 
  # will be 0 inputs.
  nInputs = 0
  
  # This is the array of input Data Structure tags, which again, will be of size 0.
  intInputTags = (c_int * nInputs)()
  
  # This is the number of results from the Functional Module stored in the Observer.
  nResults = c_int(0)

  # An array of tags used to access the results in the Observer Data Structure. A 
  # pointer to this array is returned by the AnoppComplete Functional module.
  intResultTags = pointer(c_int(0))

  # ----------------------------------------------------------------------------------
  # Integers and arrays for holding the Functional Module tags and passing them into 
  # the Mission.  ANOPP2 has 2 types of Functional Modules: 'Time Series' or 'Single 
  # Time'. The AnoppComplete Functional Module is of type 'Time Series'. Even if a 
  # user is only utilizing one type of Functional Module, the definitions for arrays 
  # and parameters need to be provided to the mission for both types.
  #-----------------------------------------------------------------------------------

  # A tag for the mission, which defines which Function Modules are executed.
  intMissionTag = c_int(0)

  # The number of Time Series Functional Modules to be called in the mission.
  # For this demonstration there will be 1 (AnoppComplete Functional Module)
  nTimeSeriesFunctionalModules = 1

  # The array of Time Series functional module tags.  This is allocated to size 1
  # because there is 1 Time Series Functional Module in this prediction: the 
  # AnoppComplete Functional Module.
  intTimeSeriesFunctionalModulesTags = (c_int * nTimeSeriesFunctionalModules)()

  # Single Time definitions are set because the routine to create the mission requires
  # these arguments. This demonstration does not have any Single Time Functional 
  # Modules, therefore all these are set to null or zero values.

  # The number of source times for the Single Time Functional Module (time in the 
  # mission when specific functional modules are executed).  Since there is only a 
  # Time Series Functional Module, this is not used and is set to 0.
  nSourceTimes = 0

  # The maximum number of Single Time Functional Modules executed at a single source 
  # time. Since there are no Single Time Functional Modules defined in this 
  # demonstration, this is set to zero.
  nMaximumSingleTimeFunctionalModules = 0

  # A 2-dimensional array of Single Time Functional Module tags.  The first dimension 
  # is equal to the number of source times, the second is equal to the max number of 
  # Functional Modules executed per source time.  These are both zero since this 
  # demonstration does not have any Single Time Functional Modules
  intSingleTimeFunctionalModuleTags = pointer(c_int(0))

  # An array to store the source times.  These can be retrieved from the Flight Path 
  # API after the Flight Path is created.  However, since there are no Single Time
  # Functional Modules, this is allocated to size zero (nSourceTimes is 0).
  fltSourceTimes = pointer(c_float(0))

  # ----------------------------------------------------------------------------------
  # An integer success value.  This integer is returned from ANOPP2 API routine calls 
  # to communicate the state of a given operation.  A return of 0 means success, 
  # anything other than 0 indicates failure. Note the code execution does not depend 
  # on this value, hence it is left to the user to check for success and take 
  # appropriate action.
  # ----------------------------------------------------------------------------------
  intSuccess = c_int(0)
    
  # This is the number of nodes existing in the Observer.
  nNodes = c_int(0)

  # This is the Epnl corresponding to this node.
  fltEpnl = c_float(-300.0)
  
  # This is the Duration factor determined while calculating EPNL.
  fltD = c_float(0)
  
  # This is the minimum and maximum time of the EPNL integration.
  fltTimeRange = (c_float * 2)(*[0.0, 0.0])
  
  # This is an array of the position of the last node in the Observer Point Cloud.
  fltPosition = (c_float * 3)(*[0.0, 0.0, 0.0])
  

    
  #===================================================================================
  # The Anopp2Component is initialized in this function. Several local variables are 
  # also initialized. An Observer is created based on the details provided in 
  # observer.config. 
  #===================================================================================
  def __init__ (self):
    """ Initialize the Anopp2 class.
    """
    super(Anopp2Component, self).__init__()

    #=================================================================================
    # Step 1.
    # The ANOPP2 API must be initialized before any of the routines can be executed 
    # and should have false as it's argument.
    #=================================================================================
    ANOPP2.a2py_exec_init_api ()

    #=================================================================================
    # Step 2.
    # Create the necessary Data Structures required by the Anopp Complete Functional 
    # Module. Set the tag numbers to zero for the Data Structures that ANOPP will 
    # generate internally when it is executed.  This are necessary becuase the 
    # variables are requried in the definition of the routine that creates the 
    # mission. The Observer must be given to the Functional Module, so it must be 
    # created from a configuration file.
    #=================================================================================
    self.intAtmosphereTag = 0
    self.intFlightPathTag = 0

    #=================================================================================
    # Step 3.
    # Construct an observer point (only a single point is used for serial execution) 
    # from a configuration file.  This is done by using the create function of the 
    # Observer API and passing a blank observer tag and the file name.  The necessary
    #  configuration file accompanies this demonstrator..
    #=================================================================================
    intSuccess =             \
      ANOPP2.a2py_obs_create \
       (pointer(self.intObserverTag), create_string_buffer (b"observer.config"))



  #===================================================================================
  # The execute function gets executed by OpenMDAO repeatedly until the specified
  # exit criteria are met. The steps followed in this function are:
  #   1. Obtain the number of nodes available in the observer.
  #   2. Obtain the position vector of the lsat node in the observer.
  #   3. Replace the x-coordinate of this position vector with that provided by the
  #      OpenMDAO optimizer.
  #   4. Insert a new node in the observer with a position vector as defined through
  #      steps 2 through 4.
  #   5. Create an AnoppComplete Functional Module based on the config file,
  #      "AnoppComplete.config".
  #   6. Create a mission for running AnoppComplete functional module and executing 
  #      ANOPP to obtain noise due to Jet, Inlet, Aft Fan, Core, Gear, Flap, and 
  #      Trailing edge are all added to obtain the total noise. This noise is then
  #      propagated to the ground observer.
  #   7. Execute the mission to obtain the total noise on the ground observer.
  #   8. Obtain the number of results in the Observer.
  #   9. Obtain the number of nodes in the Observer.
  #  10. Calculate the EPNL from the acoustic data predicted by the AnoppComplete
  #      functional module.
  #  11. Get the EPNL value of the last node.
  #  12. If the EPNL value is valid, get its inverse. The inverse of the EPNL is 
  #      numerically small. Multiply it with 1000 and treat this as EpndB_inverse.
  #  13. Export the results to a Tecplot-friendly file.
  #  14. Delete the results because we do not need it any more.
  #===================================================================================
  def execute(self):
    """ Obtain a given Observer location, find the noise at that location. Use such 
    noise values to optimize and locate the Observer location that has the maximum 
    noise.
    """
       
    #=================================================================================
    # Step 4. We need to introduce a new node at a location provided by the optimizer.
    # To do that, we need to first find the location of the last node in the observer, 
    # replace the x coordinate of this node location with that provided by the 
    # optimizer, and then introduce it as a new node in the point cloud.
    #=================================================================================

    # Get the number of nodes in the Observer.
    intSuccess = ANOPP2.a2py_obs_number_of_nodes (self.intObserverTag, self.nNodes)
    
    # Get the coordinates of the last node.
    intSuccess =               \
      ANOPP2.a2py_obs_position \
        (self.intObserverTag, self.nNodes, 0.0, a2_global, self.fltPosition)
        
    # Replace the x coordinates of this array with that from the class. Rest of the 
    # coordinates remain the same.
    self.fltPosition[0] = self.x
    
    # Insert a new node to the Point Cloud in the Observer.
    intSuccess = ANOPP2.a2py_obs_new_node (self.intObserverTag, self.fltPosition)

    #=================================================================================
    # Step 5.
    # Create the AnoppComplete Functional Module.
    #=================================================================================
    
    # Create the AnoppComplete Functional Module by passing an empty tag number (to be
    # filled), the configuration file name, the number of inputs, the list of Data 
    # structure Tags, a pointer to the Observer tag, the number of results, and a 
    # pointer to the array of result tags. The number of results and the result tags 
    # are returned from the create function and can be used to later access the data 
    # stored in the Observer Data Structure.
    intSuccess =                                                                 \
      ANOPP2.a2py_exec_create_functional_module                                  \
       (pointer(self.intAnoppCompleteTag),                                       \
        create_string_buffer (b"AnoppComplete.config"), self.nInputs,            \
        self.intInputTags, pointer(self.intObserverTag), pointer(self.nResults), \
        pointer(self.intResultTags))

    #=================================================================================
    # Step 6.
    # Create the Mission.  The Mission is the definition of what Functional Modules 
    # will be executed. In this example, only the AnoppComplete Functional Module will
    # be executed for all time.
    #=================================================================================

    # Since the only Time Series Functional Module being used is AnoppComplete, assign
    # it to the first and only index of the array (if there was a second Time Series 
    # Functional Module, it would be assigned to the second index of the array).
    self.intTimeSeriesFunctionalModulesTags [0] = self.intAnoppCompleteTag

    # To create a mission, each Functional Module tag must be added to the Mission 
    # according to its type placed in arrays of the appropriate structure.  If Single 
    # Time Functional Modules exist, then their tags would be placed into a two 
    # dimensional array corresponding to waypoints and number of Single Time 
    # Functional Modules. Time Series Functional Modules have their tags placed in a 
    # one dimensional array. The routine to create a Mission also requires the 
    # waypoint times, and the Atmosphere and Flight Path tags, regardless of  whether 
    # they are being used. In this case they are not, so their values are set to zero.
    # Note: This demonstration program has only one Functional Module: AnoppComplete. 
    # This is a Time Series Functional Module and therefore, all Single Time 
    # Functional Module inputs are left empty.  The only reason they are needed is 
    # because the a2py_exec_create_mission requires them.
    intSuccess =                                                                     \
      ANOPP2.a2py_exec_create_mission                                                \
       (pointer(self.intMissionTag), create_string_buffer (b""),                     \
        self.intAtmosphereTag, self.intFlightPathTag, self.nSourceTimes,             \
        self.nMaximumSingleTimeFunctionalModules, self.nTimeSeriesFunctionalModules, \
        self.fltSourceTimes, self.intSingleTimeFunctionalModuleTags,                 \
        self.intTimeSeriesFunctionalModulesTags)

    #=================================================================================
    # Step 7.
    # Execute the Mission.  The Mission performs the noise prediction.  This call 
    # tells the Mission to execute all Functional Modules at the time specified. This 
    # will in turn execute ANOPP, producing a fort.4 that will be renamed to the 
    # output specified in the configuration file
    #=================================================================================

    #  Call the routine that executes the Mission
    intSuccess = ANOPP2.a2py_exec_execute_mission (self.intMissionTag)
    
    # Get the number of results in the Observer.
    intSuccess = \
      ANOPP2.a2py_obs_number_of_results (self.intObserverTag, self.nResults)

    #=================================================================================
    # Step 8.
    # Calculate metrics and report the results. After the Mission is executed, the 
    # Observer Data Structure contains the prediction results. These results can be 
    # accessed to calculate derived metrics and reported to an external file using 
    # Observer API routine calls.  To calculate metrics, the Observer API provides 
    # specific acoustic analysis functionality that can be invoked via input 
    # enumerators.  A list of the enumerators available for the Observer API routines 
    # can be found in the Observer API User's Manual.
    #=================================================================================
       
    # Get the number of nodes in the Observer.
    intSuccess = ANOPP2.a2py_obs_number_of_nodes (self.intObserverTag, self.nNodes)

    # The first step is to calculate any derived metrics. For this demonstrator, EPNL 
    # is calculated. The first argument in the call is the observer tag. The second 
    # argument is the array containing the result tags associated with the observer
    # locations.  In this case there are three results, Engine, Airframe, and Total. 
    # The third argument is an enumerator for what noise metric will be calculated and
    # returned by this call. For this demonstration the metric is EPNL. The last 
    # argument is an enumerator that tells the Observer API that the EPNL has to be'
    # calculated based on the complete time history.  This is defined by the 
    # enumerator, a2_obs_complete.
    intSuccess =                                                                  \
      ANOPP2.a2py_obs_calc_metric                                                 \
       (self.intObserverTag, self.nResults.value, self.intResultTags, a2_aa_epnl, \
        a2_obs_complete)

    # Get the EPNL value for the last node which is the node that was inserted into 
    # the Observer.
    intSuccess =                                                        \
      ANOPP2.a2py_obs_get_epnl                                          \
        (self.intObserverTag, self.intResultTags[0], self.nNodes.value, \
         self.fltEpnl, self.fltD, self.fltTimeRange)
    
    # Ensure that the EPNL obtained from the Observer is greater than zero and is not 
    # none.
    if (self.fltEpnl is not None) and (self.fltEpnl.value > 0.0):

      # Set the Epndb inverse as the reciprocal of the Epndb.
      self.Epndb_inverse = 1000.0/float(self.fltEpnl.value)

    # Print the Location and the EPNL values to the screen.
    print ("Location: ", self.fltPosition[0])
    print ("EPNL: ", self.fltEpnl.value)
    
    # Set the Output file name for exporting the EPNL to a file.
    self.strOutputFile = "Epnl.out.dat"
    
    # Export the result to a file.
    intSuccess =                                                                 \
      ANOPP2.a2py_obs_export                                                     \
        (self.intObserverTag, self.intResultTags[0],                             \
         create_string_buffer(bytes(self.strOutputFile)), a2_aa_epnl, a2_global, \
         a2_formatted, a2_tecplot)
    
    # Delete the results because we don't need them any more.
    intSuccess =                     \
      ANOPP2.a2py_obs_delete_results \
        (self.intObserverTag, self.nResults.value, self.intResultTags, 0)



#====================================================================================
# This class contains the optimizer. It defines the design variable (the variable 
# that has to be varied) and the parameter to be minimized (Epndb_inverse) and calls 
# the Anopp2Component class repeatedly. It also specifies the driver to be used for
# optimization and the criteria for optimizing and exiting the optimization.
# This class performs the following steps:
#   1. It adds the Driver to be used and assigns a name to it. Two drivers have been 
#      tried out: SLSQPdriver and CONMINdriver.
#   2. It adds the Anopp2Component class and assigns a name to it.
#   3. It adds this Anopp2Component to the Workflow of the driver.
#   4. It specifies the interval to display the optimization details.
#   5. It then adds the Objective variable and the parameter variable to be minimed.
#   6. Depending on the driver chosen it specifies the set of parameters for 
#      optimization. 
#====================================================================================
class Anopp2Optimize(Assembly):
  """Unconstrained Optimization to locate the Observer location corresponding to 
  maximum EpndB"""



  def configure(self):
    
    # Create an optimizer instance (Uncomment the following statement if SLSQP driver 
    # is to be used, and comment the next statement.
#    self.add('driver', SLSQPdriver())
    self.add('driver', CONMINdriver())
    
    # Create Anopp2 component instance.
    self.add('anopp2', Anopp2Component())
    
    # Iteration hierarchy
    self.driver.workflow.add('anopp2')
    
    # SLSQP Flags
    self.driver.iprint = 1
    
    # Objective
    self.driver.add_objective('anopp2.Epndb_inverse')
    
    # Design variable
    self.driver.add_parameter('anopp2.x', low=2400., high=3500.0)
    
    # Set the SLSQP-specific settings. Uncomment the following if SLSQP Driver is to
    # be used.
#    self.driver.accuracy = 1.0e-08
#    self.driver.maxiter = 50
    
    # Set the CONMIN-specific settings. Comment the following if SLSQP Driver is to be
    # used.
    self.driver.itmax = 30
    self.driver.fdch = 0.001
    self.driver.fdchm = 0.0001
    self.driver.ctlmin = 0.01
    self.driver.delfun = 0.01
    self.driver.conmin_diff = True
    self.iIteration = 0
        
