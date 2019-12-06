# x Intcode
# i 0-index of where to start processing
# op Function to apply to the second and third elements of x[(i + 1):(i + 4)]
# parameter mode Which mode to use. 0 is positional, 1 is immediate.
op_code_group4 <- function(x, i, op = `+`, mode = 0) {
  xsection <- x[(i + 1):(i + 4)]
  
  if (mode == 0) { # positional mode
    i1 <- xsection[2] + 1 # + 1 to convert to 1 index
    i2 <- xsection[3] + 1
    resi <- xsection[4] + 1
    x[resi] <- op(x[i1], x[i2])
  } else if (mode == 1) {
    
  }
  
  x
}

op_code_one <- function(x, i, mode = 0) op_code_group4(x, i, op = `+`, mode = mode)

op_code_two <- function(x, i, mode = 0) op_code_group4(x, i, op = `*`, mode = mode)

op_code_three <- function(x, i, input, mode = 0) {
  xsection <- x[(i + 1):(i + 2)]
  
  if (mode == 0) {
    resi <- xsection[2] + 1
    x[resi] <- input
  } else if (mode == 1) {
    
  }
  
  x
}

op_code_four <- function(x, i, mode = 0) {
  xsection <- x[(i + 1):(i + 2)]
  
  if (mode == 0) {
    resi <- xsection[2] + 1
    out <- x[resi]
  } else if (mode == 1) {
    out <- xsection[2]
  }
  
  out
}

op_code <- function(x, op, i, mode = 0, input) {
  if (op == 1) op_code_one(x, i, mode)
  else if (op == 2) op_code_two(x, i, mode)
  else if (op == 3) op_code_three(x, i, mode, input)
  else if (op == 4) op_code_four(x, i, mode)
}

move <- function(op) {
  if (op == 1) 4
  else if (op == 2) 4
  else if (op == 3) 2
  else if (op == 4) 2
}

# Intcode computer
process_code <- function(code, mode = 0) {
  n <- length(code)
  i <- 1
  
  while(TRUE) {
    op <- code[i]
    if (op == 99) break
    code <- op_code(x = code, op = op, i = i - 1, mode = mode, input = NA)
    i <- i + move(op = op)
  }
  
  code
}

process_code(c(1,0,0,0,99))
process_code(c(2,3,0,3,99))
process_code(c(2,4,4,5,99,0))
process_code(c(1,1,1,4,99,5,6,0,99))
