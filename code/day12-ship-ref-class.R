library(R6)

get_action <- function(command) gsub("^([NSEWLRF])(\\d+)$", "\\1", command)

get_value <- function(command) as.integer(gsub("^([NSEWLRF])(\\d+)$", "\\2", command))

Ship <- R6Class(classname = "Ship", public = list(
  start_x = NA, # east/west position
  start_y = NA, # north/south position
  curr_x = NA,
  curr_y = NA,
  direction = NA,
  DEGREES = c("N" = 0L, "E" = 90L, "S" = 180L, "W" = 270L),
  initialize = function(start_x = 0L, start_y = 0L, direction = "E") {
    self$start_x <- start_x
    self$start_y <- start_y
    self$curr_x <- start_x
    self$curr_y <- start_y
    self$direction <- direction
    invisible(self)
  },
  move_forward = function(by) {
    if (self$direction == "N") self$curr_y <- self$curr_y + by
    else if (self$direction == "S") self$curr_y <- self$curr_y - by
    else if (self$direction == "E") self$curr_x <- self$curr_x + by
    else if (self$direction == "W") self$curr_x <- self$curr_x - by
    invisible(self)
  },
  move_direction = function(direction, by) {
    curr_direction <- self$direction
    self$direction <- direction
    self$move_forward(by = by)
    self$direction <- curr_direction
    invisible(self)
  },
  turn = function(lr, degrees) {
    deg <- (self$DEGREES[self$direction] + ifelse(lr == "L", -degrees, degrees)) %% 360
    self$direction <- names(self$DEGREES)[self$DEGREES == deg]
    invisible(self)
  },
  move = function(command) {
    action <- get_action(command)
    value <- get_value(command)
    
    if (action %in% c("N", "S", "E", "W")) {
      self$move_direction(direction = action, by = value)
    } else if (action %in% c("L", "R")) {
      self$turn(lr = action, degrees = value)
    } else if (action == "F") {
      self$move_forward(by = value)
    }
    
    invisible(self)
  },
  # methods that do not return self
  start_position = function() {
    c(x = self$start_x, y = self$start_y)
  },
  current_position = function() {
    c(x = self$curr_x, y = self$curr_y)
  },
  manhattan_distance = function() {
    sum(abs(self$current_position() - self$start_position()))
  }
))

Waypoint <- R6Class(classname = "Waypoint", public = list(
  rel_x = NA,
  rel_y = NA,
  initialize = function(rel_x = 10L, rel_y = 1L) {
    self$rel_x <- rel_x
    self$rel_y <- rel_y
    invisible(self)
  },
  move_direction = function(direction, by) {
    if (direction == "N") self$rel_y <- self$rel_y + by
    else if (direction == "S") self$rel_y <- self$rel_y - by
    else if (direction == "E") self$rel_x <- self$rel_x + by
    else if (direction == "W") self$rel_x <- self$rel_x - by
    invisible(self)
  },
  rotate = function(lr, degree) {
    # degrees to rotate clock wise
    cw_degree <- ifelse(lr == "L", -degree, degree) %% 360
    
    if (cw_degree == 90) {
      rel_x_ <- self$rel_x
      self$rel_x <- self$rel_y
      self$rel_y <- -rel_x_
    } else if (cw_degree == 180) {
      self$rel_x <- -self$rel_x
      self$rel_y <- -self$rel_y
    } else if (cw_degree == 270) {
      rel_x_ <- self$rel_x
      self$rel_x <- -self$rel_y
      self$rel_y <- rel_x_
    }

    invisible(self)
  },
  relative_position = function() {
    c(x = self$rel_x, y = self$rel_y)
  }
))

# a ship with a waypoint
ShipWaypoint <- R6Class(classname = "ShipWaypoint", inherit = Ship, public = list(
  waypoint = NA,
  initialize = function(start_x = 0L, start_y = 0L, direction = "E", rel_x = 10, rel_y = 1) {
    super$initialize(start_x = start_x, start_y = start_y, direction = direction)
    self$waypoint <- Waypoint$new(rel_x = rel_x, rel_y = rel_y)
    invisible(self)
  },
  move_to_waypoint = function(by) {
    # move towards the waypoint by number of times
    move_by <- by * self$waypoint$relative_position()
    self$curr_x <- unname(self$curr_x + move_by["x"])
    self$curr_y <- unname(self$curr_y + move_by["y"])
    invisible(self)
  },
  move = function(command) {
    action <- get_action(command)
    value <- get_value(command)
    
    if (action %in% c("N", "S", "E", "W")) {
      self$waypoint$move_direction(direction = action, by = value)
    } else if (action %in% c("L", "R")) {
      self$waypoint$rotate(lr = action, degree = value)
    } else if (action == "F") {
      self$move_to_waypoint(by = value)
    }
    
    invisible(self)
  },
  # methods that do not return self
  current_ship_position = function() {
    super$current_position()
  },
  current_waypoint_position = function() {
    self$current_ship_position() + self$waypoint$relative_position()
  }
))
