from __future__ import annotations
import re
from dataclasses import dataclass
from utils import read_input

input = [
    "Monkey 0:",
    "  Starting items: 79, 98",
    "  Operation: new = old * 19",
    "  Test: divisible by 23",
    "    If true: throw to monkey 2",
    "    If false: throw to monkey 3",
    "",
    "Monkey 1:",
    "  Starting items: 54, 65, 75, 74",
    "  Operation: new = old + 6",
    "  Test: divisible by 19",
    "    If true: throw to monkey 2",
    "    If false: throw to monkey 0",
    "",
    "Monkey 2:",
    "  Starting items: 79, 60, 97",
    "  Operation: new = old * old",
    "  Test: divisible by 13",
    "    If true: throw to monkey 1",
    "    If false: throw to monkey 3",
    "",
    "Monkey 3:",
    "  Starting items: 74",
    "  Operation: new = old + 3",
    "  Test: divisible by 17",
    "    If true: throw to monkey 0",
    "    If false: throw to monkey 1",
]

# input = read_input(11)

@dataclass
class Monkey:
    i: int
    starting_items: list[int]
    operation: str
    test: str
    true_throw_to: str
    false_throw_to: str

    @classmethod
    def from_chunk(cls, lines: list[str]) -> Monkey:
        i = int(re.findall("\\d+", lines[0])[0])
        starting_items = int(re.findall("\\d+", lines[1])[0])
        re.match("Operation: ", lines[2])

        return cls()

Monkey.from_chunk(input[:6])