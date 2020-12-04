# input
source("y2020/day4-read-input.R")

# first try
source("y2020/day4-non-vectorized.R")
sum(vapply(PASSPORTS, is_valid_passport1, logical(1))) # answer 1
sum(vapply(PASSPORTS, is_valid_passport2, logical(1))) # answer 2

# second try
source("y2020/day4-vectorized.R")
sum(is_valid_passport1(PASSPORTS)) # answer 1
sum(is_valid_passport2(PASSPORTS)) # answer 2
