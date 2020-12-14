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

n <- input_mem_n(input)
mem <- numeric(n)
command_chunks <- prep_input(input)

for (chunk in command_chunks) {
  mem <- process_command_chunk2(mem = mem, chunk = chunk)
}

# cannot allocate memory
# try writing out to a text file? and upating certain positions

options(scipen = 100)
sum(mem) # answer 2
