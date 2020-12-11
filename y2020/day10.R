# output joltage = input
input <- as.integer(readLines("y2020/day10-input.txt"))

# part 1
prod(table(diff(c(0, sort(input), max(input) + 3)))) # answer 1

# part 2
input <- c(16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4)

input_to_joltages <- function(input) {
  input_s <- sort(input)
  c(0, input_s, input_s[length(input_s)] + 3)
}

joltages <- input_to_joltages(input)

next_joltages <- function(in_joltage) {
  in_joltage + c(1, 2, 3)
}

possible_next_joltages <- function(in_joltage, joltages) {
  joltages[joltages %in% next_joltages(in_joltage)]
}

valid_arrangement <- function(arrangement) {
  # arrangement is sorted from lowest to highest joltage
  all(diff(arrangement) <= 3)
}

# (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
# (0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
# (0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
# (0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 7, 10, 12, 15, 16, 19, (22)

explode <- function(l, x) {
  if (length(x) == 1) {
    lapply(l, `c`, x)
  } else {
    unlist(mapply(function(lst, val) {
      lapply(lst, `c`, val)
    }, replicate(length(x), l, simplify = FALSE), x, SIMPLIFY = FALSE), recursive = FALSE)
  }
}

arrangements <- function(in_joltage, joltages, paths = list(in_joltage)) {
  if (in_joltage == joltages[length(joltages)]) {
    explode(paths, in_joltage)
  } else {
    nexts <- possible_next_joltages(in_joltage, joltages)
    paths <- explode(paths, nexts)
    lapply(nexts, function(x) {
      arrangements(x, joltages = joltages, paths = paths)
    })
  }
}

arrangements(joltages[1], joltages)

all_arrangements <- function(joltages) {
  # longest isn't valid, no shorter can be valid
  if (!valid_arrangement(joltages)) return(list())
  
  arrangements <- list(joltages[1])
  
  while(TRUE) {
    
  }
  
  for (joltage in joltages[-1]) {
    nxts <- possible_next_joltages(in_joltage = joltage, joltages = joltages)
    arrangements <- 
    
    if (length(nxts) == 1) {
      path <- c(joltage, nxts)
    } else {
      # explode path or something
    }

    
  }
}


n_arrangements <- function(input) {
  length(all_arrangements(input))
}

all_arrangements(input)


possible_next_joltages(joltages[1], joltages)
possible_next_joltages(joltages[2], joltages)

choices <- lapply(joltages, possible_next_joltages, joltages)
choices
prod(lengths(choices[-length(choices)]))
