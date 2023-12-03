from __future__ import annotations

import re
from dataclasses import dataclass

from utils import read_input

lines = read_input(2)


test_lines = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]


def get_game_id(line: str) -> int:
    return int(re.sub("Game (\\d+): .*", "\\1", line))


def get_possible_game_ids(
    lines: list[str], max_reds: int, max_greens: int, max_blues: int
) -> list[int]:
    all_games = []
    impossible_games = []

    for line in lines:
        id = get_game_id(line)
        all_games.append(id)

        reds = map(int, re.findall("(\\d+) red", line))

        if any([red > max_reds for red in reds]):
            impossible_games.append(id)
            continue

        greens = map(int, re.findall("(\\d+) green", line))

        if any([green > max_greens for green in greens]):
            impossible_games.append(id)
            continue

        blues = map(int, re.findall("(\\d+) blue", line))

        if any([blue > max_blues for blue in blues]):
            impossible_games.append(id)
            continue

    possible_games = [id for id in all_games if id not in impossible_games]
    return possible_games


def solve1(lines: list[str]) -> int:
    possible_game_ids = get_possible_game_ids(lines, 12, 13, 14)
    return sum(possible_game_ids)


assert solve1(test_lines) == 8

print(solve1(lines))


def get_power_of_game(line: str) -> int:
    needed_reds = max(map(int, re.findall("(\\d+) red", line)))
    needed_greens = max(map(int, re.findall("(\\d+) green", line)))
    needed_blues = max(map(int, re.findall("(\\d+) blue", line)))

    return needed_reds * needed_greens * needed_blues

assert get_power_of_game(test_lines[0]) == 48
assert get_power_of_game(test_lines[1]) == 12

def solve2(lines: list[str]) -> int:
    powers = [get_power_of_game(line) for line in lines]
    return sum(powers)

assert solve2(test_lines) == 2286

print(solve2(lines))
