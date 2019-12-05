next_point <- function(current_point, code) {
  direction <- substr(code, 1, 1)
  distance <- as.numeric(substr(code, 2, nchar(code)))
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

plot_wire <- function(wire, start = c(0, 0), color = "black", first = FALSE) {
  pts <- wire_points(wire, start)
  pts_df <- t(data.frame(pts))
  if (first) {
    plot(pts_df, type = "l", col = color, xlab = "x", ylab = "y")
    points(pts_df, col = color)
  } else {
    lines(pts_df, col = color)
    points(pts_df, col = color)
  }
}

slope <- function(x1, x2) {
  (x2[2] - x1[2]) / (x2[1] - x1[1])
}

intercept <- function(x1, x2) {
  m <- slope(x1, x2)
  x1[2] - m * x1[1]
}

points_cross <- function(a1, a2, b1, b2) {
  a1 <- c(0, 0)
  a2 <- c(1, 1)
  b1 <- c(0, 1)
  b2 <- c(1, 0)
  
  
  
  am <- slope(a1, a2)
  ab <- intercept(a1, a2)
  bm <- slope(b1, b2)
  bb <- intercept(b1, b2)
  
  af <- function(x) am * x + ab
  bf <- function(x) bm * x + bb
  
  
  
  
}

wire1 <- "R8,U5,L5,D3"
wire2 <- "U7,R6,D4,L4"
wire1_pts <- wire_points(wire1)
wire2_pts <- wire_points(wire2)

plot_wire(wire1, color = "red", first = TRUE)
plot_wire(wire2, color = "blue")

wire1 <- "R75,D30,R83,U83,L12,D49,R71,U7,L72"
wire2 <- "U62,R66,U55,R34,D71,R55,D58,R83"
plot_wire(wire1, color = "red", first = TRUE)
plot_wire(wire2, color = "blue")

input <- readLines("2019/day3-input.txt")
wire1 <- input[1]
wire2 <- input[2]
plot_wire(wire1, color = "red", first = TRUE)
plot_wire(wire2, color = "blue")
