# responsible for managing the different virtual channels by creating the TransferFrame objects
import struct
from TransferFrame import TransferFrame

def main():
    print("SSRL COSMO Mock Depacketizer...")
    SPACE_DATA = "mission_data.bin"

    try:
        frame_size = 1024
        with open(SPACE_DATA, "rb") as f:
            while True:
                frame = f.read(frame_size)
                if not frame:
                    break

                transfer_frame = TransferFrame(frame)     
                
        print(f"VCID: {transfer_frame.vcid}")
        print(f"FHP: {transfer_frame.fhp}")

    except FileNotFoundError:
        print(f"Error: File {SPACE_DATA} NOT FOUND !!!")


if __name__ == "__main__":
    main()
