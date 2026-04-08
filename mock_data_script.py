# responsible for creating mock TransferFrames for parsing/testing
import struct

def generate_test_file(filename="mission_data.bin"):
    # Frame size is usually 1024
    FRAME_SIZE = 1024
    
    with open(filename, "wb") as f:
        # --- FRAME 1: The Start of a Big Packet ---
        # TM Header (simplified): Version(2b), SCID(10b), VCID(3b), OCF(1b)
        # We'll just pack a 2-byte ID and 4-bytes of counts/pointers
        # VCID=1, FHP=0 (starts at byte 6)
        header1 = struct.pack(">HHBB", 0x0022, 0x0000, 0x00, 0x00) # FHP is 0
        
        # Space Packet Header (The 'Inner' Letter): APID=100, Length=2000
        packet_header = struct.pack(">HHH", 0x0064, 0xC001, 2000)
        
        # Data for Frame 1
        payload1 = b"IMAGE_PART_A" + (b"A" * 1000)
        
        # Assemble Frame 1
        frame1 = header1 + packet_header + payload1
        f.write(frame1[:FRAME_SIZE]) # Ensure it's exactly 1024
        
        # --- FRAME 2: The Continuation ---
        # VCID=1, FHP=2047 (0x07FF) means 'Continuation'
        header2 = struct.pack(">HHHH", 0x0022, 0x0001, 0x01, 0x07FF)
        
        # Data for Frame 2
        payload2 = b"IMAGE_PART_B" + (b"B" * 1000)
        
        # Assemble Frame 2
        frame2 = header2 + payload2
        f.write(frame2[:FRAME_SIZE])

    print(f"Generated {filename}. You are ready to start coding!")

generate_test_file()