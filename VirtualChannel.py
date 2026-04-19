# responsible for slicing the buffer based on TFPH

class VirtualChannel():
    def __init__(self, vcid):
        self.vcid = vcid
        self.packet_buffer = bytearray()
        self.target_packet_length = 0

    def process_frame(self):
        if (self.packet_buffer):
            self.packet_buffer.append()
