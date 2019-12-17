times <- c(
  "[1518-11-01 00:00] Guard #10 begins shift",
  "[1518-11-01 00:05] falls asleep",
  "[1518-11-01 00:25] wakes up",
  "[1518-11-01 00:30] falls asleep",
  "[1518-11-01 00:55] wakes up",
  "[1518-11-01 23:58] Guard #99 begins shift",
  "[1518-11-02 00:40] falls asleep",
  "[1518-11-02 00:50] wakes up",
  "[1518-11-03 00:05] Guard #10 begins shift",
  "[1518-11-03 00:24] falls asleep",
  "[1518-11-03 00:29] wakes up",
  "[1518-11-04 00:02] Guard #99 begins shift",
  "[1518-11-04 00:36] falls asleep",
  "[1518-11-04 00:46] wakes up",
  "[1518-11-05 00:03] Guard #99 begins shift",
  "[1518-11-05 00:45] falls asleep",
  "[1518-11-05 00:55] wakes up"
)

library(tidyverse)
library(lubridate)

times <- readLines("Day 4.txt")

rgx <- "^\\[(.*)\\] (.*)$"

times_df <- data.frame(
  datetime = ymd_hm(gsub(rgx, "\\1", times)),
  event = gsub(rgx, "\\2", times),
  stringsAsFactors = FALSE
)
times_df <- times_df[order(times_df$datetime), ]
times_df$curr_guard <- zoo::na.locf(as.numeric(gsub("Guard #(\\d+) .*", "\\1", times_df$event)))
times_df$asleep <- ifelse(stringr::str_detect(times_df$event, "begins shift"), 0,
                          ifelse(stringr::str_detect(times_df$event, "falls asleep"), 1,
                                 ifelse(stringr::str_detect(times_df$event, "wakes up"), 0, NA)))

head(times_df, 10)

times_df
times_df$new_shift <- stringr::str_detect(times_df$event, "begins shift")
times_df

id <- c()
suff <- 0
for (i in 1:nrow(times_df)) {
  suff <- ifelse(times_df$new_shift[i], suff + 1, suff)
  id[i] <- paste0(times_df$curr_guard[i], "_", suff)
}

times_df$id <- id
times_df

shifts <- split(times_df, f = times_df$curr_guard)
shift <- shifts[[1]]

minutes_asleep <- function(shift) {
  minutes <- rep(0, 60)
  
  for (r in 1:nrow(shift)) {
    if (shift$asleep[r] == 1) {
      start_min <- minute(shift$datetime[r])
      end_min <- minute(shift$datetime[r + 1]) - 1
      min_range <- start_min:end_min
      minutes[min_range] <- minutes[min_range] + 1
    }
  }
  
  names(minutes) <- as.character(1:60)
  minutes
}

minutes_asleep(shift)
sleep_times <- lapply(shifts, minutes_asleep)
sleep_times

tots <- sapply(sleep_times, sum)
sleepiest_guard <- names(tots)[tots == max(tots)]
sleepiest_guard_times <- sleep_times$`131`
names(sleepiest_guard_times)[sleepiest_guard_times == max(sleepiest_guard_times)]

131 * 36 # answer 1


max_times_asleep <- sapply(sleep_times, function(sq) {
  max(sq)
})

sleep_times$`2389`

2389 * 49 # answer 2
