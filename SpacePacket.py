# responsible for reading from VirtualChannel and parsing the packet header (SPH)
# 6 bytes total (each 2 bytes):
#  - packet identifier: version #, type indicator, secondary header flag, and APID
#  - packet sequence control: sequence flag, packet sequence count
#  - packet data length

