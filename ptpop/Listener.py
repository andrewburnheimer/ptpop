#!/usr/local/bin/python
'''
Listener Class
Informative Notes T.B.D...
'''
__version__ = '$Id$'
'''
To Do:
    -
'''

#import inspect

# =============================================================================
# Listener
# 
# Inheriting from `object` (top-level class)
# =============================================================================
class Listener(object):
    #def __init__(self, assign_input={}, *optional_value_input, **optional_dict_input):
    def __init__(self):
        '''
        Listener Initialization
        Keyword Arguments:
        ------------------
        T.B.D.

        Input Attributes:
        -----------------
        T.B.D.

        Additional Attributes:
        ----------------------
        T.B.D.

        '''

        # Default Values

        # Input Checks

        # init ...



    def ptp_neighbor_stats(self):
#       '''
#       Public Module
#       '''
        neighbors = list()
        # Inputs
        # Module Code
        # Output

#    def Public_Method(self):
#        '''
#        Private Module
#        '''
        # Inputs
        # Module Code
        # Output

#    def Public_Static_Method():

#    def Public_Class_Method(cls):


# =============================================================================
# Private Module Functions
# =============================================================================
#def __Private_Function(inputs):
#        '''
#        Private Function
#        '''
#        # Inputs
#        # Function code ...
#        return outputs

# =============================================================================
# Public Module Functions
# =============================================================================
#def Public_Function(inputs):
#        '''
#        Public Function
#        '''
#        # Inputs
#        # Function code ...
#        return outputs

#==============================================================================
# Class Test
#==============================================================================
import unittest

class TestListener(unittest.TestCase):
    def testMockReturn(self):
        None
#*100.100.100.102 E2E  2 255 255 255 255 255 255 aa-cd-ff 128.0 128.0 128.0
#*100.100.100.101 E2E  2 255 255 255 255 255 255 ab-cd-ff 128.0 128.0 128.0
#*100.100.100.100 E2E  2 255 255 255 255 255 255 ab-cd-ef 128.0 128.0 128.0
        #self.failUnlessRaises(VE, PtpNeighbor, arg)
        #self.assertEqual(PtpNeighbor.statMethod(0), string)

if __name__ == '__main__':
    # Test class
    unittest.main()
