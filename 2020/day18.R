input <- c(
  "1 + 2 * 3 + 4 * 5 + 6",
  "1 + (2 * 3) + (4 * (5 + 6))"
)

prep_input <- function(input) {
  gsub("\\s+", "", x)
}

# modified math order of operations
modified_math_ooo <- function(expression) {
  chars <- strsplit(expression, "")[[1]]
  
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

fill_parens_ <- function(expresson) {
  chars <- strsplit(expression, "")[[1]]
  
  in_open <- FALSE
  res <- c()
  collect <- c()
  history <- c()
  
  browser()
  
  for (char in chars) {
    if (char == "(" & !in_open) {
      # encountered open paren when not already open
      in_open <- TRUE
      history <- c(history, char)
    } else if (char == ")" & in_open) {
      # encountered close paren when already open
      res <- c(res, modified_math_ooo(paste0(collect, collapse = "")))
      # success, reset everything
      in_open <- FALSE
      collect <- c()
      history <- c()
    } else if (char == "(" & in_open) {
      # encountered open paren when already open
      res <- c(res, history)
      collect <- c()
      history <- c(char)
    } else if (char == ")" & !in_open) {
      # encountered close paren when not open
      # can this happen?
      res <- c(res, ")")
    } else if (in_open) {
      # encountered non-paren when open
      collect <- c(collect, char)
      history <- c(history, char)
    } else if (!in_open) {
      # encountered non-paren when not open
      res <- c(res, char)
    }
  }
  
  paste0(res, collapse = "")
}

fill_parens <- function(expression) {
  while (grepl("\\(", expression)) {
    expression <- fill_parens_(expression)
  }
  
  expression
}

evaluate_expression <- function(expression) {
  modified_math_ooo(expression = fill_parens(expression = expression))
}

expressions <- prep_input(input)

evaluate_expression(expressions[1])
evaluate_expression(expressions[2])



