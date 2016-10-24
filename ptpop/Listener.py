#!/usr/local/bin/python
'''
Listener Class
'''

import pcap
import thread
from PtpNeighbor import PtpNeighbor
from PtpPacket import PtpPacket

# =============================================================================
# Listener
# 
# Inheriting from `object` (top-level class)
# =============================================================================
class Listener(object):
    def __init__(self, intf=None):
        '''
        Listener Initialization

        Input Attributes:
        ------------------
        intf: network interface the listener should observe
        '''

        # Default Values
        self.ptp_neighbors = dict()

        # Input Checks
        if intf:
            self._pcap = pcap.pcap(name=intf)
            self._pcap.setfilter('dst port 319 or dst port 320')
            # UDP port 319: Sync, Delay_Req, Pdelay_Req, Pdelay_Resp
            # UDP port 320: Follow_Up, Delay_Resp, Pdelay_Resp_Follow_Up, Announce, Management, Signaling
            thread.start_new_thread(self._pcap.loop, (999, self._handle_received_packet))


    def read_from_pcap_file(self, filename):
        pc = pcap.pcap(filename)
        for ts, pkt in pc:
            pn = PtpNeighbor(pkt)
            pn_key = "%s:%d" % (pn.src_addr_str, pn.domain)
            self.ptp_neighbors[pn_key] = pn

    @classmethod
    def from_pcap_file(cls, filename):
        "Initialize Listener with packets read from a pcap"
        l = cls()
        l.read_from_pcap_file(filename)
        return l


# =============================================================================
# Private Module Functions
# =============================================================================
    def _handle_received_packet(self, timestamp, data):
        '''
        Interpret a packet observed on the network interface

        Keyword Arguments:
        ------------------
        #'''
        pp = PtpPacket(data)
        ptp_neighbor_key = "%s:%d" % (pp.src_addr_str, pp.domain)

        try:
            ptp_neighbor = self.ptp_neighbors[ptp_neighbor_key]
            if pp.ptp_control == 5:
                ptp_neighbor.new_announce_message(data)
            elif pp.ptp_control == 0:
                ptp_neighbor.new_sync_message(data)
        except KeyError:
            if pp.ptp_control == 5:
                self.ptp_neighbors[ptp_neighbor_key] = PtpNeighbor(data)


#==============================================================================
# Class Test
#==============================================================================
import unittest
import time

class TestListener(unittest.TestCase):
    def test_new_with_mock_data(self):
        l = Listener.from_pcap_file('single_ptp_announce_packet_from_2_to_129.pcap')
        l.read_from_pcap_file('single_ptp_announce_packet_from_3_to_129.pcap')
        l.read_from_pcap_file('single_ptp_announce_packet_from_4_to_129.pcap')

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

        # Cheap fix to the race condition
        time.sleep(0.1)
        ptp_neighbor_key = iter(l.ptp_neighbors)
        actual = str(l.ptp_neighbors[ptp_neighbor_key.next()])
        expected = "192.168.1.4     E2E  - 129 128   6 0x21 15652 128 001c73ffff35b519   -     -     -  "
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    # Test class
    unittest.main()
