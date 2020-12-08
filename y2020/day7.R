input <- readLines("y2020/day7-input.txt")

prep_input <- function(input) {
  input <- gsub("\\.", "", input)
  bags <- gsub("^(.*) bags contain (.*)$", "\\1", input)
  contains <- strsplit(gsub("^(.*) bags contain (.*)$", "\\2", input), ", ")
  contains <- lapply(contains, function(x) {
    if (all(x == "no other bags")) return(0)
    amt <- as.integer(gsub("^(\\d+) (.*) bags?", "\\1", x))
    color <- gsub("^(\\d+) (.*) bags?", "\\2", x)
    setNames(amt, color)
  })
  names(contains) <- bags
  contains
}

# input <- c(
#   "light red bags contain 1 bright white bag, 2 muted yellow bags.",
#   "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
#   "bright white bags contain 1 shiny gold bag.",
#   "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
#   "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
#   "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
#   "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
#   "faded blue bags contain no other bags.",
#   "dotted black bags contain no other bags."
# )

contains <- prep_input(input)

# part 1
find_bags <- function(curr_bags, contains) {
  names(contains)[sapply(contains, function(l) any(names(l) %in% curr_bags))]
}

bag_path <- function(curr_bags, contains) {
  if (identical(find_bags(curr_bags, contains), character(0))) {
    curr_bags
  } else {
    c(curr_bags, bag_path(find_bags(curr_bags, contains), contains))
  }
}

poss_bags <- bag_path("shiny gold", contains)
length(unique(poss_bags[-1])) # answer 1

# part 2
input <- c(
  "light red bags contain 1 bright white bag, 2 muted yellow bags.",
  "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
  "bright white bags contain 1 shiny gold bag.",
  "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
  "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
  "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
  "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
  "faded blue bags contain no other bags.",
  "dotted black bags contain no other bags."
)

input <- c(
  "shiny gold bags contain 2 dark red bags.",
  "dark red bags contain 2 dark orange bags.",
  "dark orange bags contain 2 dark yellow bags.",
  "dark yellow bags contain 2 dark green bags.",
  "dark green bags contain 2 dark blue bags.",
  "dark blue bags contain 2 dark violet bags.",
  "dark violet bags contain no other bags."
)

contains <- prep_input(input)

count_bags <- function(bag, contains) {
  sum(contains[[bag]])
}

all_contains <- function()

bag_path("shiny gold", contains)[-1]

sapply(bag_path("shiny gold", contains)[-1], count_bags, contains)

count_bags("shiny gold", contains)

count_bags("shiny gold", contains)

count_contains <- function(curr_bags, contains) {
  if (contain_bags(curr_bags, contains))
}
