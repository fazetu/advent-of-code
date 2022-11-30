# output joltage = input
input <- as.integer(readLines("2020/day10-input.txt"))

# part 1
prod(table(diff(c(0L, sort(input), max(input) + 3L)))) # answer 1

# part 2
input <- c(16L, 10L, 15L, 5L, 1L, 11L, 7L, 19L, 6L, 12L, 4L)
input <- c(28L, 33L, 18L, 42L, 31L, 14L, 46L, 20L, 48L, 47L, 24L, 23L, 49L, 45L, 19L, 38L, 39L, 11L, 1L, 32L, 25L, 35L, 8L, 17L, 7L, 9L, 4L, 2L, 34L, 10L, 3L)

input_to_joltages <- function(input) {
  input_s <- sort(input)
  c(0L, input_s, input_s[length(input_s)] + 3L)
}

count_n_ones_in_runs <- function(deltas) {
  n_ones_in_runs <- c(0L)
  j <- 1L
  for (i in seq_along(deltas)) {
    curr_delta <- deltas[i]
    
    if (curr_delta == 1L) {
      n_ones_in_runs[j] <- n_ones_in_runs[j] + 1L
    } else if (curr_delta == 3L) {
      j <- j + 1L
      n_ones_in_runs[j] <- 0L
    }
  }
  
  n_ones_in_runs
}

joltages <- input_to_joltages(input)
deltas <- diff(joltages)
table(deltas) # fails if deltas are not all 1's or 3's

n_ones_in_runs <- count_n_ones_in_runs(deltas)
n_ones_in_runs <- n_ones_in_runs[n_ones_in_runs != 0] # drop 0 runs

mults <- c(1, 2, 4, 7) # fails if runs are longer than 5!
options(scipen = 100)
prod(mults[n_ones_in_runs])
