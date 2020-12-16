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

# to restart with input
system("rm y2020/day14-files -rf")

DIR <- "y2020/day14-files"
if (!dir.exists(DIR)) dir.create(DIR)
FILE_SIZE <- 10000000L # store 10M records per file

ith_file <- function(i) {
  file.path(DIR, sprintf("file-%d.txt", floor(i / FILE_SIZE)))
}

write_value <- function(i, value) {
  f <- ith_file(i)
  
  if (!file.exists(f)) {
    data <- rep("", FILE_SIZE)
    data[i %% FILE_SIZE] <- as.character(value)
    cat(data, file = f, sep = "\n")
  } else {
    data <- readLines(con = f)
    data[i %% FILE_SIZE] <- as.character(value)
    writeLines(text = data, con = f, sep = "\n")
  }
}

command_chunks <- prep_input(input)
j <- 1L

for (chunk in command_chunks) {
  print(sprintf("command #%d", j))
  mask <- chunk$mask
  steps <- chunk$steps
  
  for (step in steps) {
    curr_bit <- num_to_bit(num = step$where)
    new_bit <- apply_mask2(bit = curr_bit, mask = mask)
    pos_bits <- all_bit_combos(bit = new_bit)
    new_val <- bit_to_num(bit = pos_bits)
    
    # expand mem if needed
    for (i in new_val) {
      write_value(i = i, value = step$value)
    }
  }
  
  j <- j + 1L
}

files <- dir(DIR, full.names = TRUE)
ans <- 0L

for (file in files) {
  lines <- readLines(file)
  lines[lines == ""] <- "0"
  ans <- ans + sum(as.integer(lines))
}

ans # answer 2
