source("y2020/day14-functions.R")

input <- c(
  "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
  "mem[8] = 11",
  "mem[7] = 101",
  "mem[8] = 0"
)

input <- readLines("y2020/day14-input.txt")

# part 1
n <- input_mem_n(input)
mem <- numeric(n)
command_chunks <- prep_input(input)

for (chunk in command_chunks) {
  mem <- process_command_chunk1(mem = mem, chunk = chunk)
}

options(scipen = 100)
sum(mem) # answer 1

# part 2
input <- c(
  "mask = 000000000000000000000000000000X1001X",
  "mem[42] = 100",
  "mask = 00000000000000000000000000000000X0XX",
  "mem[26] = 1"
)

input <- readLines("y2020/day14-input.txt")

command_chunks <- prep_input(input)

mem <- c()

for (chunk in command_chunks) {
  mask <- chunk$mask
  steps <- chunk$steps
  
  for (step in steps) {
    curr_bit <- num_to_bit(num = step$where)
    new_bit <- apply_mask2(bit = curr_bit, mask = mask)
    pos_bits <- all_bit_combos(bit = new_bit)
    new_val <- bit_to_num(bit = pos_bits)
    mem[as.character(new_val)] <- step$value
  }
}

options(scipen = 100)
sum(mem)

# too high: 3584380595408
