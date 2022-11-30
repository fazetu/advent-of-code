from typing import List

# test input
input = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]

# read input
with open("day1-input.txt", "r") as file:
    _input = file.readlines()

input = [int(line.strip()) for line in _input]

# part 1
def count_increases(input: List[int]) -> int:
    n = 0

    # skip 0 index since we compare backwards
    for i in range(1, len(input)):
        n += (input[i - 1] < input[i])

    return n

count_increases(input) # part 1 answer

# part 2
def make_window_sums(input: List[int], window_size: int = 3) -> List[int]:
    res = []

    for i in range(len(input) - window_size + 1):
        slice = input[i:(i + window_size)]
        res.append(sum(slice))

    return res

count_increases(make_window_sums(input)) # part 2 answer
