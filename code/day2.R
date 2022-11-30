input <- c(
  "forward 5",
  "down 5",
  "forward 8",
  "up 3",
  "down 8",
  "forward 2"
)

input <- readLines("2021/day2-input.txt")

# part 1
run_commands1 <- function(input) {
  commands <- strsplit(input, " ")
  horizontal <- 0
  depth <- 0
  
  for (i in seq_along(commands)) {
    dir <- commands[[i]][1]
    dist <- as.integer(commands[[i]][2])
    
    if (dir == "forward") {
      horizontal <- horizontal + dist
    } else if (dir == "up") {
      depth <- depth - dist
    } else if (dir == "down") {
      depth <- depth + dist
    }
  }
  
  c(horizontal, depth)
}

prod(run_commands1(input))

# part 2
run_commands2 <- function(input) {
  commands <- strsplit(input, " ")
  horizontal <- 0
  depth <- 0
  aim <- 0
  
  for (i in seq_along(commands)) {
    dir <- commands[[i]][1]
    dist <- as.integer(commands[[i]][2])
    
    if (dir == "forward") {
      horizontal <- horizontal + dist
      depth <- depth + (aim * dist)
    } else if (dir == "up") {
      aim <- aim - dist
    } else if (dir == "down") {
      aim <- aim + dist
    }
  }
  
  c(horizontal, depth)
}

prod(run_commands2(input))
