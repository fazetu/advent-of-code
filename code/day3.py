from typing import List, Dict, Tuple
import os

os.chdir("C:/Projects/advent-of-code/2021")

small_input = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]

with open("day3-input.txt", "r") as f:
    _input = f.readlines()

input = [line.strip() for line in _input]

# part 1
def positions_count_ones(numbers: List[str]) -> Dict[int, int]:
    """Go through all numbers and count how many 1s are found in each position."""
    bit_size = len(numbers[0])
    ones_count = {i: 0 for i in range(bit_size)}

    for number in numbers:
        for pos, bit in enumerate(number):
            ones_count[pos] += bit == "1"
    return ones_count


def find_gamma_epsilon(numbers: List[str]) -> Tuple[str, str]:
    ones_count = positions_count_ones(numbers)

    gamma = ""
    epsilon = ""

    for count1 in ones_count.values():
        count0 = len(numbers) - count1  # number of 0s in that position

        if count1 > count0:
            gamma += "1"
            epsilon += "0"
        elif count1 < count0:
            gamma += "0"
            epsilon += "1"

    return (gamma, epsilon)


def find_power_consumption(numbers: List[str]) -> int:
    gamma, epsilon = find_gamma_epsilon(numbers)
    return int(gamma, 2) * int(epsilon, 2)


find_power_consumption(input)  # answer part 1

# part 2
def position_count_ones(numbers: List[str], pos: int) -> int:
    """Go through all numbers and only count 1s if they appear in a specified position"""
    count = 0
    for number in numbers:
        count += number[pos] == "1"
    return count


def find_oxygen_generator_rating(numbers: List[str]) -> int:
    bit_size = len(numbers[0])
    ns = numbers.copy()

    for pos in range(bit_size):
        if len(ns) == 1:
            return int(ns[0], 2)

        count1 = position_count_ones(ns, pos)
        count0 = len(ns) - count1
        if count1 >= count0:
            # keep only numbers with 1's in their ith position if 1 is most common
            ns = [n for n in ns if n[pos] == "1"]
        else:
            ns = [n for n in ns if n[pos] == "0"]

    return int(ns[0], 2)  # for typing


def find_co2_scrubber_rating(numbers: List[str]) -> int:
    bit_size = len(numbers[0])
    ns = numbers.copy()

    for pos in range(bit_size):
        if len(ns) == 1:
            return int(ns[0], 2)

        count1 = position_count_ones(ns, pos)
        count0 = len(ns) - count1
        if count1 >= count0:
            # keep only numbers with 0's in their ith position if 1 is most common
            ns = [n for n in ns if n[pos] == "0"]
        else:
            ns = [n for n in ns if n[pos] == "1"]

    return int(ns[0], 2)  # for typing


def find_life_support_rating(numbers: List[str]) -> int:
    o = find_oxygen_generator_rating(numbers)
    co2 = find_co2_scrubber_rating(numbers)
    return o * co2


find_life_support_rating(input)  # answer part 2
