from typing import List, Set, Tuple
import string
from functools import reduce
from utils import read_input

# input = [
#     "vJrwpWtwJgWrhcsFMMfFFhFp",
#     "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
#     "PmmdzqPrVvPwwTWBwg",
#     "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
#     "ttgJtRGJQctTZtZT",
#     "CrZsJsPPZsGzwwsLwLmpwMDw",
# ]

input = read_input(3)

# common
def item_priority(item: str) -> int:
    if item in string.ascii_lowercase:
        return string.ascii_lowercase.find(item) + 1

    if item in string.ascii_uppercase:
        return string.ascii_uppercase.find(item) + 27

    raise ValueError(f"Invalid item: {item}")


def common_items(groups: List[str]) -> Set[str]:
    return reduce(lambda x, y: x.intersection(y), map(set, groups))


def common_item(groups: List[str]) -> str:
    common = common_items(groups)

    if len(common) == 1:
        return list(common)[0]
    else:
        raise ValueError(f"Found more than 1 item in common: {common}")


# part 1
def split_rucksack(rucksack: str) -> List[str]:
    half = int(len(rucksack) / 2)
    return [rucksack[:half], rucksack[half:]]


# answer 1
priorities = [
    item_priority(common_item(split_rucksack(rucksack))) for rucksack in input
]
print(sum(priorities))

# part 2
GROUP_SIZE = 3


def create_group_i(rucksacks: List[str], i: int) -> List[str]:
    # [0:3] => 0, 1, 2
    # [3:6] => 3, 4, 5
    # [6:9] => 6, 7, 8
    start = GROUP_SIZE * i
    end = start + GROUP_SIZE
    return rucksacks[start:end]


def create_groups(rucksacks: List[str]) -> List[List[str]]:
    n_groups = int(len(rucksacks) / GROUP_SIZE)
    groups = [create_group_i(rucksacks, i) for i in range(n_groups)]
    return groups


# answer 2
priorities = [
    item_priority(common_item(group)) for group in create_groups(input)
]
print(sum(priorities))
