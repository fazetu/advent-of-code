input <- readLines("y2020/day3-input.txt")

# part 1
count_trees <- function(hill, right, down) {
  # explode hill input into matrix
  # keep original sized hill matrix around in hill_o for cbinding
  hill_o <- do.call(rbind, strsplit(hill, ""))
  hill_m <- hill_o
  
  # starting positions
  r <- 1
  c <- 1
  
  count <- 0L
  
  while (r <= nrow(hill_m)) {
    # if we go too far right, add more to the hill
    if (c > ncol(hill_m)) hill_m <- cbind(hill_m, hill_o)
    
    # if we hit a tree increment count
    if (hill_m[r, c] == "#") count <- count + 1L
    
    # update position
    r <- r + down
    c <- c + right
  }
  
  count
}


count_trees(input, right = 3, down = 1) # answer 1

# part 2
possible_slopes <- list(list(right = 1, down = 1),
                        list(right = 3, down = 1),
                        list(right = 5, down = 1),
                        list(right = 7, down = 1),
                        list(right = 1, down = 2))

counts <- vapply(possible_slopes, function(l) {
  do.call(count_trees, modifyList(l, list(hill = input)))
}, integer(1))

prod(counts) # answer 2

