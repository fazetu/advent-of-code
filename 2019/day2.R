# part 1
# 99 = program finished and should stop
# 1 = adds based on next 3 values
# 2 = multiplies based on next 3 values

code <- c(1,9,10,3,2,3,11,0,99,30,40,50)

process_code <- function(code) {
  n <- length(code)
  i <- 1
  
  while(TRUE) {
    op <- code[i]
    if (op == 99) break
    p1 <- code[i + 1] + 1
    p2 <- code[i + 2] + 1
    p3 <- code[i + 3] + 1
    
    if (op == 1) {
      val <- code[p1] + code[p2]
    } else if (op == 2) {
      val <- code[p1] * code[p2]
    }
    
    code[p3] <- val
    i <- i + 4
  }
  
  code
}

process_code(code)
process_code(c(1,0,0,0,99))
process_code(c(2,3,0,3,99))
process_code(c(2,4,4,5,99,0))
process_code(c(1,1,1,4,99,5,6,0,99))

gap <- readLines("2019/day2-input.txt")
gap <- as.numeric(strsplit(gap, ",")[[1]])
gap[1 + 1] <- 12
gap[2 + 1] <- 2
gap
res <- process_code(gap)
res[0 + 1] # answer

# part 2
noun_verb <- function(code, noun, verb) {
  code[1 + 1] <- noun
  code[2 + 1] <- verb
  res <- process_code(code)
  res[0 + 1]
}

gap <- readLines("2019/day2-input.txt")
gap <- as.numeric(strsplit(gap, ",")[[1]])
noun_verb(gap, 1, 1)

grid <- expand.grid(noun = 0:99, verb = 0:99)
grid$res <- mapply(function(n, v) noun_verb(gap, n, v), grid$noun, grid$verb)
grid[grid$res == 19690720, ]

noun_verb(gap, 40, 19)
100 * 40 + 19 # answer
