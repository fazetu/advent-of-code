input <- readLines("2020/day2-input.txt")

first <- gsub("^(\\d+)-(\\d+) ([a-z]): ([a-z]*)$", "\\1", input)
last <- gsub("^(\\d+)-(\\d+) ([a-z]): ([a-z]*)$", "\\2", input)
letter <- gsub("^(\\d+)-(\\d+) ([a-z]): ([a-z]*)$", "\\3", input)
password <- gsub("^(\\d+)-(\\d+) ([a-z]): ([a-z]*)$", "\\4", input)

# part 1
is_valid1 <- vapply(seq_along(input), function(i) {
  pw <- strsplit(password[i], "")[[1]]
  times <- sum(grepl(letter[i], pw))
  (as.integer(first[i]) <= times) & (times <= as.integer(last[i]))
}, logical(1))

sum(is_valid1) # answer 1

# part 2
is_valid2 <- vapply(seq_along(input), function(i) {
  pw <- strsplit(password[i], "")[[1]]
  f <- as.integer(first[i])
  l <- as.integer(last[i])
  let <- letter[i]
  (pw[f] == let & pw[l] != let) | (pw[f] != let & pw[l] == let)
}, logical(1))

sum(is_valid2) # answer 2
