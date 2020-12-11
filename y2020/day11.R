# . = floor
# L = empty seat
# # = occupied seat

input <- c(
  "L.LL.LL.LL",
  "LLLLLLL.LL",
  "L.L.L..L..",
  "LLLL.LL.LL",
  "L.LL.LL.LL",
  "L.LLLLL.LL",
  "..L.L.....",
  "LLLLLLLLLL",
  "L.LLLLLL.L",
  "L.LLLLL.LL"
)

input <- readLines("y2020/day11-input.txt")

input_to_matrix <- function(input) do.call(rbind, strsplit(input, ""))

find_adjacent_seats <- function(m, i, j) {
  if (i > nrow(m)) stop("i surpasses m's rows")
  if (j > ncol(m)) stop("j surpasses m's cols")
  
  if (i == 1) i_slice <- i:(i + 1L)
  else if (i == nrow(m)) i_slice <- (i - 1L):i
  else i_slice <- (i - 1L):(i + 1L)
  
  if (j == 1) j_slice <- j:(j + 1L)
  else if (j == ncol(m)) j_slice <- (j - 1L):j
  else j_slice <- (j - 1L):(j + 1L)
  
  m[i_slice, j_slice]
}

n_occupied_adjacent_seats <- function(m, i, j) {
  adj <- find_adjacent_seats(m = m, i = i, j = j)
  # don't include the current seat of interest
  sum(adj == "#") - (m[i, j] == "#")
}

run_iter <- function(m, occupied_tolerance = 4L) {
  next_m <- m
  
  for (i in 1:nrow(m)) {
    for (j in 1:ncol(m)) {
      if (m[i, j] == ".") next
      n <- n_occupied_adjacent_seats(m, i, j)
      if (m[i, j] == "L" & n == 0L) next_m[i, j] <- "#"
      else if (m[i, j] == "#" & n >= occupied_tolerance) next_m[i, j] <- "L"
    }
  }
  
  next_m
}

run_iters <- function(m) {
  prev_m <- m
  
  while (TRUE) {
    m <- run_iter(m)
    if (all(prev_m == m)) break
    prev_m <- m
  }
  
  m
}

# part 1
m <- input_to_matrix(input)
m_final <- run_iters(m)
sum(m_final == "#") # answer 1

# part 2
# get upper, left diagonal from i,j
ul_diag <- function(m, i, j) {
  
}

# get upper, right diagonal from i,j
ur_diag <- function(m, i, j) {
  
}

# get lower, left diagonal from i,j
ll_diag <- function(m, i, j) {
  
}

# get lower, right diagonal from i,j
lr_diag <- function(m, i, j) {
  
}

# change how we count adjacent occupied seats for part 2
n_occupied_adjacent_seats <- function(m, i, j) {
  # views from current seat
  # -1 to exclude our current seat from the view
  left <- m[i, 1:j][-1]
  right <- m[i, j:ncol(m)][-1]
  up <- m[1:i, j][-1]
  down <- m[i:nrow(m), j][-1]
  
  (sum(left == "#") > 0) +
    (sum(right == "#") > 0) +
    (sum(up == "#") > 0) +
    (sum(down == "#") > 0)
}

m <- input_to_matrix(input)
m_final <- run_iters(m)
sum(m_final == "#") # answer 2