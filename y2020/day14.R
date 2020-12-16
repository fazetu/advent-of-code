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
# try writing out to a text file? and updating certain positions of file?
# move to python for file editing?

options(scipen = 100)
sum(mem) # answer 2

# part 2 spark
input <- readLines("y2020/day14-input.txt")

n <- input_mem_n(input)
mem <- numeric(n)
command_chunks <- prep_input(input)

# install.packages("sparklyr")
library(sparklyr)
# spark_install(version = "2.1.0")
sc <- spark_connect(master = "local")
mem_tbl <- copy_to(sc, data.frame(mem = mem), "mem")

DBI::dbGetQuery(sc, "CREATE TABLE add_rows (mem INT)")
DBI::dbGetQuery(sc, sprintf("INSERT INTO add_rows VALUES (%s)", paste0(rep(0, 100000), collapse = ", ")))


for (chunk in command_chunks) {
  mask <- chunk$mask
  steps <- chunk$steps
  
  for (step in steps) {
    curr_bit <- num_to_bit(num = step$where)
    new_bit <- apply_mask2(bit = curr_bit, mask = mask)
    pos_bits <- all_bit_combos(bit = new_bit)
    new_val <- bit_to_num(bit = pos_bits)
    
    # expand mem if needed
    mx <- max(new_val)
    nr <- sdf_nrow(mem_tbl)
    while (mx > nr) {
      print(sprintf("adding rows to mem_tbl. current nrow: %d", nr))
      # stack data onto mem
      DBI::dbGetQuery(sc, "SELECT * FROM mem UNION SELECT * from add_rows")
      nr <- sdf_nrow(mem_tbl)
    } 
    
    mem_tbl$mem[new_val] <- step$value
  }
}

sum(mem_tbl$mem)

spark_disconnect(sc)
