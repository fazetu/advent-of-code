setwd("F:/advent-of-code/")

# helpers
rng_to_int <- function(x) {
  lapply(strsplit(x, "-"), function(i) {
    as.integer(i[1]):as.integer(i[2])
  })
}

parse_ranges <- function(ranges) {
  info <- strsplit(ranges, ": +")
  attributes <- vapply(info, function(i) i[1], character(1L))
  rngs <- lapply(strsplit(vapply(info, function(i) i[2], character(1L)), " +or +"), function(l) {
    sort(unique(unlist(rng_to_int(l))))
  })
  names(rngs) <- attributes
  rngs
}

invalid_ticket_numbers <- function(tickets, parsed_ranges) {
  tickets_num <- lapply(strsplit(tickets, ","), as.integer)
  all_valid_nums <- unique(unlist(parsed_ranges))
  lapply(tickets_num, function(ticket) ticket[!ticket %in% all_valid_nums])
}

possible_attributes <- function(ticket) {
  ticket_num <- as.integer(strsplit(ticket, ",")[[1]])
  lapply(ticket_num, function(num) {
    works <- vapply(parsed_ranges, function(rng) num %in% rng, logical(1L))
    names(parsed_ranges)[works]
  })
}

# parse input
input <- readLines("2020/day16-input.txt")

ranges <- input[1L:(min(grep("^$", input)) - 1L)]
your_ticket <- input[(min(grep("^$", input)) + 2L):(max(grep("^$", input)) - 1L)]
nearby_tickets <- input[(max(grep("^$", input)) + 2L):length(input)]

parsed_ranges <- parse_ranges(ranges)
inv_nums <- invalid_ticket_numbers(nearby_tickets, parsed_ranges)

# part 1
sum(unlist(inv_nums)) # answer 1

# part 2
valid_tickets <- nearby_tickets[vapply(inv_nums, function(x) length(x) == 0L, logical(1L))]

pos_atts <- lapply(valid_tickets, possible_attributes)

uniq_pos_atts <- lapply(seq_len(length(parsed_ranges)), function(i) {
  ith_pos_atts <- lapply(pos_atts, function(atts) atts[[i]])
  Reduce(intersect, ith_pos_atts)
})

key <- c()

while (TRUE) {
  ls <- lengths(uniq_pos_atts)
  i <- which(ls == 1L)
  if (length(i) == 0L) break
  nm <- uniq_pos_atts[[i]]
  key <- c(key, setNames(i, nm))
  
  # remove it
  uniq_pos_atts <- lapply(uniq_pos_atts, function(atts) {
    setdiff(atts, nm)
  })
}

departure_pos <- key[grep("^departure", names(key))]
options(scipen = 100)
prod(as.integer(strsplit(your_ticket, ",")[[1]])[departure_pos]) # answer 2
