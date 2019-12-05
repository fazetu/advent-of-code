op_code_one <- function(x, i) {
  ai <- x[i + 2] + 1
  bi <- x[i + 3] + 1
  resi <- x[i + 4] + 1
  x[resi] <- x[ai] + x[bi]
  x
}

op_code_two <- function(x, i) {
  ai <- x[i + 2] + 1
  bi <- x[i + 3] + 1
  resi <- x[i + 4] + 1
  x[resi] <- x[ai] * x[bi]
  x
}

op_code_three <- function(x, i, input) {
  inputi <- x[i + 2] + 1
  x[inputi] <- input
  x
}

op_code_four <- function(x, i) {
  outputi <- x[i + 2] + 1
  x[outputi]
}

op_code <- function(x, op, i, input) {
  if (op == 1) op_code_one(x, i)
  else if (op == 2) op_code_two(x, i)
  else if (op == 3) op_code_three(x, i, input)
  else if (op == 4) op_code_four(x, i)
}

move <- function(op) {
  if (op == 1) 4
  else if (op == 2) 4
  else if (op == 3) 2
  else if (op == 4) 2
}

# Intcode computer
process_code <- function(code) {
  n <- length(code)
  i <- 1
  
  while(TRUE) {
    op <- code[i]
    if (op == 99) break
    code <- op_code(code, op, i - 1, NA)
    i <- i + move(op)
  }
  
  code
}

process_code(c(1,0,0,0,99))
process_code(c(2,3,0,3,99))
process_code(c(2,4,4,5,99,0))
process_code(c(1,1,1,4,99,5,6,0,99))
