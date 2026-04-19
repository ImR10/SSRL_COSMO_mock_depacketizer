# responsible for slicing the buffer based on TFPH

class VirtualChannel():
    def __init__(self, vcid):
        self.vcid = vcid
        self.packet_buffer = bytearray()
        self.target_packet_length = 0

    def process_frame(self, frame_obj):
        payload = frame_obj.raw_data[6:]
        fhp = frame_obj.fhp

        if fhp == 2047:
            # no new packet
            self.packet_buffer.extend(payload)
        else:
            # 1. add 'tail end' to end of packet
            packet_tail_data = payload[:fhp]
            self.packet_buffer.extend(packet_tail_data)

            # 2. If the buffer has data, packet ends so split from buffer
        if len(self.buffer) > 0:
            self.dispatch_completed_packet()
            
        # 3. Start a new packet from the FHP position
        self.buffer = bytearray(payload[fhp:])

def dispatch_completed_packet(self):
    packet = SpacePacket(self.buffer) 
    print(f"DEBUG: VCID {self.vcid} reconstructed a packet of {len(self.buffer)} bytes")
    self.buffer = bytearray()
