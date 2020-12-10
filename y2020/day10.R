# output joltage = input
input <- as.integer(readLines("y2020/day10-input.txt"))

# part 1
prod(table(diff(c(0, sort(input), max(input) + 3)))) # answer 1

# part 2
input <- c(16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4)

input_s <- sort(input)
joltages <- c(0, input_s, input_s[length(input_s)] + 3)

next_joltages <- function(in_joltage) {
  in_joltage + c(1, 2, 3)
}

possible_next_joltages <- function(in_joltage, joltages) {
  joltages[joltages %in% next_joltages(in_joltage)]
}

choices <- lapply(joltages, possible_next_joltages, joltages)
choices
prod(lengths(choices[-length(choices)]))


##################################


valid_arrangement <- function(arrangement) {
  # arrangement is sorted from lowest to highest joltage
  all(diff(arrangement) <= 3)
}

all_valid_arrangements <- function(input) {
  input_s <- sort(input)
  joltages <- c(0, input_s, input_s[length(input_s)] + 3) # max plus 3 for device joltage
  
  if (!valid_arrangement(joltages)) return(list()) # longest isn't valid, no shorter can be valid
  
  valid_arrangements <- list(joltages)
  j <- 2
  
  # loop
  # while (TRUE) {
    diffs <- diff(joltages)
    can_drop <- which(diffs < 3)
    
    for (i in can_drop) {
      if (valid_arrangement(joltages[-i])) {
        valid_arrangements[[j]] <- joltages[-i]
        j <- j + 1
      }
    }
  # }
  
  valid_arrangements
}

n_valid_arrangements <- function(input) {
  length(all_valid_arrangements(input))
}

all_valid_arrangements(input)
