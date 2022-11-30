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

process_intcode <- function(program, inputs) {
  if (program[1] == 3 & missing(inputs)) stop("Need input")
  res <- c()
  i <- 0
  input_i <- 1
  
  while (TRUE) {
    #if (any(is.na(program))) browser()
    #if (i == 22) browser()
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
      program <- op3(program, i, inputs[input_i], modes)
      input_i <- input_i + 1
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

amps <- function(program, phase, startv = 0) {
  v2 <- startv
  
  for (v1 in phase) {
    out <- process_intcode(program, inputs = c(v1, v2))
    program <- out$program
    v2 <- out$res
  }
  
  list(program = program, val = v2)
}

amps_phase_combos <- function(program, all_phases) {
  # phases are 0 to 4 - not used twice
  res <- apply(all_phases, 1, function(row) amps(program, row)$val)
  res <- cbind(all_phases, res)
  colnames(res) <- c("A", "B", "C", "D", "E", "Val")
  res
}

amps_phase_combos_feedback <- function(program, all_phases) {
  res <- apply(all_phases, 1, function(row) {
    out <- amps(program, row, 0)
    program <- out$program
    val <- out$val
    amps(program, row, val)
  })
  res <- cbind(all_phases, res)
  colnames(res) <- c("A", "B", "C", "D", "E", "Val")
  res
}

# part 1
all_phases <- gtools::permutations(n = 5, r = 5, v = 0:4)

program <- c(3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0)
res <- amps_phase_combos(program, all_phases)
res[which.max(res[, "Val"]), ]

program <- c(3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0)
res <- amps_phase_combos(program, all_phases)
res[which.max(res[, "Val"]), ]

program <- c(3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0)
res <- amps_phase_combos(program, all_phases)
res[which.max(res[, "Val"]), ]

input <- readLines("2019/day7-input.txt")
program <- as.numeric(strsplit(input, ",")[[1]])
res <- amps_phase_combos(program, all_phases)
res[which.max(res[, "Val"]), ] # answer in Val column

# part 2
all_phases <- gtools::permutations(n = 5, r = 5, v = 5:9)

program <- c(3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5)
res <- amps_phase_combos_feedback(program, all_phases)
res[which.max(res[, "Val"]), ]
