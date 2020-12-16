import re

with open("day2-input.txt", "r") as f:
    input = f.readlines()

input = [i.strip() for i in input]

srch = re.compile("^(\\d+)-(\\d+) (\\w): (\\w+)$")
groups = [srch.match(i).groups() for i in input]
idx = range(len(input))

# part 1
def is_valid_parts1(parts):
    f, l, let, pw = parts
    times = sum([char.find(let) != -1 for char in pw])
    return int(f) <= times <= int(l)

valid1 = {input[i]: is_valid_parts1(groups[i]) for i in idx}
sum(valid1.values()) # answer 1

# part 2
def is_valid_parts2(parts):
    f, l, let, pw = parts
    f_i = int(f) - 1
    l_i = int(l) - 1
    return ((pw[f_i] == let) & (pw[l_i] != let)) | ((pw[f_i] != let) & (pw[l_i] == let))

valid2 = {input[i]: is_valid_parts2(groups[i]) for i in idx}
sum(valid2.values()) # answer 2
