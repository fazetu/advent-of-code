find_neighbors_layer <- function(m, x, y) {
  x_slice <- (x - 1L):(x + 1L)
  y_slice <- (y - 1L):(y + 1L)
  
  # x direction goes "left" of current - add more columns to the left
  if (any(x_slice <= 0)) {
    n_more_cols <- sum(x_slice <= 0)
    m <- cbind(matrix(0, nrow = nrow(m), ncol = n_more_cols), m)
    x_slice <- x_slice + n_more_cols
  }
  
  # y direction goes "above" current - add more rows above
  if (any(y_slice <= 0)) {
    n_more_rows <- sum(y_slice <= 0)
    m <- rbind(matrix(0, nrow = n_more_rows, ncol = ncol(m)), m)
    # can't have negatives in a matrix indexes
    y_slice <- y_slice + n_more_rows
  }
  
  # x direction goes "right" of current - add more columns to the right
  if (any(x_slice > nrow(m))) {
    n_more_cols <- max(x_slice) - ncol(m)
    m <- cbind(m, matrix(0L, nrow = nrow(m), ncol = n_more_cols))
  }
  
  # y direction goes "below" current - add more rows below
  if (any(y_slice > ncol(m))) {
    n_more_rows <- sum(x_slice > ncol(m))
    m <- cbind(m, matrix(0L, nrow = n_more_rows, ncol = ncol(m)))
  }
  
  list(neighbors = m[y_slice, x_slice], new = m)
}

# run 1 cycle
cycle <- function(state) {
  new_state <- state
  
  for (layer in state) {
    layer
    
    for (r in seq_len(nrow(layer))) {
      for (c in seq_len(ncol(layer))) {
        find_neighbors_layer(layer, c, r)
      }
    }
  }
}

input <- c(
  ".#.",
  "..#",
  "###"
)

state <- list("0" = do.call(rbind, lapply(strsplit(input, ""), function(r) ifelse(r == "#", 1, 0))))

for (i in 1:6) {
  state <- cycle(state = state)
}

x <- 1
y <- 1
z <- 0
