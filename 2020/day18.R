exprs <- c(
  "1 + 2 * 3 + 4 * 5 + 6",
  "1 + (2 * 3) + (4 * (5 + 6))"
)

# modified math order of operations
modified_math_ooo <- function(expression) {
  chars <- strsplit(gsub("\\s+", "", expression), "")[[1]]
  
  ans <- as.numeric(chars[1])
  
  for (char in chars[-1]) {
    if (char %in% c("+", "*")) {
      op <- switch(char, "+" = `+`, "*" = `*`)
    } else {
      ans <- op(ans, as.numeric(char))
    }
  }
  
  ans
}

fill_parens <- function(expresson) {
  expression <- gsub("\\s+", "", expression)
  chars <- strsplit(expression, "\\(")[[1]]
  
  for (char in chars) {
    
  }
  
  
  paren_groups <- strsplit(expression, "\\(")
}

modified_math_ooo(exprs[1])
