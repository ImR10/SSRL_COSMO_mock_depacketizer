# responsible for reading from VirtualChannel and parsing the packet header (SPH)
# 6 bytes total (each 2 bytes):
#  - packet identifier: version #, type indicator, secondary header flag, and APID
#  - packet sequence control: sequence flag, packet sequence count
#  - packet data length

import struct

class SpacePacket():
    def __init__(self, buffer):
        self.buffer = buffer
        self.payload = buffer[6:]
        self.parseSPH()

    def parseSPH(self):
        space_PH = self.buffer[0:6]
        word1, word2, word3 = struct.unpack('>HHH', space_PH)

        # retrieve the packet identifier (bytes 0-1)
        self.version_num = (word1 >> 13) & 0x07
        self.packet_type = (word1 >> 12) & 0x01
        self.secondary_HF = (word1 >> 11) & 0x01
        self.APID = word1 & 0x07FF

        # retrieve sequence control (bytes 2-3)
        self.sequence_flag = (word2 >> 14) & 0x03
        self.sequence_count = word2 & 0x3FFF

        # retrieve data length (bytes 4-5)
        self.data_length = word3 + 1

        # make sure payload is same size as what the SPH says
        if len(self.payload) != self.data_length:
            print(f"Warning: Packet Length Mismatch! Header says {self.data_length}, but got {len(self.payload)}")