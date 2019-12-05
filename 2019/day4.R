# part 1
# 6 digits
# in a range
# 2 adjacent digits are the same (22 in 122345)
# going from left to right the digits never decrease

is_6_digits <- function(num) nchar(as.character(num)) == 6
is_6_digits(123)
is_6_digits(123456)

split_num <- function(num) as.numeric(strsplit(as.character(num), "")[[1]])

is_not_decreasing <- function(nums) {
  curr <- nums[1]
  for (i in 2:length(nums)) {
    if (curr > nums[i]) return(FALSE)
    curr <- nums[i]
  }
  return(TRUE)
}
is_not_decreasing(split_num(122345))
is_not_decreasing(split_num(111123))
is_not_decreasing(split_num(223450))

has_double <- function(nums) {
  for (n in nums) {
    if (sum(n == nums) >= 2) return(TRUE)
  }
  return(FALSE)
}
has_double(split_num(123456))
has_double(split_num(122345))
has_double(split_num(111111))

passes <- function(num) {
  nums <- split_num(num)
  has_double(nums) & is_not_decreasing(nums)
}

input <- "136818-685979"
rng <- as.numeric(strsplit(input, "-")[[1]])
res <- sapply(seq(rng[1], rng[2]), passes)
sum(res) # answer

# part 2
has_exact_double <- function(nums) {
  for (n in nums) {
    if (sum(n == nums) == 2) return(TRUE)
  }
  return(FALSE)
}

passes <- function(num) {
  nums <- split_num(num)
  has_exact_double(nums) & is_not_decreasing(nums)
}

input <- "136818-685979"
rng <- as.numeric(strsplit(input, "-")[[1]])
res <- sapply(seq(rng[1], rng[2]), passes)
sum(res) # answer
