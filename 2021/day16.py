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

def convert_hex_to_binary(hex: str) -> str:
    bin = ""
    for char in hex:
        bin += hex_to_binary[char]

    return bin

def version_of_binary(bin: str) -> int:
    return int(bin[:3], 2)

def type_id_of_binary(bin: str) -> int:
    return int(bin[3:6], 2)

def literal_value_binary(bin: str) -> int:
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
        

hex = "D2FE28"
bin = convert_hex_to_binary(hex)
version_of_binary(bin)
type_id_of_binary(bin)
literal_value_binary(bin)

hex = "38006F45291200"
bin = convert_hex_to_binary(hex)
version_of_binary(bin)
type_id_of_binary(bin)
