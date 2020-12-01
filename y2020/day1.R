# part 1
report <- readLines("y2020/day1-input.txt")
report <- as.numeric(report)

combos <- expand.grid(report, report)
combos$sum <- rowSums(combos)

combos[combos$sum == 2020, ]
prod(combos[combos$sum == 2020, ][1, 1:2]) # answer 1

# part 2
combos <- expand.grid(report, report, report)
combos$sum <- rowSums(combos)

combos[combos$sum == 2020, ]
prod(combos[combos$sum == 2020, ][1, 1:3]) # answer 2
