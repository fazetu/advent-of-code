source("2020/day7-functions.R")

input <- readLines("2020/day7-input.txt")

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

num_contain <- prep_input(input)

# part 1
length(unique(all_colors_color_can_be_inside("shiny gold", num_contain))) # answer 1

# part 2
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

# input <- c(
#   "shiny gold bags contain 2 dark red bags.",
#   "dark red bags contain 2 dark orange bags.",
#   "dark orange bags contain 2 dark yellow bags.",
#   "dark yellow bags contain 2 dark green bags.",
#   "dark green bags contain 2 dark blue bags.",
#   "dark blue bags contain 2 dark violet bags.",
#   "dark violet bags contain no other bags."
# )

num_contain <- prep_input(input)

# minus 1 to not count shiny gold itself
rec_count_bags("shiny gold", 1L, num_contain) - 1L # answer 2
