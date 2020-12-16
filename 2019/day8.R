# 25 pixels wide
# 6  pixels tall
wide <- 25
tall <- 6
img <- as.numeric(strsplit(readLines("2019/day8-input.txt"), "")[[1]])

img_to_layers <- function(img, width, height) {
  layer_pixels <- width * height
  f <- rep(1:(length(img) / layer_pixels), each = layer_pixels)
  layers <- split(img, f)
  layers
}

layers <- img_to_layers(img, wide, tall)
n_0s <- sapply(layers, function(l) sum(l == 0))
layer_least_0s <- layers[[which.min(n_0s)]]
sum(layer_least_0s == 1) * sum(layer_least_0s == 2) # answer part 1

img_to_mats <- function(img, width, height) {
  layers <- img_to_layers(img, width, height)
  lapply(layers, function(l) matrix(l, nrow = height, ncol = width, byrow = TRUE))
}

gen_img <- function(img, width, height) {
  mats <- img_to_mats(img, width, height)
  # first layer is at the front
  final <- mats[[1]]
  
  for (i in 2:length(mats)) {
    add <- mats[[i]]
    # 0 = black
    # 1 = white
    # 2 = transparent
    final[final == 2] <- add[final == 2]
  }
  
  final
}

final <- gen_img(img, wide, tall)
rotate <- function(x) t(apply(x, 2, rev))
image(rotate(final))
