# . = floor
# L = empty seat
# # = occupied seat

source("y2020/day11-functions.R")
input <- readLines("y2020/day11-input.txt")

# part 1
m <- input_to_matrix(input)
m_final <- run_iters1(m, occupied_tolerance = 4L)
sum(m_final == "#") # answer 1

# part 2
# change how we count adjacent occupied seats for part 2
m <- input_to_matrix(input)
m_final <- run_iters2(m, occupied_tolerance = 5L)
sum(m_final == "#") # answer 2
