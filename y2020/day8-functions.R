prep_input <- function(input) {
  splt <- strsplit(input, " ")
  
  lapply(seq_along(splt), function(i) {
    list(id = i, op = splt[[i]][1], arg = as.integer(splt[[i]][2]))
  })
}

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

run_commands <- function(commands, accumulator = 0L, i = 1L) {
  state <- list(ACCUMULATOR = accumulator, I = i, GOOD = FALSE)
  id_history <- c()
  
  while (TRUE) {
    command <- commands[[state$I]]
    if (command$id %in% id_history) return(state)
    
    state <- command_dispatch[[command$op]](command$arg, state)
    
    if (state$I == (length(commands) + 1)) {
      state$GOOD <- TRUE # program executed until the end
      return(state)
    }
    
    id_history <- c(id_history, command$id)
  }
}

try_fix_jmp_nop <- function(commands, fix_i, accumulator = 0L, i = 1L) {
  if (commands[[fix_i]]$op == "jmp") {
    # current one to change is jmp so change to nop
    commands[[fix_i]]$op <- "nop"
    state <- run_commands(commands = commands, accumulator = accumulator, i = i)
  } else {
    # current one to change is nop so change to jmp
    commands[[fix_i]]$op <- "jmp"
    state <- run_commands(commands = commands, accumulator = accumulator, i = i)
  }
  
  state
}

fix_all <- function(commands, accumulator = 0L, i = 1L) {
  ops <- vapply(commands, function(l) l$op, character(1))
  states <- list()
  j <- 1
  
  for (fix_i in which(ops %in% c("jmp", "nop"))) {
    state <- try_fix_jmp_nop(commands = commands, fix_i = fix_i, accumulator = accumulator, i = i)
    states[[j]] <- state
    j <- j + 1
  }
  
  states
}