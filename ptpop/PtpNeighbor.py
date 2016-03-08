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

import pcap
import re
from AnnounceMessage import AnnounceMessage

# =============================================================================
# PtpNeighbor
# 
# Inheriting from `object` (top-level class)
# =============================================================================
class PtpNeighbor(object):
    #def __init__(self, assign_input={}, *optional_value_input, **optional_dict_input):

    def __init__(self, pkt):
        "Initialize PtpNeighbor from a PTP Announce packet"
        msg = AnnounceMessage(pkt)
        # According to the pcap data, set this objects' properties
        self.src_addr = msg.ipv4_src_str
        # Obliged to update delay_mode after P_Delay_Req received 
        self.delay_mode = "E2E"
        # Obliged to update step_mode after sync received 
        self.step_mode = None
        self.domain = msg.ipv4_dst % 256
        self.priority1 = msg.ptp_bmca_priority1
        self.clock_class = msg.ptp_bmca_gm_clock_class
        self.accuracy = msg.ptp_bmca_gm_clock_acc
        self.variance = msg.ptp_bmca_gm_clock_var
        self.priority2 = msg.ptp_bmca_priority2
        self.uniq_id = msg.ptp_clock_id
        # Obliged to update the period values after a few syncs are received
        self._sync_period = None
        self._delay_period = None
        self._announce_period = None

    @property
    def sync_period(self):
        """Get the latest calculated sync_period"""
        return self._sync_period

    @property
    def delay_period(self):
        """Get the latest calculated delay_period"""
        return self._delay_period

    @property
    def announce_period(self):
        """Get the latest calculated announce_period"""
        return self._announce_period

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
        stats_str += ( ' %2d' % self.step_mode ) if self.step_mode != None else '  -'
        stats_str += ( ' %3d' % self.domain ) if self.domain != None else ''
        stats_str += ( ' %3d' % self.priority1 ) if self.priority1 != None else ''
        stats_str += ( ' %3d' % self.clock_class ) if self.clock_class != None else ''
        stats_str += ( ' 0x%2x' % self.accuracy ) if self.accuracy != None else ''
        stats_str += ( ' %5d' % self.variance ) if self.variance != None else ''
        stats_str += ( ' %3d' % self.priority2 ) if self.priority2 != None else ''

        trimmed_uniq_id = str()
        exp = re.compile('0x([a-fA-F0-9]+)')
        if self.uniq_id != None:
            match = exp.findall(self.uniq_id)
            trimmed_uniq_id = match[0]
        stats_str += ( ' % 16s' % trimmed_uniq_id )

        stats_str += ( ' %.1f' % self.sync_period ) if self.sync_period != None else '   -  '
        stats_str += ( ' %.1f' % self.delay_period ) if self.delay_period != None else '   -  '
        stats_str += ( ' %.1f' % self.announce_period ) if self.announce_period != None else '   -  '
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
    def test_new_from_pcap_file(self):
        pc = pcap.pcap('single_ptp_announce_packet.pcap')
        ts, pkt = pc.next()
        pn = PtpNeighbor(pkt)
        self.assertEqual(pn.src_addr, '192.168.1.2')
        self.assertEqual(pn.delay_mode, 'E2E')
        self.assertIsNone(pn.step_mode)
        self.assertEqual(pn.domain, 129)
        self.assertEqual(pn.priority1, 128)
        self.assertEqual(pn.clock_class, 6)
        self.assertEqual(pn.accuracy, 33)
        self.assertEqual(pn.variance, 15652)
        self.assertEqual(pn.priority2, 128)
        self.assertEqual(pn.uniq_id, '0x001c73ffffb53519')
        self.assertIsNone(pn.sync_period)
        self.assertIsNone(pn.delay_period)
        self.assertIsNone(pn.announce_period)

    def test_pcap_file_object_as_string(self):
        pc = pcap.pcap('single_ptp_announce_packet.pcap')
        ts, pkt = pc.next()
        pn = PtpNeighbor(pkt)
        actual = str(pn)
        expected = "192.168.1.2     E2E  - 129 128   6 0x21 15652 128 001c73ffffb53519   -     -     -  "
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    # Test class
    unittest.main()
