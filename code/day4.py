from __future__ import annotations
import re
from dataclasses import dataclass
from utils import read_input, dict_insert_add

lines = read_input(4)

test_lines = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]


@dataclass
class ScratchCard:
    id: int
    winners: list[int]
    haves: list[int]

    @classmethod
    def from_line(cls, line: str) -> ScratchCard:
        id_part, numbers_part = line.split(":")
        id = re.sub("^Card\\s+(\\d+)$", "\\1", id_part)
        winners_part, haves_part = numbers_part.split("|")

        winners = winners_part.strip().split(" ")
        haves = haves_part.strip().split(" ")

        return cls(
            id=int(id),
            winners=[int(n) for n in winners if n != ""],
            haves=[int(n) for n in haves if n != ""],
        )
    
    def get_winning_numbers(self) -> list[int]:
        return [n for n in self.haves if n in self.winners]
    
    def n_winning_numbers(self) -> int:
        return len(self.get_winning_numbers())
    
    def score(self) -> int:
        n = self.n_winning_numbers()

        if n == 0:
            return 0
        else:
            return 2 ** (n - 1)


sc = ScratchCard.from_line(test_lines[0])
assert sc.n_winning_numbers() == 4
assert sc.score() == 8

sc = ScratchCard.from_line(test_lines[1])
assert sc.n_winning_numbers() == 2
assert sc.score() == 2


def solve1(lines: list[str]) -> int:
    total = 0

    for line in lines:
        sc = ScratchCard.from_line(line)
        total += sc.score()

    return total

assert solve1(test_lines) == 13
print(solve1(lines))

def get_all_cards(lines: list[str]) -> list[ScratchCard]:
    return [ScratchCard.from_line(line) for line in lines]


def get_card_counts(cards: list[ScratchCard]) -> dict[int, int]:
    # start with 1 of every card
    card_counts = {card.id: 1 for card in cards}

    for card in cards:
        id = card.id
        n_winners = card.n_winning_numbers()

        card_count = card_counts[id]

        for _ in range(card_count):
            for i in range(n_winners):
                winning_id = id + i + 1
                # print(f"Card with {id} gives a copy of {winning_id}")
                card_counts[winning_id] += 1

    return card_counts

def solve2(lines: list[str]) -> int:
    cards = get_all_cards(lines)
    counts = get_card_counts(cards)
    return sum(counts.values())

assert solve2(test_lines) == 30
print(solve2(lines))
