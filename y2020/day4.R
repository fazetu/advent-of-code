input <- tolower(readLines("y2020/day4-input.txt"))
input <- paste0(input, " ") # put space at end of every line for paste0 later
any(grepl("&", input)) # fine to use as unique char
input[input == " "] <- "&"
chunks <- trimws(strsplit(paste0(input, collapse = ""), split = "&")[[1]])

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

# part 1
is_valid_chunk1 <- function(chunk) {
  has_fields <- vapply(required_fields, function(field) {
    any(grepl(sprintf("%s:", field), chunk))
  }, logical(1))
  all(has_fields)
}

sum(vapply(chunks, is_valid_chunk1, logical(1))) # answer 1

# part 2
valid_numeric <- function(val) {
  num_try <- tryCatch(as.numeric(val), warning = function(w) FALSE)
  is.numeric(num_try)
}

valid_numeric_range <- function(val, low, high) {
  is_num <- valid_numeric(val)
  if (!is_num) return(FALSE)
  val <- as.numeric(val)
  low <= val & val <= high
}

valid_height <- function(val) {
  last2 <- substr(val, start = nchar(val) - 1, nchar(val))
  
  if (last2 == "cm") {
    CM_MIN <- 150; CM_MAX <- 193
    rest <- substr(val, start = 1, stop = nchar(val) - 2)
    valid_numeric_range(rest, CM_MIN, CM_MAX)
  } else if (last2 == "in") {
    IN_MIN <- 59; IN_MAX <- 76
    rest <- substr(val, start = 1, stop = nchar(val) - 2)
    valid_numeric_range(rest, IN_MIN, IN_MAX)
  } else {
    FALSE
  }
}

valid_hex_color <- function(val) {
  val_split <- strsplit(val, "")[[1]]
  if (val_split[1] != "#") return(FALSE)
  all(grepl("[0-9a-f]", val_split[-1]))
}

valid_eye_color <- function(val) {
  val %in% c("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
}

valid_passport_id <- function(val) {
  val_split <- strsplit(val, "")[[1]]
  if (length(val_split) != 9) return(FALSE)
  all(grepl("[0-9]", val_split))
}

is_valid_chunk2 <- function(chunk) {
  # can still quit early if not all fields there
  if (!is_valid_chunk1(chunk)) return(FALSE)
  
  pairs <- strsplit(strsplit(chunk, " ")[[1]], ":")
  keys <- vapply(pairs, function(l) l[[1]], character(1))
  vals <- vapply(pairs, function(l) l[[2]], character(1))
  
  valid_numeric_range(vals[keys == "byr"], 1920, 2002) &
    valid_numeric_range(vals[keys == "iyr"], 2010, 2020) &
    valid_numeric_range(vals[keys == "eyr"], 2020, 2030) &
    valid_height(vals[keys == "hgt"]) &
    valid_hex_color(vals[keys == "hcl"]) &
    valid_eye_color(vals[keys == "ecl"]) &
    valid_passport_id(vals[keys == "pid"])
}

sum(vapply(chunks, is_valid_chunk2, logical(1))) # answer 2
