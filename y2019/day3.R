get_dir <- function(code) substr(code, 1, 1)

get_dist <- function(code) as.numeric(substr(code, 2, nchar(code)))

out_of_bounds <- function(grid, slice_r, slice_c) {
  if (!missing(slice_r) & !missing(slice_c)) {
    res <- tryCatch(grid[slice_r, slice_c], error = function(e) NULL)
  } else if (!missing(slice_r)) {
    res <- tryCatch(grid[slice_r, ], error = function(e) NULL)
  } else if (!missing(slice_c)) {
    res <- tryCatch(grid[, slice_c], error = function(e) NULL)
  }
  
  is.null(res)
}

expand_grid <- function(grid, dir, dist) {
  switch(
    dir,
    "R" = {
      add <- matrix("", nrow = nrow(grid), ncol = dist)
      cbind(grid, add)
    },
    "L" = {
      add <- matrix("", nrow = nrow(grid), ncol = dist)
      cbind(add, grid)
    },
    "U" = {
      add <- matrix("", nrow = dist, ncol = ncol(grid))
      rbind(add, grid)
    },
    "D" = {
      add <- matrix("", nrow = dist, ncol = ncol(grid))
      rbind(grid, add)
    }
  )
}

draw_wire <- function(grid, wire, start, fill_val) {
  for (code in wire) {
    dir <- get_dir(code)
    dist <- get_dist(code)
    
    if (dir == "R") {
      # move along columns
      end <- c(start[1], start[2] + dist)
      
      need_expand <- out_of_bounds(grid, slice_c = start[2]:end[2])
      if (need_expand) grid <- expand_grid(grid, dir, dist)
      
      # fill grid
      curr_vals <- grid[start[1], (start[2]+1):end[2]]
      new_vals <- curr_vals
      new_vals[curr_vals != "" & curr_vals != fill_val] <- "X"
      new_vals[curr_vals == ""] <- fill_val
      grid[start[1], (start[2]+1):end[2]] <- new_vals
      
      # update
      start <- end
    } else if (dir == "L") {
      # move along columns
      end <- c(start[1], start[2] - dist)
      
      browser()
    } else if (dir == "U") {
      # move along rows
      browser()
    } else if (dir == "D") {
      # move along rows
      browser()
    }
  }
  
  list(grid = grid, start = start)
}

make_grid <- function(wire1, wire2) {
  grid <- matrix("O", 1, 1)
  start <- c(1, 1)
  
  res <- draw_wire(grid, wire1, start, "1")
  grid <- res$grid
  start <- res$start
  
  res <- draw_wire(grid, wire2, start, "2")
  res$grid
}

wire1 <- c("R8","U5","L5","D3")
wire2 <- c("U7","R6","D4","L4")
make_grid(wire1, wire2)




###########################


#######################

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
  browser()
  
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

manhattan_distances <- function(grid) {
  dists <- c()
  
  ro <- which(apply(grid, 1, function(x) any(x == "O")))
  co <- which(apply(grid, 2, function(x) any(x == "O")))
  n_crosses <- sum(grid == "X")
  
  for (i in seq_len(n_crosses)) {
    r <- min(which(apply(grid, 1, function(x) any(x == "X"))))
    c <- min(which(grid[r, ] == "X"))
    dists <- c(dists, abs(ro - r) + abs(co - c))
    grid[r, c] <- "" # get rid of it in grid
  }
  
  dists
}

grid <- matrix("O", 1, 1)
grid <- fill_grid(wire1, grid, fill_val = "1")
grid <- fill_grid(wire2, grid, fill_val = "2")
min(manhattan_distances(grid))

wire1 <- c("R75","D30","R83","U83","L12","D49","R71","U7","L72")
wire2 <- c("U62","R66","U55","R34","D71","R55","D58","R83")
grid <- matrix("O", 1, 1)
grid <- fill_grid(wire1, grid, fill_val = "1")
grid <- fill_grid(wire2, grid, fill_val = "2")
min(manhattan_distances(grid))
