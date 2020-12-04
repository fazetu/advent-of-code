input <- tolower(readLines("y2020/day4-input.txt"))
input <- paste0(input, " ") # put space at end of every line for paste0 later
any(grepl("&", input)) # fine to use as unique char
input[input == " "] <- "&"
passports <- trimws(strsplit(paste0(input, collapse = ""), split = "&")[[1]])

fields <- c(
  "Birth Year" = "byr",
  "Issue Year" = "iyr",
  "Expiration Year" = "eyr",
  "Height" = "hgt",
  "Hair Color" = "hcl",
  "Eye Color" = "ecl",
  "Passport ID" = "pid",
  "Country ID" = "cid"
)

required_fields <- fields[-length(fields)]

# functions
source("y2020/day4-non-vectorized.R")
# source("y2020/day4-vectorized.R")

# part 1
sum(vapply(passports, is_valid_passport1, logical(1))) # answer 1

# part 2
sum(vapply(passports, is_valid_passport2, logical(1))) # answer 2
