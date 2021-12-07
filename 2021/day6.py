from __future__ import annotations
from typing import List, Optional

class Lanternfish:
    def __init__(self, timer: int):
        self.timer = timer

    def tick(self) -> Optional[Lanternfish]:
        if self.timer == 0:
            self.timer = 6
            return Lanternfish(8)
        else:
            self.timer -= 1
            return None

class School:
    def __init__(self, fish: List[Lanternfish]):
        self.fish = fish

    def all_timers(self) -> List[int]:
        return [fish.timer for fish in self.fish]

    def age(self):
        new_pop = []

        for fish in self.fish:
            new_fish = fish.tick()

            # add the newly aged parent
            new_pop.append(fish)

            # add the new child if there is one
            if new_fish is not None:
                new_pop.append(new_fish)

        self.fish = new_pop

    def age_n(self, n: int, verbose: bool = False):
        for _ in range(n):
            if verbose:
                print(self.all_timers())
            self.age()

# input = [3,4,3,1,2]
input = [3,3,2,1,4,1,1,2,3,1,1,2,1,2,1,1,1,1,1,1,4,1,1,5,2,1,1,2,1,1,1,3,5,1,5,5,1,1,1,1,3,1,1,3,2,1,1,1,1,1,1,4,1,1,1,1,1,1,1,4,1,3,3,1,1,3,1,3,1,2,1,3,1,1,4,1,2,4,4,5,1,1,1,1,1,1,4,1,5,1,1,5,1,1,3,3,1,3,2,5,2,4,1,4,1,2,4,5,1,1,5,1,1,1,4,1,1,5,2,1,1,5,1,1,1,5,1,1,1,1,1,3,1,5,3,2,1,1,2,2,1,2,1,1,5,1,1,4,5,1,4,3,1,1,1,1,1,1,5,1,1,1,5,2,1,1,1,5,1,1,1,4,4,2,1,1,1,1,1,1,1,3,1,1,4,4,1,4,1,1,5,3,1,1,1,5,2,2,4,2,1,1,3,1,5,5,1,1,1,4,1,5,1,1,1,4,3,3,3,1,3,1,5,1,4,2,1,1,5,1,1,1,5,5,1,1,2,1,1,1,3,1,1,1,2,3,1,2,2,3,1,3,1,1,4,1,1,2,1,1,1,1,3,5,1,1,2,1,1,1,4,1,1,1,1,1,2,4,1,1,5,3,1,1,1,2,2,2,1,5,1,3,5,3,1,1,4,1,1,4]
school = School([Lanternfish(timer) for timer in input])

# part 1
school.age_n(80)
len(school.fish) # answer part 1

# part 2
# school = School([Lanternfish(timer) for timer in input])
# school.age_n(256)
# len(school.fish) # answer part 2

# this approach does not work for large numbers, too memory taxing.
# see different approach

########################################################################

# different approach
from typing import List
# input = [3,4,3,1,2]
input = [3,3,2,1,4,1,1,2,3,1,1,2,1,2,1,1,1,1,1,1,4,1,1,5,2,1,1,2,1,1,1,3,5,1,5,5,1,1,1,1,3,1,1,3,2,1,1,1,1,1,1,4,1,1,1,1,1,1,1,4,1,3,3,1,1,3,1,3,1,2,1,3,1,1,4,1,2,4,4,5,1,1,1,1,1,1,4,1,5,1,1,5,1,1,3,3,1,3,2,5,2,4,1,4,1,2,4,5,1,1,5,1,1,1,4,1,1,5,2,1,1,5,1,1,1,5,1,1,1,1,1,3,1,5,3,2,1,1,2,2,1,2,1,1,5,1,1,4,5,1,4,3,1,1,1,1,1,1,5,1,1,1,5,2,1,1,1,5,1,1,1,4,4,2,1,1,1,1,1,1,1,3,1,1,4,4,1,4,1,1,5,3,1,1,1,5,2,2,4,2,1,1,3,1,5,5,1,1,1,4,1,5,1,1,1,4,3,3,3,1,3,1,5,1,4,2,1,1,5,1,1,1,5,5,1,1,2,1,1,1,3,1,1,1,2,3,1,2,2,3,1,3,1,1,4,1,1,2,1,1,1,1,3,5,1,1,2,1,1,1,4,1,1,1,1,1,2,4,1,1,5,3,1,1,1,2,2,2,1,5,1,3,5,3,1,1,4,1,1,4]

# number of fish that are currently at age i
age_counts = [0 for _ in range(9)] # fish can only be age 0-8

# set up initial age counts from input
for f in input:
    age_counts[f] += 1

def age(age_counts: List[int]) -> List[int]:
    # this decreases the age timer for each fish
    nzero = age_counts[0] # number of fish currently aged 0
    res = age_counts[1:] # this moves fish down 1 age
    res[6] += nzero # this resets those that just gave birth to age 6
    res.append(nzero) # this adds babies to age 8
    return res

def age_n(age_counts: List[int], n: int, verbose: bool = False) -> List[int]:
    # run age n times
    for _ in range(n):
        if verbose:
            print(age_counts)
        age_counts = age(age_counts)

    return age_counts

# part 1
sum(age_n(age_counts, 80)) # answer part 1

# part 2
sum(age_n(age_counts, 256)) # answer part 2
