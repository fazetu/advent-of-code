library(tidyverse)
source("2020/day11-functions.R")

input <- c(
  "L.LL.LL.LL",
  "LLLLLLL.LL",
  "L.L.L..L..",
  "LLLL.LL.LL",
  "L.LL.LL.LL",
  "L.LLLLL.LL",
  "..L.L.....",
  "LLLLLLLLLL",
  "L.LLLLLL.L",
  "L.LLLLL.LL"
)

m <- input_to_matrix(input)

plot_seats <- function(m) {
  df <- as.data.frame(m)
  cnms <- as.character(1:ncol(df))
  colnames(df) <- cnms
  
  df %>% 
    mutate(y = nrow(.) - row_number() + 1) %>% 
    pivot_longer(cnms, names_to = "x") %>% 
    mutate(x = as.integer(x),
           value = factor(value, levels = c(".", "L", "#"))) %>% 
    ggplot() + 
    geom_tile(aes(x = x, y = y, fill = value)) +
    scale_fill_manual(values = c("." = "white", "L" = "lightgreen", "#" = "pink")) +
    guides(fill = FALSE) +
    theme_void()
}

plot_iters2 <- function(m, occupied_tolerance = 5L, delay_sec = 1L) {
  prev_m <- m
  print(plot_seats(m))
  Sys.sleep(delay_sec)
  
  while (TRUE) {
    m <- run_iter2(m, occupied_tolerance = occupied_tolerance)
    print(plot_seats(m))
    Sys.sleep(delay_sec)
    if (all(prev_m == m)) break
    prev_m <- m
  }
  
  m
}

plot_iters2(m, 5L)

m <- input_to_matrix(readLines("2020/day11-input.txt"))
m_final <- plot_iters2(m, 5L)
