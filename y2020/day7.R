input <- readLines("y2020/day7-input.txt")

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

our_bag <- "shiny gold"
