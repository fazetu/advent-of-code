input <- c(
  "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
  "byr:1937 iyr:2017 cid:147 hgt:183cm",
  "",
  "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
  "hcl:#cfa07d byr:1929",
  "",
  "hcl:#ae17e1 iyr:2013",
  "eyr:2024",
  "ecl:brn pid:760753108 byr:1931",
  "hgt:179cm",
  "",
  "hcl:#cfa07d eyr:2025 pid:166559648",
  "iyr:2011 ecl:brn hgt:59in"
)


input <- readLines("y2020/day4-input.txt")
breaks <- grep("^$", input)
break_is <- mapply(`:`,
                   c(1, head(breaks, -1) + 1),
                   c(head(breaks, -1) - 1, length(input)),
                   SIMPLIFY = FALSE)
chunks <- lapply(break_is, function(i) input[i])

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
is_valid_chunk <- function(chunk) {
  has_fields <- vapply(required_fields, function(field) {
    any(grepl(field, chunk))
  }, logical(1))
  all(has_fields)
}

vapply(chunks, is_valid_chunk, logical(1))
sum(vapply(chunks, is_valid_chunk, logical(1))) # answer 1
