z <- function(mat, pt) {
  x <- pt[1] + 1
  y <- nrow(mat) - pt[2]
  mat[y, x]
}

`z<-` <- function(mat, pt, value) {
  x <- pt[1] + 1
  y <- nrow(mat) - pt[2]
  mat[y, x] <- value
  mat
}

expand_mat <- function(mat, dir) {
  switch(
    dir,
    "R" = cbind(mat, rep("", nrow(mat))),
    "L" = cbind(rep("", nrow(mat)), mat),
    "U" = rbind(rep("", ncol(mat)), mat),
    "D" = rbind(mat, rep("", ncol(mat)))
  )
}

# mat <- matrix(1:15, nrow = 3, ncol = 5, byrow = TRUE)
# pt <- c(0, 0)
# z(mat, pt) # 11
# z(mat, pt) <- 999
# mat
# z(mat, c(1, 0)) # 12
# z(mat, c(1, 1)) # 7
# z(mat, c(3, 0)) # 14

get_direction <- function(code) substr(code, 1, 1)

get_distance <- function(code) as.numeric(substr(code, 2, nchar(code)))

next_point <- function(current_point, code) {
  direction <- get_direction(code)
  distance <- get_distance(code)
  switch(
    direction,
    "R" = current_point[1] <- current_point[1] + distance,
    "L" = current_point[1] <- current_point[1] - distance,
    "U" = current_point[2] <- current_point[2] + distance,
    "D" = current_point[2] <- current_point[2] - distance
  )
  current_point
}

wire_points <- function(wire, start = c(0, 0)) {
  codes <- strsplit(wire, ",")[[1]]
  res <- list(start)
  for (i in seq_along(codes)) {
    res[[i + 1]] <- next_point(res[[i]], codes[i])
  }
  res
}

find_start <- function(grid, o_val = "O") {
  row <- which(apply(grid, 1, function(row) any(row == o_val)))
  col <- which(apply(grid, 2, function(col) any(col == o_val)))
  c(col - 1, nrow(grid) - row)
}

fill_grid <- function(wire, grid, start = c(0, 0), fill_val = "1", cross_val = "X") {
  cp <- find_start(grid)
  
  for (code in wire) {
    dir <- get_direction(code)
    dist <- get_distance(code)
    
    if (dir == "R") {
      for (i in seq_len(dist)) {
        cp <- c(cp[1] + 1, cp[2])
        curr_val <- tryCatch(z(grid, cp), error = function(e) NULL)
        if (is.null(curr_val) | length(curr_val) == 0) grid <- expand_mat(grid, dir)
        curr_val <- z(grid, cp)
        if (curr_val == fill_val) next
        z(grid, cp) <- ifelse(curr_val != "", cross_val, fill_val)
      }
    } else if (dir == "L") {
      for (i in seq_len(dist)) {
        cp <- c(cp[1] - 1, cp[2])
        curr_val <- tryCatch(z(grid, cp), error = function(e) NULL)
        if (is.null(curr_val) | length(curr_val) == 0) grid <- expand_mat(grid, dir)
        curr_val <- z(grid, cp)
        if (curr_val == fill_val) next
        z(grid, cp) <- ifelse(curr_val != "", cross_val, fill_val)
      }
    } else if (dir == "U") {
      for (i in seq_len(dist)) {
        cp <- c(cp[1], cp[2] + 1)
        curr_val <- tryCatch(z(grid, cp), error = function(e) NULL)
        if (is.null(curr_val) | length(curr_val) == 0) grid <- expand_mat(grid, dir)
        curr_val <- z(grid, cp)
        if (curr_val == fill_val) next
        z(grid, cp) <- ifelse(curr_val != "", cross_val, fill_val)
      }
    } else if (dir == "D") {
      for (i in seq_len(dist)) {
        cp <- c(cp[1], cp[2] - 1)
        curr_val <- tryCatch(z(grid, cp), error = function(e) NULL)
        if (is.null(curr_val) | length(curr_val) == 0) grid <- expand_mat(grid, dir)
        curr_val <- z(grid, cp)
        if (curr_val == fill_val) next
        z(grid, cp) <- ifelse(curr_val != "", cross_val, fill_val)
      }
    }
  }
  
  grid
}

wire1 <- c("R8","U5","L5","D3")
wire2 <- c("U7","R6","D4","L4")
grid <- matrix("O", 1, 1)
grid <- fill_grid(wire1, grid, fill_val = "1")
grid <- fill_grid(wire2, grid, fill_val = "2")
grid

dist_o_to_cross <- function(grid) {
  o <- find_start(grid)
  n_crosses <- sum(grid == "X")
}


