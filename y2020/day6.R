input <- readLines("y2020/day6-input.txt")
any(grepl("&", input)) # fine to use &
input[input == ""] <- "&"
input <- paste0(input, collapse = "")
input <- strsplit(input, "&")[[1]]

# part 1
answers <- strsplit(input, "")
unique_answers <- lapply(answers, unique)
sum(lengths(unique_answers)) # answer 1

# part 2
input <- readLines("y2020/day6-input.txt")
breaks <- which(input == "")
is <- mapply(`:`, c(1, breaks + 1), c(breaks, length(input)))
groups <- lapply(is, function(i) input[i])
groups[[length(groups)]] <- c(groups[[length(groups)]], "")
groups <- lapply(groups, function(group) group[-length(group)])

count_group <- function(group) {
  ans <- strsplit(group, "")
  length(Reduce(`intersect`, ans))
}

counts <- vapply(groups, count_group, integer(1))
sum(counts)
