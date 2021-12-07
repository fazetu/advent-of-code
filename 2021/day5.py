from __future__ import annotations
from typing import Tuple, List
import numpy as np

Point = Tuple[int, int]

input = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]


def horizontal_points(x1: int, x2: int, y: int) -> List[Point]:
    if x1 == x2:
        return [(x1, y)]
    elif x1 < x2:
        xr = list(range(x1, x2 + 1, 1))
    else:
        xr = list(range(x1, x2 - 1, -1))

    return [(x, y) for x in xr]


def vertical_points(x: int, y1: int, y2: int) -> List[Point]:
    if y1 == y2:
        return [(x, y1)]
    elif y1 < y2:
        yr = list(range(y1, y2 + 1))
    else:
        yr = list(range(y1, y2 - 1, -1))

    return [(x, y) for y in yr]


def diagonal_points(x1: int, y1: int, x2: int, y2: int) -> List[Point]:
    pass


def line_points(x1: int, y1: int, x2: int, y2: int) -> List[Point]:
    if x1 == x2:
        return vertical_points(x1, y1, y2)
    elif y1 == y2:
        return horizontal_points(x1, x2, y1)
    else:
        return diagonal_points(x1, x2, y1, y2)


class Vent:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    @property
    def x1(self) -> int:
        return self.p1[0]

    @property
    def y1(self) -> int:
        return self.p1[1]

    @property
    def x2(self) -> int:
        return self.p2[0]

    @property
    def y2(self) -> int:
        return self.p2[1]

    def vent_line(self) -> List[Point]:
        return line_points(self.x1, self.y1, self.x2, self.y2)

    @classmethod
    def from_string(cls, string: str) -> Vent:
        p1, p2 = string.split(" -> ")
        p1 = [int(val) for val in p1.split(",")]
        p2 = [int(val) for val in p2.split(",")]
        return cls(p1, p2)

    def max_x(self) -> int:
        return max(self.x1, self.x2)

    def min_x(self) -> int:
        return min(self.x1, self.x2)

    def max_y(self) -> int:
        return max(self.y1, self.y2)

    def min_y(self) -> int:
        return min(self.y1, self.y2)


class OceanFloor:
    def __init__(self, vents: List[Vent]):
        self.vents = vents

    def max_x(self) -> int:
        return max([vent.max_x() for vent in self.vents])

    def min_x(self) -> int:
        return min([vent.min_x() for vent in self.vents])

    def max_y(self) -> int:
        return max([vent.max_y() for vent in self.vents])

    def min_y(self) -> int:
        return min([vent.min_y() for vent in self.vents])

    def boundaries(self) -> Tuple[Point, Point, Point, Point]:
        max_x = self.max_x()
        min_x = self.min_x()
        max_y = self.max_y()
        min_y = self.min_y()

        return [
            (min_x, min_y),
            (max_x, min_y),
            (min_x, max_y),
            (max_x, max_y),
        ]

    def overlapping_matrix(self) -> np.matrix:
        nx = self.max_x() + 1
        ny = self.max_y() + 1

        np.matrix()
        np.m
        pass


of = OceanFloor([Vent.from_string(string) for string in input])
of.boundaries()
