input_to_matrix <- function(input) do.call(rbind, strsplit(input, ""))

# part 1
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

n_occupied_adjacent_seats1 <- function(m, i, j) {
  adj <- find_adjacent_seats(m = m, i = i, j = j)
  # don't include the current seat of interest
  sum(adj == "#") - (m[i, j] == "#")
}

run_iter1 <- function(m, occupied_tolerance = 4L) {
  next_m <- m
  
  for (i in 1:nrow(m)) {
    for (j in 1:ncol(m)) {
      if (m[i, j] == ".") next
      n <- n_occupied_adjacent_seats1(m, i, j)
      if (m[i, j] == "L" & n == 0L) next_m[i, j] <- "#"
      else if (m[i, j] == "#" & n >= occupied_tolerance) next_m[i, j] <- "L"
    }
  }
  
  next_m
}

run_iters1 <- function(m, occupied_tolerance = 4L) {
  prev_m <- m
  
  while (TRUE) {
    m <- run_iter1(m, occupied_tolerance = occupied_tolerance)
    if (all(prev_m == m)) break
    prev_m <- m
  }
  
  m
}

# part 2
# minimum length between two vectors
minl <- function(x, y) min(length(x), length(y))

go_diag <- function(m, rows, cols) mapply(function(row, col) m[row, col], rows, cols)

# get up, left diagonal from i,j
ul_diag <- function(m, i, j) {
  rows_ <- i:1L
  cols_ <- j:1L
  rows <- rows_[1:minl(rows_, cols_)]
  cols <- cols_[1:minl(rows_, cols_)]
  go_diag(m, rows, cols)
}

# get up, right diagonal from i,j
ur_diag <- function(m, i, j) {
  rows_ <- i:1L
  cols_ <- j:ncol(m)
  rows <- rows_[1:minl(rows_, cols_)]
  cols <- cols_[1:minl(rows_, cols_)]
  go_diag(m, rows, cols)
}

# get down, left diagonal from i,j
dl_diag <- function(m, i, j) {
  rows_ <- i:nrow(m)
  cols_ <- j:1L
  rows <- rows_[1:minl(rows_, cols_)]
  cols <- cols_[1:minl(rows_, cols_)]
  go_diag(m, rows, cols)
}

# get down, right diagonal from i,j
dr_diag <- function(m, i, j) {
  rows_ <- i:nrow(m)
  cols_ <- j:ncol(m)
  rows <- rows_[1:minl(rows_, cols_)]
  cols <- cols_[1:minl(rows_, cols_)]
  go_diag(m, rows, cols)
}

filter_to_first_seat <- function(x) {
  is_seat <- x %in% c("L", "#")
  if (!any(is_seat)) return(character(0))
  x[is_seat][1]
}

n_occupied_adjacent_seats2 <- function(m, i, j) {
  # views from current seat
  # -1 to exclude our current seat from the view
  l  <- filter_to_first_seat(m[i, j:1L][-1]       )
  r  <- filter_to_first_seat(m[i, j:ncol(m)][-1]  )
  u  <- filter_to_first_seat(m[i:1L, j][-1]       )
  d  <- filter_to_first_seat(m[i:nrow(m), j][-1]  )
  ur <- filter_to_first_seat(ur_diag(m, i, j)[-1L])
  ul <- filter_to_first_seat(ul_diag(m, i, j)[-1L])
  dr <- filter_to_first_seat(dr_diag(m, i, j)[-1L])
  dl <- filter_to_first_seat(dl_diag(m, i, j)[-1L])
  sight <- c(l, r, u, d, ur, ul, dr, dl)
  sum(sight == "#")
}

run_iter2 <- function(m, occupied_tolerance = 5L) {
  next_m <- m
  
  for (i in 1:nrow(m)) {
    for (j in 1:ncol(m)) {
      if (m[i, j] == ".") next
      n <- n_occupied_adjacent_seats2(m, i, j)
      if (m[i, j] == "L" & n == 0L) next_m[i, j] <- "#"
      else if (m[i, j] == "#" & n >= occupied_tolerance) next_m[i, j] <- "L"
    }
  }
  
  next_m
}

run_iters2 <- function(m, occupied_tolerance = 5L) {
  prev_m <- m
  
  while (TRUE) {
    m <- run_iter2(m, occupied_tolerance = occupied_tolerance)
    if (all(prev_m == m)) break
    prev_m <- m
  }
  
  m
}