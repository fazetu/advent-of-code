z <- function(x, i) {
  x[i + 1]
}

`z<-` <- function(x, i, value) {
  x[i + 1] <- value
  x
}

move <- function(op_code) {
  if (op_code %in% c(1, 2, 7, 8)) 4
  else if (op_code %in% c(3, 4)) 2
  else if (op_code %in% c(5, 6)) 3
}

op1 <- function(x, start, modes) {
  mode1 <- modes[1]
  mode2 <- modes[2]
  j1 <- ifelse(mode1 == 0, z(x, start + 1), start + 1)
  j2 <- ifelse(mode2 == 0, z(x, start + 2), start + 2)
  val1 <- z(x, j1)
  val2 <- z(x, j2)
  jres <- z(x, start + 3)
  z(x, jres) <- val1 + val2
  x
}

op2 <- function(x, start, modes) {
  mode1 <- modes[1]
  mode2 <- modes[2]
  j1 <- ifelse(mode1 == 0, z(x, start + 1), start + 1)
  j2 <- ifelse(mode2 == 0, z(x, start + 2), start + 2)
  val1 <- z(x, j1)
  val2 <- z(x, j2)
  jres <- z(x, start + 3)
  z(x, jres) <- val1 * val2
  x
}

op3 <- function(x, start, input, modes) {
  mode <- modes[1]
  j <- ifelse(mode == 0, z(x, start + 1), start + 1)
  z(x, j) <- input
  x
}

op4 <- function(x, start, modes) {
  mode <- modes[1]
  j <- ifelse(mode == 0, z(x, start + 1), start + 1)
  z(x, j)
}

op5 <- function(x, start, modes) {
  mode1 <- modes[1]
  mode2 <- modes[2]
  j1 <- ifelse(mode1 == 0, z(x, start + 1), start + 1)
  j2 <- ifelse(mode2 == 0, z(x, start + 2), start + 2)
  val1 <- z(x, j1)
  val2 <- z(x, j2)
  ifelse(val1 != 0, val2, start + move(5))
}

op6 <- function(x, start, modes) {
  mode1 <- modes[1]
  mode2 <- modes[2]
  j1 <- ifelse(mode1 == 0, z(x, start + 1), start + 1)
  j2 <- ifelse(mode2 == 0, z(x, start + 2), start + 2)
  val1 <- z(x, j1)
  val2 <- z(x, j2)
  ifelse(val1 == 0, val2, start + move(6))
}

op7 <- function(x, start, modes) {
  mode1 <- modes[1]
  mode2 <- modes[2]
  j1 <- ifelse(mode1 == 0, z(x, start + 1), start + 1)
  j2 <- ifelse(mode2 == 0, z(x, start + 2), start + 2)
  val1 <- z(x, j1)
  val2 <- z(x, j2)
  resj <- z(x, start + 3)
  resval <- ifelse(val1 < val2, 1, 0)
  z(x, resj) <- resval
  x
}

op8 <- function(x, start, modes) {
  mode1 <- modes[1]
  mode2 <- modes[2]
  j1 <- ifelse(mode1 == 0, z(x, start + 1), start + 1)
  j2 <- ifelse(mode2 == 0, z(x, start + 2), start + 2)
  val1 <- z(x, j1)
  val2 <- z(x, j2)
  resj <- z(x, start + 3)
  resval <- ifelse(val1 == val2, 1, 0)
  z(x, resj) <- resval
  x
}

decode_opcode <- function(num) {
  num_str <- as.character(num)
  zeros <- paste0(rep("0", 5 - nchar(num_str)), collapse = "")
  num_str <- paste0(zeros, num_str, collapse = "") # pad with 0's
  
  s <- strsplit(num_str, "")[[1]]
  srev <- rev(s)
  
  op_code <- rev(srev[1:2])
  op_code <- as.numeric(paste0(op_code, collapse = ""))
  mode1 <- as.numeric(srev[3])
  mode2 <- as.numeric(srev[4])
  mode3 <- as.numeric(srev[5])
  
  list(op_code = op_code, modes = c(mode1, mode2, mode3))
}

process_intcode <- function(program, input) {
  if (program[1] == 3 & missing(input)) stop("Need input")
  res <- c()
  i <- 0
  while (TRUE) {
    first <- z(program, i)
    l <- decode_opcode(first)
    op_code <- l$op_code
    modes <- l$modes
    print(i)
    
    if (op_code == 99) {
      break
    } else if (op_code == 1) {
      program <- op1(program, i, modes)
      i <- i + move(op_code)
    } else if (op_code == 2) {
      program <- op2(program, i, modes)
      i <- i + move(op_code)
    } else if (op_code == 3) {
      program <- op3(program, i, input, modes)
      i <- i + move(op_code)
    } else if (op_code == 4) {
      out <- op4(program, i, modes)
      res <- c(res, out)
      i <- i + move(op_code)
    } else if (op_code == 5) {
      i <- op5(program, i, modes)
    } else if (op_code == 6) {
      i <- op6(program, i, modes)
    } else if (op_code == 7) {
      program <- op7(program, i, modes)
      i <- i + move(op_code)
    } else if (op_code == 8) {
      program <- op8(program, i, modes)
      i <- i + move(op_code)
    }
  }
  
  list(program = program, res = res)
}

# part 1
input <- readLines("2019/day5-input.txt")
input <- as.numeric(strsplit(input, ",")[[1]])
res <- process_intcode(input, 1)
tail(res$res, 1) # answer

# part 2
res <- process_intcode(input, 5)
res$res # answer
