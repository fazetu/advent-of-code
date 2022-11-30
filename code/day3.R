input <- readLines("2020/day3-input.txt")

# part 1
count_trees <- function(hill, right, down) {
  # separate hill input character vector into matrix
  hill_m <- do.call(rbind, strsplit(hill, ""))
  nr <- nrow(hill_m)
  nc <- ncol(hill_m)
  
  r <- 1L # row position tracker
  c <- 1L # column position tracker
  count <- 0L
  
  while (r <= nr) {
    # reset which column we are at to "recycle" the matrix
    if (c > nc) c <- c - nc
    
    # if we hit a tree increment count
    if (hill_m[r, c] == "#") count <- count + 1L
    
    # update position
    r <- r + down
    c <- c + right
  }
  
  count
}

count_trees(input, right = 3L, down = 1L) # answer 1

# part 2
slopes <- list(list(right = 1L, down = 1L),
               list(right = 3L, down = 1L),
               list(right = 5L, down = 1L),
               list(right = 7L, down = 1L),
               list(right = 1L, down = 2L))

counts <- vapply(slopes, function(slope) {
  do.call(count_trees, modifyList(slope, list(hill = input)))
}, integer(1))

prod(counts) # answer 2

# time it
count_trees2 <- function(hill_m, right, down) {
  nr <- nrow(hill_m)
  nc <- ncol(hill_m)
  
  r <- 1L # row position tracker
  c <- 1L # column position tracker
  count <- 0L
  
  while (r <= nr) {
    # reset which column we are at to "recycle" the matrix
    if (c > nc) c <- c - nc
    
    # if we hit a tree increment count
    if (hill_m[r, c] == "#") count <- count + 1L
    
    # update position
    r <- r + down
    c <- c + right
  }
  
  count
}

microbenchmark::microbenchmark(
  part2 = {
    counts <- vapply(slopes, function(slope) {
      do.call(count_trees, modifyList(slope, list(hill = input)))
    }, integer(1))
    
    prod(counts)
  },
  part2a = {
    hill_m <- do.call(rbind, strsplit(input, ""))
    
    counts <- vapply(slopes, function(slope) {
      do.call(count_trees2, modifyList(slope, list(hill_m = hill_m)))
    }, integer(1))
    
    prod(counts)
  },
  times = 1000
)
