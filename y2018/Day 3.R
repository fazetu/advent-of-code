d <- readLines("E:/Coding Practice/R Practice/Advent of Code/Day 3.txt")

head(d)
ids <- gsub("#(\\d+) @ .*: .*", "\\1", d)
coords <- gsub("#\\d+ @ (.*): .*", "\\1", d)
left <- as.numeric(gsub("(\\d+),\\d+", "\\1", coords))
top <- as.numeric(gsub("\\d+,(\\d+)", "\\1", coords))
dims <- gsub("#\\d+ @ .*: (.*)", "\\1", d)
width <- as.numeric(gsub("(\\d+)x\\d+", "\\1", dims))
height <- as.numeric(gsub("\\d+x(\\d+)", "\\1", dims))

d_summary <- data.frame(
  id = ids,
  coord = coords,
  dim = dims,
  left = left,
  top = top,
  width = width,
  height = height,
  stringsAsFactors = FALSE
)

head(d_summary)

min(d_summary$left)
min(d_summary$top)

max(d_summary$left + d_summary$width)
max(d_summary$top + d_summary$height)

fabric_counts <- matrix(rep(0, 1000 * 1000), nrow = 1000, ncol = 1000, byrow = TRUE)
# fabric <- matrix(1:(1000*1000), nrow = 1000, ncol = 1000, byrow = TRUE)
# head(fabric)

fill_fabric <- function(fabric, claim) {
  ids <- gsub("#(\\d+) @ .*: .*", "\\1", claim)
  coords <- gsub("#\\d+ @ (.*): .*", "\\1", claim)
  left_start <- as.numeric(gsub("(\\d+),\\d+", "\\1", coords)) + 1 # want 0's to go to 1
  top_start <- as.numeric(gsub("\\d+,(\\d+)", "\\1", coords)) + 1
  dims <- gsub("#\\d+ @ .*: (.*)", "\\1", claim)
  width <- as.numeric(gsub("(\\d+)x\\d+", "\\1", dims))
  height <- as.numeric(gsub("\\d+x(\\d+)", "\\1", dims))
  
  left_end <- left_start + width - 1
  top_end <- top_start + height - 1

  fabric[top_start:top_end, left_start:left_end] <- fabric[top_start:top_end, left_start:left_end] + 1
  fabric
}

for (claim in d) {
  fabric_counts <- fill_fabric(fabric_counts, claim)
}


sum(fabric_counts > 1) # answer 1

n <- 1000
fabric_ids <- matrix(rep("0", n^2), nrow = n, ncol = n, byrow = TRUE)

# d <- c(
#   "#1 @ 1,3: 4x4",
#   "#2 @ 3,1: 4x4",
#   "#3 @ 5,5: 2x2"
# )

fill_fabric_w_ids <- function(fabric, claim) {
  ids <- gsub("#(\\d+) @ .*: .*", "\\1", claim)
  coords <- gsub("#\\d+ @ (.*): .*", "\\1", claim)
  left_start <- as.numeric(gsub("(\\d+),\\d+", "\\1", coords)) + 1
  top_start <- as.numeric(gsub("\\d+,(\\d+)", "\\1", coords)) + 1
  dims <- gsub("#\\d+ @ .*: (.*)", "\\1", claim)
  width <- as.numeric(gsub("(\\d+)x\\d+", "\\1", dims))
  height <- as.numeric(gsub("\\d+x(\\d+)", "\\1", dims))
  
  left_end <- left_start + width - 1
  top_end <- top_start + height - 1
  
  fabric_section <- fabric[top_start:top_end, left_start:left_end]
  
  if (all(fabric_section == "0")) {
    fabric[top_start:top_end, left_start:left_end] <- ids
  } else if (any(fabric_section == "0")) {
    others <- unique(fabric_section[fabric_section != "0"])
    fabric[fabric %in% others] <- "X"
    fabric[top_start:top_end, left_start:left_end] <- "X"
  } else if (any(fabric_section == "X")) {
    others <- unique(fabric_section[fabric_section != "0"])
    fabric[fabric %in% others] <- "X"
    fabric[top_start:top_end, left_start:left_end] <- "X"
  } else {
    fabric[top_start:top_end, left_start:left_end] <- "X"
  }
  
  fabric
}

for (claim in d) {
  fabric_ids <- fill_fabric_w_ids(fabric_ids, claim)
}

# all but 0's and X's are the answer.
unique(as.vector(fabric_ids)) # answer 2

