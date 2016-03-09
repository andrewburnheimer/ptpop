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

import pcap
from PtpNeighbor import PtpNeighbor

# =============================================================================
# Listener
# 
# Inheriting from `object` (top-level class)
# =============================================================================
class Listener(object):
    #def __init__(self, assign_input={}, *optional_value_input, **optional_dict_input):
    def __init__(self, *intf):
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
        self.ptp_neighbors = list()

        # Input Checks
        # TODO When intf is defined, start listening to the interface,
        # and forward packets into the right PtpNeighbor in
        # self.ptp_neighbors as they come in.  That PtpNeighbor should
        # update info, including message periods.

        # init ...

    def readFromPcapFile(self, filename):
        pc = pcap.pcap(filename)
        for ts, pkt in pc:
            self.ptp_neighbors.append(PtpNeighbor(pkt))

    @classmethod
    def fromPcapfile(cls, filename):
        "Initialize Listener with packets read from a pcap"
        l = cls()
        l.readFromPcapFile(filename)
        return l

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
    def test_new_with_mock_data(self):
        l = Listener.fromPcapfile('single_ptp_announce_packet_from_2_to_129.pcap')
        l.readFromPcapFile('single_ptp_announce_packet_from_3_to_129.pcap')
        l.readFromPcapFile('single_ptp_announce_packet_from_4_to_129.pcap')

        stats = iter(l.ptp_neighbors)
        actual = str(stats.next())
        expected = "192.168.1.2     E2E  - 129 128   6 0x21 15652 128 001c73ffffb53519   -     -     -  "
        self.assertEqual(actual, expected)

        actual = str(stats.next())
        expected = "192.168.1.3     E2E  - 129 128   6 0x21 15652 128 001c73ffff1935b5   -     -     -  "
        self.assertEqual(actual, expected)

        actual = str(stats.next())
        expected = "192.168.1.4     E2E  - 129 128   6 0x21 15652 128 001c73ffff35b519   -     -     -  "
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    # Test class
    unittest.main()
