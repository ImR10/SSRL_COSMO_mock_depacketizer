# responsible for slicing the buffer based on TFPH

from SpacePacket import SpacePacket

class VirtualChannel():
    def __init__(self, vcid):
        self.vcid = vcid
        self.buffer = bytearray()

    def process_frame(self, frame_obj):
        payload = frame_obj.raw_data[6:]
        fhp = frame_obj.fhp

        if fhp == 2047:
            # No new packet starts here. Just keep adding to the pile.
            self.buffer.extend(payload)
            return None
        else:
            # 1. extend 'tail end' of the previous packet
            packet_tail_data = payload[:fhp]
            self.buffer.extend(packet_tail_data)

            # 2. If buffer has data, packet is complete
            finished_packet = None
            if len(self.buffer) > 0:
                finished_packet = self.dispatch_completed_packet()
                
            # 3. Start new packet from the FHP position
            # This MUST happen after dispatching the old one
            self.buffer = bytearray(payload[fhp:])
            
            return finished_packet

    def dispatch_completed_packet(self):
        # Pass the current full buffer to the SpacePacket parser
        packet = SpacePacket(self.buffer) 
        self.buffer = bytearray()

        if packet.apid == 2047:
            return None # Ignore fill packets

        return packet