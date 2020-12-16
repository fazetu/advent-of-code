# part 1
input <- readLines("2020/day1-input.txt")
input <- as.numeric(input)

combos <- t(combn(input, 2))
row_tot <- rowSums(combos)
i <- which(row_tot == 2020)[1]
prod(combos[i, ]) # answer 1

# part 2
combos <- t(combn(input, 3))
row_tot <- rowSums(combos)
i <- which(row_tot == 2020)[1]
prod(combos[i, ])
