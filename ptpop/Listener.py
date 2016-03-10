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
    def __init__(self, intf=None):
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
        self.ptp_neighbors = dict()

        # Input Checks
        if intf:
            self._pcap = pcap.pcap(intf)
            # Thread - for every packet coming in 
            for ts, pkt in self._pcap:
                print str(ts) + ' ' + ':'.join('{:02x}'.format(ord(c)) for c in str(pkt[0:12]))
                pn = PtpNeighbor(pkt)
                ptp_neighbor_key = "%s:%d" % (pn.src_addr_str, pn.domain)
                try:
                    ptp_neighbor = self.ptp_neighbors[ptp_neighbor_key]
                    ptp_neighbor.new_announce_message(pn)
                except KeyError:
                    self.ptp_neighbors[ptp_neighbor_key] = pn


        # TODO When intf is defined, start listening to the interface,
        # and forward packets into the right PtpNeighbor in
        # self.ptp_neighbors as they come in.  That PtpNeighbor should
        # update info, including message periods.

        # init ...

    def readFromPcapFile(self, filename):
        pc = pcap.pcap(filename)
        for ts, pkt in pc:
            pn = PtpNeighbor(pkt)
            pn_key = "%s:%d" % (pn.src_addr_str, pn.domain)
            self.ptp_neighbors[pn_key] = pn

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

        ptp_neighbor_keys = iter(l.ptp_neighbors)
        for ptp_neighbor_key in ptp_neighbor_keys:
            actual = str(l.ptp_neighbors[ptp_neighbor_key])
            expected = str()
            if ptp_neighbor_key == '192.168.1.2:129':
                expected = '192.168.1.2     E2E  - 129 128   6 0x21 15652 128 001c73ffffb53519   -     -     -  '
            elif ptp_neighbor_key == '192.168.1.3:129':
                expected = '192.168.1.3     E2E  - 129 128   6 0x21 15652 128 001c73ffff1935b5   -     -     -  '
            elif ptp_neighbor_key == '192.168.1.4:129':
                expected = '192.168.1.4     E2E  - 129 128   6 0x21 15652 128 001c73ffff35b519   -     -     -  '
            else:
                self.fail(msg='Unknown key in ptp_neighbor_keys: ' +
                        ptp_neighbor_key)
            self.assertEqual(actual, expected)

    def test_listening_to_intf(self):
        l = Listener('lo')

        pcap_file = pcap.pcap('single_ptp_announce_packet_from_4_to_129.pcap')
        pc = pcap.pcap(name='lo')
        for ts, pkt in pcap_file:
            pc.sendpacket(str(pkt))

        ptp_neighbor_key = iter(l.ptp_neighbors)
        actual = str(l.ptp_neighbors[ptp_neighbor_key.next()])
        expected = "192.168.1.4     E2E  - 129 128   6 0x21 15652 128 001c73ffff35b519   -     -     -  "
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    # Test class
    unittest.main()
