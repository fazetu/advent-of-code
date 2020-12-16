small_input <- c(
  "35",
  "20",
  "15",
  "25",
  "47",
  "40",
  "62",
  "55",
  "65",
  "95",
  "102",
  "117",
  "150",
  "182",
  "127",
  "219",
  "299",
  "277",
  "309",
  "576"
)

small_input <- as.numeric(small_input)
input <- as.numeric(readLines("2020/day9-input.txt"))

all_sums <- function(nums, m = 2L) colSums(combn(nums, m = m))

find_first_invalid <- function(nums, window_size = 25L, m = 2L) {
  start <- window_size + 1L
  
  for (i in start:length(nums)) {
    previous_nums <- nums[(i - window_size):(i - 1)]
    if (!nums[i] %in% all_sums(previous_nums, m = m)) return(nums[i])
  }
}

# find_first_invalid(small_input, window_size = 5L, m = 2L)
find_first_invalid(input, window_size = 25L, m = 2L) # answer 1

find_contiguous_range <- function(nums, target_value) {
  n <- length(nums)
  
  seqs <- lapply(seq_along(nums), function(i) {
    cs <- cumsum(nums[i:n])[-1] # -1 to ensure at least 2 numbers go into the sum
    j <- which(cs == target_value)
    if (length(j) == 0) return(NULL)
    nums[i:(i + j)]
  })
  
  unlist(seqs)
}

# find_contiguous_range(small_input, find_first_invalid(small_input, 5L, 2L))

rng <- find_contiguous_range(input, find_first_invalid(input, 25L, 2L))
sum(range(rng)) # answer 2
