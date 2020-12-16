source("2020/day8-functions.R")

small_input <- c(
  "nop +0",
  "acc +1",
  "jmp +4",
  "acc +3",
  "jmp -3",
  "acc -99",
  "acc +1",
  "jmp -4",
  "acc +6"
)

input <- readLines("2020/day8-input.txt")

# commands <- prep_input(small_input)
commands <- prep_input(input)

# part 1
run_commands(commands)$ACCUMULATOR # answer 1

# part 2
states <- fix_all(commands)

i_good_state <- which(vapply(states, function(l) l$GOOD, logical(1)))
states[[i_good_state]]$ACCUMULATOR # answer 2
