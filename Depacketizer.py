# responsible for managing the different virtual channels by creating the TransferFrame objects
import struct

def main():
    print("SSRL COSMO Mock Depacketizer...")
    SPACE_DATA = "mission_data.bin"

    try:
        frame_size = 1024
        with open(SPACE_DATA, "rb") as f:
            while True:
                frame = f.read(frame_size)
                transfer_frame = TransferFrame()     
                if not frame:
                    break
                

    except FileNotFoundError:
        print(f"Error: File {SPACE_DATA} NOT FOUND !!!")
        



if __name__ == "__main__":
    main()
