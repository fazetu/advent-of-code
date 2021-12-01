# inputs
input <- c(
  199,
  200,
  208,
  210,
  200,
  207,
  240,
  269,
  260,
  263
)

input <- as.integer(readLines("2021/day1-input.txt"))

# part 1
count_increases <- function(x) sum(head(x, -1) < tail(x, -1))
count_increases(input) # part 1 answer

# part 2
make_window_slices <- function(n, window_size = 3) {
  lapply(seq(n - window_size + 1), function(i) i:(i + window_size - 1))
}

windows <- lapply(make_window_slices(length(input), 3), function(slice) input[slice])
window_sums <- vapply(windows, sum, numeric(1L))
count_increases(window_sums) # part 2 answer
