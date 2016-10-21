#!/usr/local/bin/python
'''
AnnounceMessage Class
'''

import struct

# =============================================================================
# AnnounceMessage
# 
# Inheriting from `object` (top-level class)
# =============================================================================
class AnnounceMessage(object):
    ENET_DST_LEN = 6
    ENET_SRC_LEN = 6
    ENET_TYPE_LEN = 2

    IPV4_VER_LEN = 1
    IPV4_DIFF_SERV_LEN = 1
    IPV4_TOTAL_LEN = 2
    IPV4_ID_LEN = 2
    IPV4_FLAGS_OFFSET_LEN = 2
    IPV4_TTL_LEN = 1

    IPV4_PROTOCOL_LEN = 1
    IPV4_HDR_CHKSUM_LEN = 2
    IPV4_SRC_LEN = 4
    IPV4_DST_LEN = 4

    UDP_SRC_LEN = 2
    UDP_DST_LEN = 2
    UDP_LEN_LEN = 2
    UDP_CHKSUM_LEN = 2

    PTP_MESSAGE_FLAGS = 2
    PTP_MESSAGE_LEN = 2
    PTP_SUBDOMAIN = 1
    # 1 byte padding
    PTP_FLAGS = 2
    PTP_CORRECTION = 8

    # 4 bytes padding 
    PTP_CLOCK_ID = 8
    PTP_SOURCE_PORT_ID = 2
    PTP_SEQ_ID = 2
    PTP_CONTROL = 1
    PTP_LOG_MESSAGE_PER = 1
    PTP_ORIGIN_TIMESTAMP_S = 6
    PTP_ORIGIN_TIMESTAMP_NS = 4
    PTP_ORIGIN_CURRENT_UTC_OFFSET = 2

    # 1 byte padding
    PTP_BMCA_PRIORITY1 = 1
    PTP_BMCA_GM_CLOCK_CLASS = 1
    PTP_BMCA_GM_CLOCK_ACC = 1
    PTP_BMCA_GM_CLOCK_VAR = 2
    PTP_BMCA_PRIORITY2 = 1
    PTP_BMCA_GM_CLOCK_ID = 8
    PTP_LOCAL_STEPS_REMOVED = 2
    PTP_TIME_SOURCE = 1

    def __init__(self, bffr):
        '''
        AnnounceMessage Initialization

        Input Attributes:
        ------------------
        bffr: captured packet string to decode
        '''

        cursor = 0

        self.enet_dst, = struct.unpack(">Q", '\x00\x00' + bffr[cursor:cursor + self.ENET_DST_LEN])
        self.enet_dst_str = self._Binary_MAC_to_String(bffr[cursor:cursor + self.ENET_DST_LEN])
        cursor += self.ENET_DST_LEN

        self.enet_src, = struct.unpack(">Q", '\x00\x00' + bffr[cursor:cursor + self.ENET_SRC_LEN])
        self.enet_src_str = self._Binary_MAC_to_String(bffr[cursor:cursor + self.ENET_SRC_LEN])
        cursor += self.ENET_SRC_LEN

        self.enet_type = self._Binary_Repr(bffr[cursor:cursor + self.ENET_TYPE_LEN])
        cursor += self.ENET_TYPE_LEN

        self.ipv4_ver = 0
        self.ipv4_hdr_len = 0
        ipv4_ver = bffr[cursor:cursor + self.IPV4_VER_LEN]
        if ipv4_ver.encode("hex") == b'45':
            self.ipv4_ver = 4
            self.ipv4_hdr_len = 20
        cursor += self.IPV4_VER_LEN


        self.ipv4_diff_serv = self._Binary_Repr(bffr[cursor:cursor + self.IPV4_DIFF_SERV_LEN])
        cursor += self.IPV4_DIFF_SERV_LEN

        self.ipv4_total_len, = struct.unpack(">H", bffr[cursor:cursor + self.IPV4_TOTAL_LEN])
        cursor += self.IPV4_TOTAL_LEN

        self.ipv4_id, = struct.unpack(">H", bffr[cursor:cursor + self.IPV4_ID_LEN])
        cursor += self.IPV4_ID_LEN

        self.ipv4_flags_offset = self._Binary_Repr(bffr[cursor:cursor + self.IPV4_FLAGS_OFFSET_LEN])
        cursor += self.IPV4_FLAGS_OFFSET_LEN

        self.ipv4_ttl, = struct.unpack(">B", bffr[cursor:cursor + self.IPV4_TTL_LEN])
        cursor += self.IPV4_TTL_LEN

        self.ipv4_protocol, = struct.unpack(">B", bffr[cursor:cursor + self.IPV4_PROTOCOL_LEN])
        cursor += self.IPV4_PROTOCOL_LEN

        self.ipv4_hdr_chksum = self._Binary_Repr(bffr[cursor:cursor + self.IPV4_HDR_CHKSUM_LEN])
        cursor += self.IPV4_HDR_CHKSUM_LEN

        self.ipv4_src, = struct.unpack(">L", bffr[cursor:cursor + self.IPV4_SRC_LEN])
        self.ipv4_src_str = self._Binary_IPV4_to_String(bffr[cursor:cursor + self.IPV4_SRC_LEN])
        cursor += self.IPV4_SRC_LEN

        self.ipv4_dst, = struct.unpack(">L", bffr[cursor:cursor + self.IPV4_DST_LEN])
        self.ipv4_dst_str = self._Binary_IPV4_to_String(bffr[cursor:cursor + self.IPV4_DST_LEN])
        cursor += self.IPV4_DST_LEN


        self.udp_src, = struct.unpack(">H", bffr[cursor:cursor + self.UDP_SRC_LEN])
        cursor += self.UDP_SRC_LEN

        self.udp_dst, = struct.unpack(">H", bffr[cursor:cursor + self.UDP_DST_LEN])
        cursor += self.UDP_DST_LEN

        self.udp_len, = struct.unpack(">H", bffr[cursor:cursor + self.UDP_LEN_LEN])
        cursor += self.UDP_LEN_LEN

        self.udp_chksum = self._Binary_Repr(bffr[cursor:cursor + self.UDP_CHKSUM_LEN])
        cursor += self.UDP_CHKSUM_LEN


        self.ptp_message_flags = self._Binary_Repr(bffr[cursor:cursor + self.PTP_MESSAGE_FLAGS])
        cursor += self.PTP_MESSAGE_FLAGS

        self.ptp_message_len, = struct.unpack(">H", bffr[cursor:cursor + self.PTP_MESSAGE_LEN])
        cursor += self.PTP_MESSAGE_LEN

        self.ptp_subdomain, = struct.unpack(">B", bffr[cursor:cursor + self.PTP_SUBDOMAIN])
        cursor += self.PTP_SUBDOMAIN

        cursor += 1 # padding

        self.ptp_flags = self._Binary_Repr(bffr[cursor:cursor + self.PTP_FLAGS])
        cursor += self.PTP_FLAGS

        self.ptp_correction = self._Binary_Repr(bffr[cursor:cursor + self.PTP_CORRECTION])
        cursor += self.PTP_CORRECTION


        cursor += 4 # padding

        self.ptp_clock_id = self._Binary_Repr(bffr[cursor:cursor + self.PTP_CLOCK_ID])
        cursor += self.PTP_CLOCK_ID

        self.ptp_source_port_id, = struct.unpack(">H", bffr[cursor:cursor + self.PTP_SOURCE_PORT_ID])
        cursor += self.PTP_SOURCE_PORT_ID

        self.ptp_seq_id, = struct.unpack(">H", bffr[cursor:cursor + self.PTP_SEQ_ID])
        cursor += self.PTP_SEQ_ID

        self.ptp_control, = struct.unpack(">B", bffr[cursor:cursor + self.PTP_CONTROL])
        cursor += self.PTP_CONTROL

        self.ptp_log_message_per, = struct.unpack(">B", bffr[cursor:cursor + self.PTP_LOG_MESSAGE_PER])
        cursor += self.PTP_LOG_MESSAGE_PER

        self.ptp_origin_timestamp_s = self._Binary_Repr(bffr[cursor:cursor + self.PTP_ORIGIN_TIMESTAMP_S])
        cursor += self.PTP_ORIGIN_TIMESTAMP_S

        self.ptp_origin_timestamp_ns = self._Binary_Repr(bffr[cursor:cursor + self.PTP_ORIGIN_TIMESTAMP_NS])
        cursor += self.PTP_ORIGIN_TIMESTAMP_NS

        self.ptp_origin_current_utc_offset, = struct.unpack(">H", bffr[cursor:cursor + self.PTP_ORIGIN_CURRENT_UTC_OFFSET])
        cursor += self.PTP_ORIGIN_CURRENT_UTC_OFFSET


        cursor += 1 # padding

        self.ptp_bmca_priority1, = struct.unpack(">B", bffr[cursor:cursor + self.PTP_BMCA_PRIORITY1])
        cursor += self.PTP_BMCA_PRIORITY1

        self.ptp_bmca_gm_clock_class, = struct.unpack(">B", bffr[cursor:cursor + self.PTP_BMCA_GM_CLOCK_CLASS])
        cursor += self.PTP_BMCA_GM_CLOCK_CLASS

        self.ptp_bmca_gm_clock_acc, = struct.unpack(">B", bffr[cursor:cursor + self.PTP_BMCA_GM_CLOCK_ACC])
        cursor += self.PTP_BMCA_GM_CLOCK_ACC

        self.ptp_bmca_gm_clock_var, = struct.unpack(">H", bffr[cursor:cursor + self.PTP_BMCA_GM_CLOCK_VAR])
        cursor += self.PTP_BMCA_GM_CLOCK_VAR

        self.ptp_bmca_priority2, = struct.unpack(">B", bffr[cursor:cursor + self.PTP_BMCA_PRIORITY2])
        cursor += self.PTP_BMCA_PRIORITY2

        self.ptp_bmca_gm_clock_id = self._Binary_Repr(bffr[cursor:cursor + self.PTP_BMCA_GM_CLOCK_ID])
        cursor += self.PTP_BMCA_GM_CLOCK_ID

        self.ptp_local_steps_removed, = struct.unpack(">H", bffr[cursor:cursor + self.PTP_LOCAL_STEPS_REMOVED])
        cursor += self.PTP_LOCAL_STEPS_REMOVED

        self.ptp_time_source = self._Binary_Repr(bffr[cursor:cursor + self.PTP_TIME_SOURCE])
        cursor += self.PTP_TIME_SOURCE


    def _Binary_MAC_to_String(self, bin_data):
        return "%02x:%02x:%02x:%02x:%02x:%02x" % struct.unpack("BBBBBB",bin_data)

    def _Binary_Repr(self, bin_data):
        ret_str = str()
        ret_str += "0x"
        for byte in bin_data:
            ret_str += "%02x" % struct.unpack("B", byte)
        return ret_str

    def _Binary_IPV4_to_String(self, bin_data):
        return "%d.%d.%d.%d" % struct.unpack("BBBB",bin_data)


    def __str__(self):
        stats_str = str()
        stats_str += '<ptp announce ID: '
        stats_str += self.ptp_clock_id + ' '
        stats_str += self.ipv4_src_str + ' -> '
        stats_str += self.ipv4_dst_str + ' seq: '
        stats_str += str(self.ptp_seq_id) + '>'
        return stats_str


#==============================================================================
# Class Test
#==============================================================================
import pcap
import unittest

class TestAnnounceMessage(unittest.TestCase):
    def test_new_from_pcap_file(self):
        pc = pcap.pcap('single_ptp_announce_packet.pcap')
        ts, pkt = pc.next()
        am = AnnounceMessage(pkt)
        self.assertEqual(am.enet_dst, int('01005e000181', 16))
        self.assertEqual(am.enet_dst_str, '01:00:5e:00:01:81')
        self.assertEqual(am.enet_src, int('001c73b5351d', 16))
        self.assertEqual(am.enet_src_str, '00:1c:73:b5:35:1d')
        self.assertEqual(am.enet_type, '0x0800')

        self.assertEqual(am.ipv4_ver, 4)
        self.assertEqual(am.ipv4_hdr_len, 20)
        self.assertEqual(am.ipv4_diff_serv, '0x00')
        self.assertEqual(am.ipv4_total_len, 92)
        self.assertEqual(am.ipv4_id, 0)
        self.assertEqual(am.ipv4_flags_offset, '0x0000')
        self.assertEqual(am.ipv4_ttl, 1)
        self.assertEqual(am.ipv4_protocol, 17)
        self.assertEqual(am.ipv4_hdr_chksum, '0x1666')
        self.assertEqual(am.ipv4_src, int('c0a80102', 16))
        self.assertEqual(am.ipv4_src_str, '192.168.1.2')
        self.assertEqual(am.ipv4_dst, int('e0000181', 16))
        self.assertEqual(am.ipv4_dst_str, '224.0.1.129')

        self.assertEqual(am.udp_src, 320)
        self.assertEqual(am.udp_dst, 320)
        self.assertEqual(am.udp_len, 72)
        self.assertEqual(am.udp_chksum, '0x762a')

        self.assertEqual(am.ptp_message_flags, '0x0b02')
        self.assertEqual(am.ptp_message_len, 64)
        self.assertEqual(am.ptp_subdomain, 0)
        self.assertEqual(am.ptp_flags, '0x003c')
        self.assertEqual(am.ptp_correction, '0x0000000000000000')
        self.assertEqual(am.ptp_clock_id, '0x001c73ffffb53519')

        self.assertEqual(am.ptp_source_port_id, 4)
        self.assertEqual(am.ptp_seq_id, 20561)
        self.assertEqual(am.ptp_control, 5)
        self.assertEqual(am.ptp_log_message_per, 0)
        self.assertEqual(am.ptp_origin_timestamp_s, '0x000000000000')
        self.assertEqual(am.ptp_origin_timestamp_ns, '0x00000000')
        self.assertEqual(am.ptp_origin_current_utc_offset, 36)

        self.assertEqual(am.ptp_bmca_priority1, 128)
        self.assertEqual(am.ptp_bmca_gm_clock_class, 6)
        self.assertEqual(am.ptp_bmca_gm_clock_acc, 33)
        self.assertEqual(am.ptp_bmca_gm_clock_var, 15652)
        self.assertEqual(am.ptp_bmca_priority2, 128)
        self.assertEqual(am.ptp_bmca_gm_clock_id, '0x080011fffe21a7f3')
        self.assertEqual(am.ptp_local_steps_removed, 1)
        self.assertEqual(am.ptp_time_source, '0x20')

    def test_str_from_pcap_file(self):
        pc = pcap.pcap('single_ptp_announce_packet.pcap')
        ts, pkt = pc.next()
        actual = str(AnnounceMessage(pkt))
        expected = '<ptp announce ID: 0x001c73ffffb53519 192.168.1.2 -> 224.0.1.129 seq: 20561>'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    # Test class
    unittest.main()
