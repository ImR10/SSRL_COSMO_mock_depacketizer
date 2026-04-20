# responsible for managing the different virtual channels by creating the TransferFrame objects
import struct
from TransferFrame import TransferFrame
from VirtualChannel import VirtualChannel

def main():
    print("SSRL COSMO Mock Depacketizer...")
    SPACE_DATA = "mission_data.bin"

    try:
        frame_size = 1024
        channels = {}

        with open(SPACE_DATA, "rb") as f:
            while True:
                frame = f.read(frame_size)
                if not frame:
                    break

                # create transfer frame
                transfer_frame = TransferFrame(frame)

                # check if VCID exists
                if transfer_frame.vcid not in channels:
                    print(f"New Virtual Channel detected: VCID {transfer_frame.vcid}")
                    channels[transfer_frame.vcid] = VirtualChannel(transfer_frame.vcid)

                # grab channel
                vc = channels[transfer_frame.vcid]

                # process packet
                packet = channels[transfer_frame.vcid].process_frame(transfer_frame)

                if packet:
                    if packet.apid == 100:
                        with open("recovered_image.raw", "ab") as out_file:
                            f.write(packet.payload)     
                
        print(f"VCID: {transfer_frame.vcid}")
        print(f"FHP: {transfer_frame.fhp}")

    except FileNotFoundError:
        print(f"Error: File {SPACE_DATA} NOT FOUND !!!")


if __name__ == "__main__":
    main()
