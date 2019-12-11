# part 1

# helpers
# make zero indexing easier
z <- function(x, i) {
  x[i + 1]
}

`z<-` <- function(x, i, value) {
  x[i + 1] <- value
  x
}

VALID_OP_CODES <- c(1, 2, 99)

STOP_CODE <- 99

# opcode 1
process_op1 <- function(program, i) {
  i1 <- z(program, i + 1) # position to read first num
  i2 <- z(program, i + 2) # position to read second num
  ires <- z(program, i + 3) # position to substitute their sum
  z(program, ires) <- z(program, i1) + z(program, i2)
  program
}

move1 <- function() 4

# opcode 2
process_op2 <- function(program, i) {
  i1 <- z(program, i + 1) # position to read first num
  i2 <- z(program, i + 2) # position to read second num
  ires <- z(program, i + 3) # position to substitute their sum
  z(program, ires) <- z(program, i1) * z(program, i2)
  program
}

move2 <- function() 4

# combine
process_op <- function(program, i) {
  curr_code <- z(program, i)
  stopifnot(curr_code %in% VALID_OP_CODES)
  if (curr_code == 1) {
    process_op1(program, i)
  } else if (curr_code == 2) {
    process_op2(program, i)
  }
}

move <- function(program, i) {
  curr_code <- z(program, i)
  stopifnot(curr_code %in% VALID_OP_CODES)
  if (curr_code == 1) {
    move1()
  } else if (curr_code == 2) {
    move2()
  }
}

# all
process_intcode <- function(program) {
  i <- 0
  while (TRUE) {
    curr_code <- z(program, i)
    if (curr_code == STOP_CODE) break
    mv <- move(program, i)
    program <- process_op(program, i)
    i <- i + mv
  }
  
  program
}

program <- c(1, 0, 0, 3, 99)
process_intcode(program)

program <- c(1,9,10,3,2,3,11,0,99,30,40,50)
process_intcode(program)

process_intcode(c(1,1,1,4,99,5,6,0,99))

process_intcode(code)
process_intcode(c(1,0,0,0,99))
process_intcode(c(2,3,0,3,99))
process_intcode(c(2,4,4,5,99,0))
process_intcode(c(1,1,1,4,99,5,6,0,99))

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
