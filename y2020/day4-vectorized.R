# part 1
is_valid_passport1 <- function(lines) {
  Reduce(`&`, lapply(required_fields, function(field) {
    grepl(lines, pattern = sprintf("%s:", field))
  }))
}

# part 2
is_valid_passport2 <- is_valid_passport1
