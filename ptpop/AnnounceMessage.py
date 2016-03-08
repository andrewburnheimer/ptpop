#!/usr/local/bin/python
'''
AnnounceMessage Class
Informative Notes T.B.D...
'''
__version__ = '$Id$'
'''
To Do:
    -
'''

import pcap
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
    IPV4_DIFF_SERV = 1
    IPV4_TOTAL_LEN = 2
    IPV4_ID = 2
    IPV4_FLAGS_OFFSET = 2

    def __init__(self, bffr):
        "Initialize a AnnounceMessage"
        cursor = 0
        self.enet_dst = self.__Binary_MAC_to_String(bffr[cursor:cursor + self.ENET_DST_LEN])
        cursor += self.ENET_DST_LEN
        self.enet_src = self.__Binary_MAC_to_String(bffr[cursor:cursor + self.ENET_SRC_LEN])
        cursor += self.ENET_SRC_LEN
        self.enet_type = self.__Binary_Repr(bffr[cursor:cursor + self.ENET_TYPE_LEN])
        cursor += self.ENET_TYPE_LEN

        self.ipv4_ver = 0
        self.ipv4_hdr_len = 0
        ipv4_ver = bffr[cursor:cursor + self.IPV4_VER_LEN]
        if ipv4_ver.encode("hex") == b'45':
            self.ipv4_ver = 4
            self.ipv4_hdr_len = 20
        cursor += self.IPV4_VER_LEN

        self.ipv4_diff_serv = self.__Binary_Repr(bffr[cursor:cursor + self.IPV4_DIFF_SERV])
        cursor += self.IPV4_DIFF_SERV

        self.ipv4_total_len, = struct.unpack(">H", bffr[cursor:cursor + self.IPV4_TOTAL_LEN])
        cursor += self.IPV4_TOTAL_LEN

        self.ipv4_id, = struct.unpack(">H", bffr[cursor:cursor + self.IPV4_ID])
        cursor += self.IPV4_ID

        self.ipv4_flags_offset = self.__Binary_Repr(bffr[cursor:cursor + self.IPV4_FLAGS_OFFSET])
        cursor += self.IPV4_FLAGS_OFFSET

        # Default Values

        # Input Checks

        # init ...

    def __Binary_MAC_to_String(self, bin_data):
#       '''
#       Private Module
#       '''
        # Inputs
        # Module Code
        # Output
        return "%02x:%02x:%02x:%02x:%02x:%02x" % struct.unpack("BBBBBB",bin_data)

    def __Binary_Repr(self, bin_data):
#       '''
#       Private Module
#       '''
        # Inputs
        # Module Code
        # Output
        ret_str = str()
        ret_str += "0x"
        for byte in bin_data:
            ret_str += "%02x" % struct.unpack("B", byte)
        return ret_str

    def __str__(self):
        stats_str = str()
        stats_str += ( '%17s' % self.enet_dst ) if self.enet_dst != None else ''
        stats_str += ( '%17s' % self.enet_src ) if self.enet_src != None else ''
        stats_str += ( '%2s' % self.enet_type ) if self.enet_type != None else ''
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
        am = AnnounceMessage(pkt)
        self.assertEqual(am.enet_dst, '01:00:5e:00:01:81')
        self.assertEqual(am.enet_src, '00:1c:73:b5:35:1d')
        self.assertEqual(am.enet_type, '0x0800')
        self.assertEqual(am.ipv4_ver, 4)
        self.assertEqual(am.ipv4_hdr_len, 20)
        self.assertEqual(am.ipv4_diff_serv, '0x00')
        self.assertEqual(am.ipv4_total_len, 92)
        self.assertEqual(am.ipv4_id, 0)
        self.assertEqual(am.ipv4_flags_offset, '0x0000')

    @unittest.expectedFailure
    def test_str_from_pcap_file(self):
        None

if __name__ == '__main__':
    # Test class
    unittest.main()
