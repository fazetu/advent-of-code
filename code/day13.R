input <- readLines("2020/day13-input.txt")
input <- c("939", "7,13,x,x,59,x,31,19")

prep_input <- function(input) {
  list(earliest = as.integer(input[1]),
       buses = suppressWarnings(as.integer(strsplit(input[2], ",")[[1]])))
}

info <- prep_input(input)
earliest <- info$earliest
buses <- info$buses

# part 1
buses <- buses[!is.na(buses)]

times_to_next_bus <- buses - (earliest %% buses)
soonest_time <- min(times_to_next_bus)
soonest_bus_id <- buses[times_to_next_bus == soonest_time]
soonest_bus_id * soonest_time # answer 1

# part 2
# in python

# brute force is TOO SLOW:
# delta_t <- seq_along(buses)[!is.na(buses)] - 1L
# buses <- buses[!is.na(buses)]
# 
# valid_t <- function(t, buses, delta_t) {
#   times <- (t %% buses) + delta_t
#   times[1L] == 0L & all(times[-1L] == buses[-1L])
# }
# 
# upper_bound <- prod(buses)
# 
# t <- buses[1L]
# while(!valid_t(t = t, buses = buses, delta_t = delta_t)) {
#   if (t > upper_bound) break
#   print(format(t, big.mark = ","))
#   t <- t + buses[1L]
# }
# beepr::beep()
# t # answer 2
