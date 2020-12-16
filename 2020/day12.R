input <- readLines("2020/day12-input.txt")

input <- c(
  "F10",
  "N3",
  "F7",
  "R90",
  "F11"
)

source("2020/day12-ship-ref-class.R")

# part 1
ship <- Ship$new()
for (command in input) ship$move(command = command)
ship$manhattan_distance() # answer 1

# part 2
ship <- ShipWaypoint$new()
for (command in input) ship$move(command = command)
ship$manhattan_distance() # answer 2
