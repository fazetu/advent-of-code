# part 1
# AAA)BBB means BBB orbits AAA
# check sum = # direct orbits + # indirect orbits

split_orbits <- function(str_vec) {
  strsplit(str_vec, ")")
}

get_all_planets <- function(orbits) {
  unique(unlist(orbits))
}

get_all_nodes <- function(orbits) {
  inners <- sapply(orbits, `[`, 1)
  outers <- sapply(orbits, `[`, 2)
  setdiff(unique(outers), unique(inners))
}

direct_orbit <- function(inners, outers, planet) {

  i <- max(which(outers == planet))
  inners[i]
}

all_orbits <- function(orbits, planet) {
  inners <- sapply(orbits, `[`, 1)
  outers <- sapply(orbits, `[`, 2)
  
  res <- character(0)
  curr_planet <- planet
  while (curr_planet != "COM") {
    do <- direct_orbit(inners, outers, curr_planet)
    res <- c(res, do)
    curr_planet <- do
  }
  
  res
}

n_orbits <- function(orbits, planet) {
  length(all_orbits(orbits, planet))
}

orbits_summary <- function(orbits) {
  planets <- get_all_planets(orbits)
  s <- sapply(planets, function(planet) n_orbits(orbits, planet))
  s
}

orbits_checksum <- function(orbits) {
  sum(orbits_summary(orbits))
}

orbits <- split_orbits(c("COM)B","B)C","C)D","D)E","E)F","B)G","G)H","D)I","E)J","J)K","K)L"))

n_orbits(orbits, "D")
n_orbits(orbits, "L")
n_orbits(orbits, "COM")
orbits_checksum(orbits)

input <- readLines("2019/day6-input.txt")
orbits <- split_orbits(input)
orbits_checksum(orbits) # answer

# part 2
orbits <- split_orbits(c("COM)B","B)C","C)D","D)E","E)F","B)G","G)H","D)I","E)J","J)K","K)L","K)YOU","I)SAN"))

orbits_you <- all_orbits(orbits, "YOU")
orbits_san <- all_orbits(orbits, "SAN")

# first intersect
inter <- intersect(orbits_you, orbits_san)[1]
in_path <- orbits_you[1:which(orbits_you == inter)]
out_path <- orbits_san[1:which(orbits_san == inter)]
(length(in_path) - 1) + (length(out_path) - 1) # answer
