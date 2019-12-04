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
    plot(pts_df, type = "l", col = color)
    points(pts_df, col = color)
  } else {
    lines(pts_df, col = color)
    points(pts_df, col = color)
  }
}

wire1 <- "R8,U5,L5,D3"
wire2 <- "U7,R6,D4,L4"
plot_wire(wire1, color = "red", first = TRUE)
plot_wire(wire2, color = "blue")

wire1 <- "R75,D30,R83,U83,L12,D49,R71,U7,L72"
wire2 <- "U62,R66,U55,R34,D71,R55,D58,R83"
plot_wire(wire1, color = "red", first = TRUE)
plot_wire(wire2, color = "blue")
