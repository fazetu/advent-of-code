next_number <- function(history, i) {
  prev_history <- history[seq_len(i - 2L)]
  prev_number <- history[i - 1L]
  
  if (!prev_number %in% prev_history) {
    # first time the number was spoken so next is 0
    0L
  } else {
    # number has been spoken so speak the difference
    last_time <- max(which(prev_number == prev_history))
    i - 1L - last_time
  }
}

run_n <- function(start, n) {
  history <- integer(n)
  history[seq_len(length(start))] <- start
  is <- seq(length(start) + 1L, n, by = 1L)
  
  for (i in is) {
    print(i)
    history[i] <- next_number(history, i)
  }
  
  history
}

input <- c(0L, 3L, 6L)
input <- c(17L, 1L, 3L, 16L, 19L, 0L)

# part 1
n <- 2020L
res <- run_n(input, n)
res[n] # answer 1

# part 2
n <- 30000000L
res <- run_n(input, n)
res[n] # answer 2
