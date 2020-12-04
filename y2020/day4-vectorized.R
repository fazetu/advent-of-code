# part 1
is_valid_passport1 <- function(lines) {
  Reduce(`&`, lapply(REQUIRED_FIELDS, function(field) {
    grepl(lines, pattern = sprintf("%s:", field))
  }))
}

# part 2
try_numeric <- function(vals) {
  suppressWarnings(as.numeric(vals))
}

valid_numeric_range <- function(vals, low, high) {
  num <- try_numeric(vals)
  !is.na(num) & low <= num & num <= high
}

valid_height <- function(vals, cm_min = 150, cm_max = 193, in_min = 59, in_max = 76) {
  valid <- rep(FALSE, length(vals))
  is_cm <- grepl("cm$", vals)
  is_in <- grepl("in$", vals)
  valid[is_cm] <- valid_numeric_range(substr(vals[is_cm], start = 1, nchar(vals[is_cm]) - 2),
                                      low = cm_min, high = cm_max)
  valid[is_in] <- valid_numeric_range(substr(vals[is_in], start = 1, nchar(vals[is_in]) - 2),
                                      low = in_min, high = in_max)
  valid
}

valid_hex_color <- function(vals) grepl("^#[0-9a-f]{6}$", vals)

valid_eye_color <- function(vals) vals %in% c("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

valid_passport_id <- function(vals) grepl("^[0-9]{9}$", vals)

validation_map <- list(
  "byr" = function(x) valid_numeric_range(x, 1920, 2002),
  "iyr" = function(x) valid_numeric_range(x, 2010, 2020),
  "eyr" = function(x) valid_numeric_range(x, 2020, 2030),
  "hgt" = function(x) valid_height(x),
  "hcl" = function(x) valid_hex_color(x),
  "ecl" = function(x) valid_eye_color(x),
  "pid" = function(x) valid_passport_id(x),
  "cid" = function(x) rep(TRUE, length(x))
)

is_valid_passport_values <- function(lines) {
  # TODO: this preprocessing could be done before hand to increase time
  keys_vals <- lapply(lapply(strsplit(lines, " "), strsplit, ":"), function(l) {
    keys <- vapply(l, function(x) x[[1]], character(1))
    vals <- vapply(l, function(x) x[[2]], character(1))
    setNames(vals, keys)
  })
  
  valids <- lapply(REQUIRED_FIELDS, function(field) {
    validation_map[[field]](sapply(keys_vals, `[`, field))
  })
  
  Reduce(`&`, valids)
}

is_valid_passport2 <- function(lines) {
  is_valid_passport1(lines) & is_valid_passport_values(lines)
}
