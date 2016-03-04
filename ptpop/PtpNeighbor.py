#!/usr/local/bin/python
'''
PtpNeighbor Class
Informative Notes T.B.D...
'''
__version__ = '$Id$'
'''
To Do:
    -
'''

# =============================================================================
# PtpNeighbor
# 
# Inheriting from `object` (top-level class)
# =============================================================================
class PtpNeighbor(object):
    #def __init__(self, assign_input={}, *optional_value_input, **optional_dict_input):
    def __init__(self):
        '''
        Console Initialization
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
        self.src_addr = None
        self.delay_mode = None
        self.step_mode = None
        self.domain = None
        self.priority1 = None
        self.clock_class = None
        self.accuracy = None
        self.variance = None
        self.priority2 = None
        self.uniq_id = None
        self.sync_period = None
        self.delay_period = None
        self.announce_period = None


        # Default Values

        # Input Checks

        # init ...

#    def __Private_Method(self):
#       '''
#       Private Module
#       '''
        # Inputs
        # Module Code
        # Output

    def __str__(self):
        stats_str = str()
        stats_str += ( '%-15s' % self.src_addr ) if self.src_addr != None else ''
        stats_str += ( ' %3s' % self.delay_mode ) if self.delay_mode != None else ''
        stats_str += ( ' %2d' % self.step_mode ) if self.step_mode != None else ''
        stats_str += ( ' %3d' % self.domain ) if self.domain != None else ''
        stats_str += ( ' %3d' % self.priority1 ) if self.priority1 != None else ''
        stats_str += ( ' %3d' % self.clock_class ) if self.clock_class != None else ''
        stats_str += ( ' %3d' % self.accuracy ) if self.accuracy != None else ''
        stats_str += ( ' %3d' % self.variance ) if self.variance != None else ''
        stats_str += ( ' %3d' % self.priority2 ) if self.priority2 != None else ''
        stats_str += ( ' % 8s' % self.uniq_id[-8:] ) if self.uniq_id != None else ''
        stats_str += ( ' %.1f' % self.sync_period ) if self.sync_period != None else ''
        stats_str += ( ' %.1f' % self.delay_period ) if self.delay_period != None else ''
        stats_str += ( ' %.1f' % self.announce_period ) if self.announce_period != None else ''
        return stats_str

#    def Public_Method(self):
#        '''
#        Public Module
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

class TestPtpNeighbor(unittest.TestCase):
    def test_new_object(self):
        pn = PtpNeighbor()
        self.assertIsNone(pn.src_addr)
        self.assertIsNone(pn.delay_mode)
        self.assertIsNone(pn.step_mode)
        self.assertIsNone(pn.domain)
        self.assertIsNone(pn.priority1)
        self.assertIsNone(pn.clock_class)
        self.assertIsNone(pn.accuracy)
        self.assertIsNone(pn.variance)
        self.assertIsNone(pn.priority2)
        self.assertIsNone(pn.uniq_id)
        self.assertIsNone(pn.sync_period)
        self.assertIsNone(pn.delay_period)
        self.assertIsNone(pn.announce_period)

    @unittest.expectedFailure
    def test_mock_return(self):
        pn = PtpNeighbor()
#*100.100.100.100 E2E  2 255 255 255 255 255 255 ab-cd-ef 128.0 128.0 128.0
        self.assertEqual(pn.src_addr, '100.100.100.100')
        self.assertEqual(pn.delay_mode, 'E2E')
        self.assertEqual(pn.step_mode, 2)
        self.assertEqual(pn.domain, 255)
        self.assertEqual(pn.priority1, 255)
        self.assertEqual(pn.clock_class, 255)
        self.assertEqual(pn.accuracy, 255)
        self.assertEqual(pn.variance, 255)
        self.assertEqual(pn.priority2, 255)
        self.assertEqual(pn.uniq_id[-8:], 'ab-cd-ef')
        self.assertEqual(pn.sync_period, 128.0)
        self.assertEqual(pn.delay_period, 128.0)
        self.assertEqual(pn.announce_period, 128.0)

    def test_new_object_as_string(self):
        pn = PtpNeighbor()
        actual = str(pn)
        expected = ""
        self.assertEqual(actual, expected)

    @unittest.expectedFailure
    def test_mock_return_as_string(self):
        pn = PtpNeighbor()
        actual = str(pn)
        expected = "100.100.100.100 E2E  2 255 255 255 255 255 255 ab-cd-ef 128.0 128.0 128.0"
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    # Test class
    unittest.main()
