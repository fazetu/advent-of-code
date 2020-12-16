# process the input strings to return a named list
# keys are the colors of bags
# values are named vectors of how many of other bags the key can contain
# names of named vectors are colors and values are how many
# if a key has NULL as the value that colored bag doesn't contain other bags
prep_input <- function(input) {
  input <- gsub("\\.", "", input)
  bags <- gsub("^(.*) bags contain (.*)$", "\\1", input)
  contains <- strsplit(gsub("^(.*) bags contain (.*)$", "\\2", input), ", ")
  contains <- lapply(contains, function(x) {
    if (all(x == "no other bags")) return(NULL)
    amt <- as.integer(gsub("^(\\d+) (.*) bags?", "\\1", x))
    color <- gsub("^(\\d+) (.*) bags?", "\\2", x)
    setNames(amt, color)
  })
  names(contains) <- bags
  contains
}

# get the vector of colored bags that is inside the given colored bag
inside_color <- function(color, contains) contains[[color]]

# get the names of the colors that a given colored bag can contain
# returns NULL if no colors inside the given colored bag
colors_inside_color <- function(color, contains) names(inside_color(color, contains))

# get the color of bags that can contain a given color
# returns NULL if the given colored bag is not contained in other colored bags
colors_color_can_be_inside <- function(color, contains) {
  can_be_inside <- vapply(contains, function(x) {
    if (is.null(x)) return(FALSE)
    color %in% names(x)
  }, logical(1))
  
  if (!any(can_be_inside)) return(NULL)
  names(contains)[can_be_inside]
}

# get all of the colored bags that a given colored bag can be inside of
# there can be duplicates depending on the path taken
all_colors_color_can_be_inside <- function(color, contains) {
  cols <- colors_color_can_be_inside(color, contains)
  
  if (is.null(cols)) {
    return(cols)
  } else {
    c(cols, unlist(lapply(cols, all_colors_color_can_be_inside, contains = contains)))
  }
}

# count number of bags that are inside a given colored bag
rec_count_bags <- function(color, count, contains) {
  inside <- inside_color(color = color, contains = contains)
  
  if (is.null(inside)) {
    return(count)
  } else {
    counts <- count * inside
    res <- vapply(names(inside), function(col) {
      rec_count_bags(color = col, count = unname(counts[col]), contains = contains)
    }, integer(1))
    
    return(sum(count, res))
  }
}
