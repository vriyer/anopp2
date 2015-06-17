#====================================================================================
# This program is a unit test that tests the Anopp2 optimization problem.
#====================================================================================

# Import the unittest module/class.
import unittest

# Import set_as_top from the OpenMDAO Main API.
from openmdao.main.api import set_as_top

# Import Anopp2Optimize class from the anopp2 folder.
from anopp2.anopp2 import Anopp2Optimize



#====================================================================================
# This class runs the unit tests that in turn tests the Anopp2 Optimization problem.
#====================================================================================
class Anopp2TestCase(unittest.TestCase):

  # There is nothing to setup here.
  def setUp(self):
    pass
        
  # There is nothing to teardown here.
  def tearDown(self):
    pass
        
  # This function tests the ANOPP2 component.
  def test_Anopp2(self):
    
    # Import the time module so we can assess the time taken to run this test.
    import time
  
    # This is the iteration number.
    iIteration = 0
  
    # This is the increment in x that we want to jump to determine a local maximum.
    fltdelta_x = 100.0
      
    # Set the current optimization problem as ANOPP2 Optimize.
    opt_problem = Anopp2Optimize()
    
    # Run the set_as_top function for the Anopp2 Optimize problem.
    set_as_top(opt_problem)
  
    # Set the time as tt.
    tt = time.time()

    # Execute the Anopp2Optimize
    opt_problem.run()

    # Write messages on the screen when a maximum noise is found.  
    print "\n"
    print "Local Maximum found at (%f)" % opt_problem.anopp2.x
    print "EPNdB at this maximum (%f)" % opt_problem.anopp2.fltEpnl.value
    print "Elapsed time: ", time.time()-tt, "seconds"
        
if __name__ == "__main__":
    unittest.main()
    
