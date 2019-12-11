# part1

# helpers
# make zero indexing easier
z <- function(x, i) {
  x[i + 1]
}

`z<-` <- function(x, i, value) {
  x[i + 1] <- value
  x
}

VALID_OP_CODES <- c(1, 2, 3, 4, 5, 6, 7, 8, 99)

STOP_CODE <- 99

# opcode 1
process_op1 <- function(program, i, modes = c(0, 0)) {
  # for parameter 1
  mode1 <- modes[1]
  
  if (mode1 == 0) { # positional mode
    j1 <- z(program, i + 1) # position to read first num
    val1 <- z(program, j1)
  } else if (mode1 == 1) { # immediate mode
    val1 <- z(program, i + 1)
  }
  
  # for parameter 2
  mode2 <- modes[2]
  
  if (mode2 == 0) { # positional mode
    j2 <- z(program, i + 2)
    val2 <- z(program, j2)
  } else if (mode2 == 1) { # immediate mode
    val2 <- z(program, i + 2)
  }
  
  ires <- z(program, i + 3) # position to substitute their sum
  z(program, ires) <- val1 + val2
  program
}

# opcode 2
process_op2 <- function(program, i, modes = c(0, 0)) {
  # for parameter 1
  mode1 <- modes[1]
  
  if (mode1 == 0) { # positional mode
    j1 <- z(program, i + 1) # position to read first num
    val1 <- z(program, j1)
  } else if (mode1 == 1) { # immediate mode
    val1 <- z(program, i + 1)
  }
  
  # for parameter 2
  mode2 <- modes[2]
  
  if (mode2 == 0) { # positional mode
    j2 <- z(program, i + 2)
    val2 <- z(program, j2)
  } else if (mode2 == 1) { # immediate mode
    val2 <- z(program, i + 2)
  }
  
  ires <- z(program, i + 3) # position to substitute their sum
  z(program, ires) <- val1 * val2
  program
}

# opcode 3
process_op3 <- function(program, i, input, modes = 0) {
  mode <- modes[1]
  
  if (mode == 0) {
    j <- z(program, i + 1)
    z(program, j) <- input
  } else if (mode == 1) {
    z(program, i + 1) <- input
  }
  
  program
}

# opcode 4
process_op4 <- function(program, i, modes = 0) {
  mode <- modes[1]
  
  if (mode == 0) {
    j <- z(program, i + 1)
    z(program, j)
  } else if (mode == 1) {
    z(program, i + 1)
  }
}

# opcode 5
process_op5 <- function(program, i, modes = 0) {
  mode <- modes[0]
  
  if (mode == 0) {
    j1 <- z(program, i + 1)
    val1 <- z(program, j1)
  } else if (mode == 1) {
    val <- z(program, i + 1)
  }
  
  
}

# combine
process_op <- function(program, op_code, i, modes, input) {
  stopifnot(op_code %in% VALID_OP_CODES)
  
  if (op_code == 1) {
    process_op1(program, i, modes)
  } else if (op_code == 2) {
    process_op2(program, i, modes)
  } else if (op_code == 3) {
    process_op3(program, i, input, modes)
  } else if (op_code == 4) {
    process_op4(program, i, modes)
  }
}

move <- function(op_code) {
  stopifnot(op_code %in% VALID_OP_CODES)
  
  if (op_code %in% c(1, 2)) {
    4
  } else if (op_code %in% c(3, 4)) {
    2
  }
}

# all
parse_4digit_opcode <- function(num) {
  # pad with 0's
  num_str <- as.character(num)
  zeros <- paste0(rep("0", 5 - nchar(num_str)), collapse = "")
  num_str <- paste0(zeros, num_str, collapse = "")
  
  s <- strsplit(num_str, "")[[1]]
  srev <- rev(s)
  
  op_code <- rev(srev[1:2])
  op_code <- as.numeric(paste0(op_code, collapse = ""))
  mode1 <- as.numeric(srev[3])
  mode2 <- as.numeric(srev[4])
  mode3 <- as.numeric(srev[5])
  
  list(
    op_code = op_code,
    mode1 = mode1,
    mode2 = mode2,
    mode3 = mode3
  )
}

process_intcode <- function(program, input) {
  res <- c()
  i <- 0
  while (TRUE) {
    op_code <- z(program, i)
    inst <- parse_4digit_opcode(op_code)
    
    curr_code <- inst[[1]]
    modes <- unlist(inst[-1])
    
    if (curr_code == STOP_CODE) { # 99
      break
    }
    
    if (curr_code == 4) { # output code
      res <- c(res, process_op(program, 4, i, modes, input))
    } else {
      program <- process_op(program, curr_code, i, modes, input)
    }
    
    i <- i + move(curr_code)
  }
  
  res
}

input <- readLines("2019/day5-input.txt")
input <- as.numeric(strsplit(input, ",")[[1]])

res <- process_intcode(input, 1)
tail(res, 1) # answer

# part 2
