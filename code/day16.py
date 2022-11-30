from typing import Dict, List, Optional
from dataclasses import dataclass

# with open("day16-input.txt", "r") as f:
#     input = f.readline().strip()

hex_to_binary = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

@dataclass
class PacketData:
    version: int
    type: int
    name: str
    value: Optional[int]

def convert_hex_to_binary(hex: str) -> str:
    bin = ""
    for char in hex:
        bin += hex_to_binary[char]

    return bin

def version(bin: str) -> int:
    return int(bin[:3], 2)

def type_id(bin: str) -> int:
    return int(bin[3:(3 + 3)], 2)

def length_type_id(bin: str) -> int:
    return int(bin[6])

def literal_value(bin: str) -> int:
    num_bin = ""
    last_chunk = False
    start = 6
    while not last_chunk:
        group = bin[start:(start + 5)]
        num_bin += group[1:]
        if group[0] == "0":
            last_chunk = True
        start += 5

    return int(num_bin, 2)

def process_literal_packet(packet: str, i: int) -> PacketData:
    t = type_id(packet[i:])

    if t != 4:
        raise ValueError("This packet is not a literal packet")

    return PacketData(version(packet[i:]), t, "literal", literal_value(packet[i:]))

def process_operator_packet(packet: str, res: List[PacketData]):
    t = type_id(packet)

    if t == 4:
        raise ValueError("This packet is not an operator packet")

    res.append(PacketData(version(packet), t, "operator", None))

    lt = length_type_id(packet)

    if lt == 0:
        total_length = int(packet[7:22], 2)
        next_packets = packet[22:(22 + total_length)]
        process_packet(next_packets, res)
    elif lt == 1:
        next_packets = packet[22:]
        process_packet(next_packets, res)

def process_packet(packet: str, res: List[PacketData]):
    if type_id(packet) == 4:
        process_literal_packet(packet, res)
    else:
        process_operator_packet(packet, res)


# hex = "D2FE28"
# bin = convert_hex_to_binary(hex)
# res = []
# process_packet(bin, res)
# res

hex = "38006F45291200"
bin = convert_hex_to_binary(hex)
res = []
process_packet(bin, res)
res
