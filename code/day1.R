# part 1
fuel <- function(mass) floor(mass / 3) - 2

fuel(12)
fuel(14)
fuel(1969)
fuel(100756)

masses <- as.numeric(readLines("2019/day1-input.txt"))
fuel_by_module <- fuel(masses)
sum(fuel_by_module) # answer

# part 2
mass <- 14
fmass <- fuel(mass)
fuel(fmass) # negative

mass <- 1969
fmass <- fuel(mass)
ffmass <- fuel(fmass)
fffmass <- fuel(ffmass)
ffffmass <- fuel(fffmass)
fffffmass <- fuel(ffffmass)
fuel(fffffmass) # negative

fuel_fuel <- function(mass) {
  res <- 0
  fmass <- fuel(mass)
  while (fmass > 0) {
    res <- res + fmass # must add first
    fmass <- fuel(fmass)
  }
  res
}

fuel_fuel(14)
fuel_fuel(1969)
fuel_fuel(100756)

fuel_fuel_by_module <- sapply(masses, fuel_fuel)
sum(fuel_fuel_by_module) # answer

View(data.frame(fuel_by_module, fuel_fuel_by_module, diff = fuel_fuel_by_module - fuel_by_module))
