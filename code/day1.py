from typing import List
from utils import read_input

input = read_input(1)

calories: List[int] = []
i = 0

for line in input:
    if line == "":
        i += 1
    else:
        calorie = int(line)
        if len(calories) == (i + 1):
            # still on the same elf
            calories[i] += calorie
        else:
            # haven't seen this, new elf
            calories.append(calorie)

calories.sort(reverse=True)

# answer 1
print(calories[0])

# answer 2
print(sum(calories[:3]))
