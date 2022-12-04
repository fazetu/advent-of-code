from typing import Set, Tuple
from utils import read_input


# input = [
#     "2-4,6-8",
#     "2-3,4-5",
#     "5-7,7-9",
#     "2-8,3-7",
#     "6-6,4-6",
#     "2-6,4-8",
# ]

input = read_input(4)

# common
def assigned_sections(rng: str) -> Set[int]:
    start, end = rng.split("-")
    return set(range(int(start), int(end) + 1))


def pairs_sections(pair: str) -> Tuple[Set[int], Set[int]]:
    a, b = pair.split(",")
    return (assigned_sections(a), assigned_sections(b))


# part 1
count = 0

for pair in input:
    sections1, sections2 = pairs_sections(pair)
    diff1 = sections1 - sections2
    diff2 = sections2 - sections1

    if (len(diff1) == 0) or len(diff2) == 0:
        count += 1

# answer 1
print(count)

# part 2
count = 0

for pair in input:
    sections1, sections2 = pairs_sections(pair)
    overlap = sections1.intersection(sections2)

    if len(overlap) > 0:
        count += 1

# answer 2
print(count)
