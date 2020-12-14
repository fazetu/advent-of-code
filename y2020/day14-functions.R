input_mem_n <- function(input) {
  mem_lines <- grep("^mem", input)
  pos <- as.integer(gsub("^mem\\[(\\d+)\\] += +.*$", "\\1", input[mem_lines]))
  max(pos)
}

prep_input_ <- function(input) {
  steps <- lapply(input[-1L], function(step) {
    list(where = as.integer(gsub("^mem\\[(\\d+)\\] += +(.*)$", "\\1", step)),
         value = as.numeric(gsub("^mem\\[(\\d+)\\] += +(.*)$", "\\2", step)))
  })
  
  list(mask = gsub("^mask += +(.*)$", "\\1", input[1L]),
       steps = steps)
}

prep_input <- function(input) {
  brks <- grep("^mask +=", input)
  chunks <- mapply(`:`, brks, c(brks[-1L] - 1L, length(input)), SIMPLIFY = FALSE)
  lapply(chunks, function(chunk) prep_input_(input[chunk]))
}

# bit/num functions
num_to_bit <- function(num, n = 36L) {
  bits <- lapply(num, function(n) rev(as.integer(intToBits(num))))
  vapply(bits, function(b) {
    res <- paste0(b, collapse = "")
    
    if (nchar(res) > n) substr(res, 1, n)
    else if (nchar(res) < n) {
      pad <- rep("0", n - nchar(res))
      paste0(paste0(pad, collapse = ""), res)
    }
  }, character(1L))
}

bit_to_num <- function(bit) {
  bits <- strsplit(bit, "")
  vapply(bits, function(b) {
    pows <- 2 ^ rev(seq_along(b) - 1L)
    sum(as.integer(b) * pows)
  }, numeric(1L))
}

# part 1
apply_mask1 <- function(bit, mask) {
  m <- strsplit(mask, "")[[1]] # should have 1 mask
  bs <- strsplit(bit, "")
  
  vapply(bs, function(b) {
    res <- mapply(function(x, y) ifelse(y == "X", x, y), b, m)
    paste0(unname(res), collapse = "")
  }, character(1))
}

process_command_chunk1 <- function(mem, chunk) {
  mask <- chunk$mask
  steps <- chunk$steps
  
  for (step in steps) {
    curr_bit <- num_to_bit(num = step$value)
    new_bit <- apply_mask1(bit = curr_bit, mask = mask)
    new_val <- bit_to_num(bit = new_bit)
    mem[step$where] <- new_val
  }
  
  mem
}

# part 2
apply_mask2 <- function(bit, mask) {
  m <- strsplit(mask, "")[[1]] # should have 1 mask
  bs <- strsplit(bit, "")
  
  vapply(bs, function(b) {
    res <- mapply(function(x, y) {
      if (y == "0") x
      else if (y == "1") y
      else if (y == "X") y
    }, b, m)
    paste0(unname(res), collapse = "")
  }, character(1))
}

all_bit_combos <- function(bit) {
  bit_vec <- strsplit(bit, "")[[1]]
  # bit_vec has "X" values, replace them with all possible 0/1 combos
  xs <- which(bit_vec == "X")
  if (length(xs) == 0) return(bit)
  npos <- 2 ^ length(xs)
  replace <- expand.grid(replicate(length(xs), c("0", "1"), simplify = FALSE), stringsAsFactors = FALSE)
  res <- replicate(npos, bit_vec, simplify = FALSE)
  
  for (i in seq_len(npos)) {
    res[[i]][xs] <- unlist(replace[i, ])
  }
  
  vapply(res, function(r) paste0(r, collapse = ""), character(1L))
}

process_command_chunk2 <- function(mem, chunk) {
  mask <- chunk$mask
  steps <- chunk$steps
  
  for (step in steps) {
    curr_bit <- num_to_bit(num = step$where)
    new_bit <- apply_mask2(bit = curr_bit, mask = mask)
    pos_bits <- all_bit_combos(bit = new_bit)
    new_val <- bit_to_num(bit = pos_bits)
    
    # expand mem if needed
    mx <- max(new_val)
    if (mx > length(mem)) mem <- c(mem, rep(0, mx - length(mem)))
    
    mem[new_val] <- step$value
  }
  
  mem
}
