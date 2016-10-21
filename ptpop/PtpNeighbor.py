#!/usr/local/bin/python
'''
PtpNeighbor Class
'''

import pcap
import re
import datetime
from AnnounceMessage import AnnounceMessage
from SyncMessage import SyncMessage

# =============================================================================
# PtpNeighbor
# 
# Inheriting from `object` (top-level class)
# =============================================================================
class PtpNeighbor(object):
    def __init__(self, pkt):
        '''
        PtpPacket Initialization

        Input Attributes:
        ------------------
        pkt: PTP Announce packet to derive PTP details of this neighbor
             from
        '''

        self._sync_period = None
        self._delay_period = None
        self._announce_period = None
        self._time_of_last_sync = 0
        self._time_of_last_delay = 0
        self._time_of_last_announce = 0
        self.new_announce_message(pkt)

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

    def new_announce_message(self, pkt):
        '''
        Take note of an announce message from this neighbor, to derive
        its periodicity
        '''
        msg = AnnounceMessage(pkt)
        self._update_announce_params(msg)
        now = datetime.datetime.now()
        if self._time_of_last_announce != 0:
            self._announce_period = (now - self._time_of_last_announce).total_seconds()
        self._time_of_last_announce = now

    def new_sync_message(self, pkt):
        '''
        Take note of a sync message from this neighbor, to derive the
        its periodicity
        '''
        msg = SyncMessage(pkt)
        now = datetime.datetime.now()
        if self._time_of_last_sync != 0:
            self._sync_period = (now - self._time_of_last_sync).total_seconds()
        self._time_of_last_sync = now


    def _update_announce_params(self, msg):
        '''
        Update all parameters for this neighbor using info. contained
        in the announce message
        '''
        # According to the pcap data, set this objects' properties
        self.src_addr_str = msg.ipv4_src_str
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

    def __str__(self):
        stats_str = str()
        stats_str += ( '%-15s' % self.src_addr_str ) if self.src_addr_str != None else ''
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

        stats_str += ( ' % 2.2f' % self.sync_period ) if self.sync_period != None else '   -  '
        stats_str += ( ' % 2.2f' % self.delay_period ) if self.delay_period != None else '   -  '
        stats_str += ( ' % 2.2f' % self.announce_period ) if self.announce_period != None else '   -  '
        return stats_str


#==============================================================================
# Class Test
#==============================================================================
import unittest
import time

class TestPtpNeighbor(unittest.TestCase):
    def test_new_from_pcap_file(self):
        pc = pcap.pcap('single_ptp_announce_packet.pcap')
        ts, pkt = pc.next()
        pn = PtpNeighbor(pkt)
        self.assertEqual(pn.src_addr_str, '192.168.1.2')
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

    def test_updating_announce_period(self):
        pc = pcap.pcap('single_ptp_announce_packet.pcap')
        ts, pkt = pc.next()
        pn = PtpNeighbor(pkt)
        self.assertIsNone(pn.announce_period)
        time.sleep(0.667)
        pc = pcap.pcap('single_ptp_announce_packet.pcap')
        ts, pkt = pc.next()
        pn.new_announce_message(pkt)
        self.assertIsNotNone(pn.announce_period)
        actual = str(pn)
        expected = "192.168.1.2     E2E  - 129 128   6 0x21 15652 128 001c73ffffb53519   -     -    0.67"
        self.assertEqual(actual, expected)

    def test_updating_sync_period(self):
        ann_pc = pcap.pcap('single_ptp_announce_packet.pcap')
        ts, pkt = ann_pc.next()
        pn = PtpNeighbor(pkt)
        self.assertIsNone(pn.sync_period)

        sync_pc = pcap.pcap('single_ptp_sync_packet.pcap')
        ts, pkt = sync_pc.next()
        pn.new_sync_message(pkt)
        time.sleep(0.333)
        sync_pc = pcap.pcap('single_ptp_sync_packet.pcap')
        ts, pkt = sync_pc.next()
        pn.new_sync_message(pkt)
        self.assertIsNotNone(pn.sync_period)
        actual = str(pn)
        expected = "192.168.1.2     E2E  - 129 128   6 0x21 15652 128 001c73ffffb53519  0.34   -     -  "
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    # Test class
    unittest.main()
