N_PLANE_ROWS <- 128
N_PLANE_COLUMNS <- 8
PLANE_ROWS <- 0:(N_PLANE_ROWS - 1)
PLANE_COLUMNS <- 0:(N_PLANE_COLUMNS - 1)

halve <- function(x) {
  if (length(x) == 1) return(x)
  if (length(x) %% 2 != 0) stop("x can't be divided in half")
  half_mark <- length(x) / 2
  list(x[1:half_mark], x[(half_mark + 1):length(x)])
}

find_half <- function(pass) {
  pass <- strsplit(pass, "")[[1]]
  
  rows <- PLANE_ROWS
  halves <- halve(PLANE_ROWS)
  
  for (i in seq_along(pass)) {
    let <- pass[i]
    
    if (let == "F") {
      rows <- halves[[1]]
      halves <- halve(rows)
    } else if (let == "B") {
      rows <- halves[[2]]
      halves <- halve(rows)
    }
  }
  
  rows
}

find_column <- function(pass) {
  pass <- strsplit(pass, "")[[1]]
  
  cols <- PLANE_COLUMNS
  halves <- halve(cols)
  
  for (i in seq_along(pass)) {
    let <- pass[i]
    
    if (let == "L") {
      cols <- halves[[1]]
      halves <- halve(cols)
    } else if (let == "R") {
      cols <- halves[[2]]
      halves <- halve(cols)
    }
  }
  
  cols
}

seat_ID <- function(pass) {
  (find_row(pass) * 8) + find_column(pass)
}

input <- readLines("y2020/day5-input.txt")

# part 1
ids <- vapply(input, seat_ID, numeric(1))
max(ids)

# part 2
plane <- data.frame(input = input, row = vapply(input, find_row, numeric(1)),
                    col = vapply(input, find_row, numeric(1)),
                    id = vapply(input, seat_ID, numeric(1)))

min_id <- min(plane$id)
max_id <- max(plane$id)

for (i in min_id:max_id) {
  if (i %in% plane$id) next
  if ((i + 1) %in% plane$id & (i - 1) %in% plane$id) print(i)
}
