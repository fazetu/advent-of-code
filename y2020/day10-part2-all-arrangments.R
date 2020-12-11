input <- as.integer(readLines("y2020/day10-input.txt"))

input_to_joltages <- function(input) {
  input_s <- sort(input)
  c(0L, input_s, input_s[length(input_s)] + 3L)
}

next_joltages <- function(in_joltage) {
  in_joltage + c(1L, 2L, 3L)
}

possible_next_joltages <- function(in_joltage, joltages) {
  joltages[joltages %in% next_joltages(in_joltage)]
}

# valid_arrangement <- function(arrangement) {
#   # arrangement is sorted from lowest to highest joltage
#   all(diff(arrangement) %in% c(1L, 2L, 3L))
# }

explode <- function(l, x) {
  mapply(c, replicate(length(x), l, simplify = FALSE), x, SIMPLIFY = FALSE)
}

arrangements <- function(joltages) {
  paths <- list(joltages[1])
  m <- joltages[length(joltages)]
  maxes <- vapply(paths, max, integer(1))
  
  while(!all(maxes == m)) {
    paths <- unlist(lapply(paths, function(path) {
      nexts <- possible_next_joltages(path[length(path)], joltages = joltages)
      
      if (length(nexts) == 0) list(path)
      else if (length(nexts) == 1) list(c(path, nexts))
      else explode(path, nexts)
    }), recursive = FALSE)
    
    maxes <- vapply(paths, max, integer(1))
  }
  
  paths
}

joltages <- input_to_joltages(input)
arrs <- arrangements(joltages)
length(arrs) # part 2
