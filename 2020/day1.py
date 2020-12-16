# read
with open("day1-input.txt", "r") as f:
    report = f.readlines()

report = [int(val.strip()) for val in report]

# part 1
for i, val in enumerate(report):
    oths = report[:i] + report[(i+1):]
    for oth in oths:
        sm = val + oth
        if sm == 2020:
            print(f"{val} * {oth} = {val * oth}")
            break
    if sm == 2020:
        break

# part 1 alt
from itertools import permutations

perm = list(permutations(report, 2))

for i in perm:
    if sum(i) == 2020:
        print(i[0] * i[1])
        break

# part 2
perm = list(permutations(report, 3))

for i in perm:
    if sum(i) == 2020:
        print(i[0] * i[1] * i[2])
        break
