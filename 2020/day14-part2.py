import itertools as it

# helper functions
def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()
    # remove new line symbols
    return [line.strip() for line in lines]

def num_to_bit(num, n = 36):
    s = str(bin(num))[2:] # first 2 characters are 0b
    if len(s) < n:
        return ("0" * (n - len(s))) + s
    elif len(s) > n:
        return s[n:]
    else:
        return s

def bit_to_num(bit):
    pows = [int(val) * (2 ** i) for i, val in enumerate(reversed(bit))]
    return sum(pows)

# part 2 specific functions
def select_bit(main_bit, mask_bit):
    # for part 2 how does each bit get compared with the mask
    if mask_bit == "0":
        return main_bit
    elif mask_bit == "1":
        return "1"
    elif mask_bit == "X":
        return "X"

def apply_mask(bit, mask):
    # for part 2 apply the mask to the memory location bit
    return "".join([select_bit(main_bit, mask_bit) for main_bit, mask_bit in zip(bit, mask)])

def pos_bits(bit):
    # find all possible bits from an input bit with X's
    if bit.find("X") == -1:
        # no X's to vary
        return [bit]

    # split into list
    bit_list = [let for let in bit]
    xs = [i for i, val in enumerate(bit_list) if val == "X"]
    replace = list(it.product(*([("0", "1")] * len(xs))))
    res = []
    for rep in replace:
        bit_ = bit_list
        for i, x_ind in enumerate(xs):
            bit_[x_ind] = rep[i]
        res.append("".join(bit_))
    return res

# main
input = read_input("day14-input.txt")

# mem = open("day14-mem.txt", mode = "r+")
mem = []

mask = "" # so pylance think mask exists

# write to mem file
for line in input:
    if line.startswith("mask"):
        # new mask line, update our current mask
        mask = line.split(" = ")[1]
    else:
        # normal line of instructions
        location, value = line.split(" = ")
        location_num = int(location.replace("mem[", "").replace("]", ""))
        value_num = int(value)

        # find possible locations
        location_bit = num_to_bit(location_num)
        location_masked = apply_mask(location_bit, mask)
        location_bits = pos_bits(location_masked)
        location_nums = [bit_to_num(bit) for bit in location_bits]

        # overwrite all possible locations with value
        for location_num in location_nums:
            if location_num > (len(mem) - 1):
                mem += [0] * (location_num - len(mem) + 1)
            mem[location_num] = value_num
            
sum(mem)
# mem.close()

# mem file is too big to read into memory
# read chunks of mem file and accumulate sum
