# responsible for slicing out primary header (TFPH) to find which Virtual Channel (VC) 
# data stream the data belongs to.

import struct

class TransferFrame:
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.parse_TFPH

    # parses the Transfer Frame Primary Header (Bytes 0-5)
    def parse_TFPH(self):
        TF_primary_header = self.raw_data[0:6]
        word1, word2, word3 = struct.unpack('>HHH', TF_primary_header)

        # parse the VCID, master_count, vc_count, and FHP
        self.VCID = (word1 >> 1) & 0x07
        self.FHP = word3 & 0x07FF

    # get byte index of where new packet starts
    def get_packet_start_index(self):
        if self.fhp == 2047:
            return None # No new packet starts here
        
        # The FHP points to the start relative to the DATA FIELD.
        # Since the data field starts at byte 6, we add 6.
        return self.fhp + 6
