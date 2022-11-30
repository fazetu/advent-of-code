source("2020/day4-read-input.R")

# time a non vectorized approach vs a vectorized one

# part 1
microbenchmark::microbenchmark(
  non_vect = {
    source("2020/day4-non-vectorized.R")
    sum(vapply(PASSPORTS, is_valid_passport1, logical(1)))
  },
  vect = {
    source("2020/day4-vectorized.R")
    sum(is_valid_passport1(PASSPORTS))
  },
  times = 500
)

# part 2
microbenchmark::microbenchmark(
  non_vect = {
    source("2020/day4-non-vectorized.R")
    sum(vapply(PASSPORTS, is_valid_passport2, logical(1)))
  },
  vect = {
    source("2020/day4-vectorized.R")
    sum(is_valid_passport2(PASSPORTS))
  },
  times = 500
)
