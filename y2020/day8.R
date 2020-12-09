# input <- c(
#   "nop +0",
#   "acc +1",
#   "jmp +4",
#   "acc +3",
#   "jmp -3",
#   "acc -99",
#   "acc +1",
#   "jmp -4",
#   "acc +6"
# )

input <- readLines("y2020/day8-input.txt")

prep_input <- function(input) {
  splt <- strsplit(input, " ")
  
  lapply(seq_along(splt), function(i) {
    list(id = i, op = splt[[i]][1], arg = as.integer(splt[[i]][2]))
  })
}

commands <- prep_input(input)

acc <- function(arg, state) {
  state$ACCUMULATOR <- state$ACCUMULATOR + arg
  state$I <- state$I + 1L
  state
}

jmp <- function(arg, state) {
  state$I <- state$I + arg
  state
}

nop <- function(arg, state) {
  state$I <- state$I + 1L
  state
}

command_dispatch <- list(
  "acc" = function(arg, state) acc(arg, state),
  "jmp" = function(arg, state) jmp(arg, state),
  "nop" = function(arg, state) nop(arg, state)
)

run_commands <- function(commands) {
  state <- list(ACCUMULATOR = 0L, I = 1L)
  id_history <- c()
  
  while (TRUE) {
    command <- commands[[state$I]]
    if (command$id %in% id_history) return(state)
    state <- command_dispatch[[command$op]](command$arg, state)
    id_history <- c(id_history, command$id)
  }
}

# part 1
run_commands(commands)$ACCUMULATOR # answer 1

# part 2
