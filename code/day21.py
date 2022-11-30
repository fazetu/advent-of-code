from typing import Optional
from abc import ABC, abstractclassmethod
import numpy as np

def move(position: int, by: int) -> int:
    new_pos = (position + by) % 10
    if new_pos == 0:
        return 10
    else:
        return new_pos

class Die(ABC):
    @abstractclassmethod
    def roll(self) -> int:
        raise NotImplementedError("Must implement")


class D6(Die):
    def __init__(self, n_sides: int = 6):
        super().__init__()
        self.n_sides = n_sides
        self.options = list(range(1, n_sides + 1))

    def roll(self) -> int:
        r = np.random.choice(self.options, size=1, replace=True)
        return r[0]


class DeterministicDie(Die):
    def __init__(self, n_sides: int = 100):
        super().__init__()
        self.next_roll = 1
        self.n_sides = n_sides

    def roll(self) -> int:
        res = self.next_roll

        if res == self.n_sides:
            self.next_roll = 1
        else:
            self.next_roll += 1

        return res

class DiracDie(Die):
    def __init__(self):
        super().__init__()

class DiracDiceGame:
    def __init__(self, start1: int, start2: int, die: Die):
        self.player1 = start1
        self.player2 = start2
        self.player1_score = 0
        self.player2_score = 0
        self.die = die

    def move_player1(self, n_rolls: int):
        rolls = [self.die.roll() for _ in range(n_rolls)]
        by = sum(rolls)
        self.player1 = move(self.player1, by)
        self.player1_score += self.player1

    def move_player2(self, n_rolls: int):
        rolls = [self.die.roll() for _ in range(n_rolls)]
        by = sum(rolls)
        self.player2 = move(self.player2, by)
        self.player2_score += self.player2

    def play(self, winning_score: int) -> int:
        n_rolls = 0
        while True:
            self.move_player1(3)
            n_rolls += 3

            if self.player1_score >= winning_score:
                break

            self.move_player2(3)
            n_rolls += 3

            if self.player2_score >= winning_score:
                break

        return n_rolls

# part 1
d = DeterministicDie(100)
game = DiracDiceGame(4, 2, d)
n_rolls = game.play(1000)
game.player2_score * n_rolls # answer part 1

# part 2
d = DiracDie()
game = DiracDiceGame(4, 2, d)
n_rolls = game.play(21)
game.player2_score * n_rolls # answer part 2
