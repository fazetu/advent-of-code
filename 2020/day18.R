exprs <- c(
  "1 + 2 * 3 + 4 * 5 + 6",
  "1 + (2 * 3) + (4 * (5 + 6))"
)


parse_expression <- function(expression) {
  if (!grepl("\\(", expression)) return(expression)
  
  pars <- strsplit(expression, "\\(")
}

modified_math_eval <- function(expression) {
  expression <- parse_expression(expression)
  chars <- strsplit(expression, " ")[[1]]
  
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