input <- tolower(readLines("2020/day4-input.txt"))
input <- paste0(input, " ") # put space at end of every line for paste0 later
any(grepl("&", input)) # fine to use as unique char
input[input == " "] <- "&"
PASSPORTS <- trimws(strsplit(paste0(input, collapse = ""), split = "&")[[1]])

FIELDS <- c(
  "Birth Year" = "byr",
  "Issue Year" = "iyr",
  "Expiration Year" = "eyr",
  "Height" = "hgt",
  "Hair Color" = "hcl",
  "Eye Color" = "ecl",
  "Passport ID" = "pid",
  "Country ID" = "cid"
)

REQUIRED_FIELDS <- FIELDS[-length(FIELDS)]

rm(input)
