from __future__ import annotations
from typing import Tuple, List, Optional
import numpy as np
import seaborn as sns
from matplotlib.axes import Axes

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

with open("day5-input.txt", "r") as f:
    input = [line.strip() for line in f.readlines()]

def axis_range(a: int, b: int) -> List[int]:
    if a == b:
        return [a]
    elif a < b:
        return list(range(a, b + 1, 1))
    else:
        return list(range(a, b - 1, -1))


def horizontal_points(x1: int, x2: int, y: int) -> List[Point]:
    xr = axis_range(x1, x2)
    return [(x, y) for x in xr]


def vertical_points(x: int, y1: int, y2: int) -> List[Point]:
    yr = axis_range(y1, y2)
    return [(x, y) for y in yr]


def diagonal_points(x1: int, y1: int, x2: int, y2: int) -> List[Point]:
    xr = axis_range(x1, x2)
    yr = axis_range(y1, y2)
    return [(x, y) for x, y in zip(xr, yr)]


def line_points(x1: int, y1: int, x2: int, y2: int, with_diagonals: bool = True) -> Optional[List[Point]]:
    if x1 == x2:
        return vertical_points(x1, y1, y2)
    elif y1 == y2:
        return horizontal_points(x1, x2, y1)
    else:
        if with_diagonals:
            return diagonal_points(x1, y1, x2, y2)
        else:
            return None


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

    def vent_line(self, with_diagonals: bool = True) -> Optional[List[Point]]:
        return line_points(self.x1, self.y1, self.x2, self.y2, with_diagonals)

    @classmethod
    def from_string(cls, string: str) -> Vent:
        p1, p2 = string.split(" -> ")
        x1, y1 = p1.split(",")
        x2, y2 = p2.split(",")
        return cls((int(x1), int(y1)), (int(x2), int(y2)))

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

        return (
            (min_x, min_y),
            (max_x, min_y),
            (min_x, max_y),
            (max_x, max_y),
        )

    def overlapping_matrix(self, with_diagonals: bool = True) -> np.matrix:
        nx = self.max_x() + 1
        ny = self.max_y() + 1

        rows = [[0 for _ in range(ny)] for _ in range(nx)]
        m = np.matrix(rows)

        for vent in self.vents:
            points = vent.vent_line(with_diagonals)

            # points returned can be None if with_diagonals is False
            if points is None:
                continue

            for point in points:
                m[point[0], point[1]] += 1

        return m

    def count_at_least_two_overlaps(self, with_diagonals: bool = True) -> int:
        m = self.overlapping_matrix(with_diagonals)
        return (m >= 2).sum()

    def plot(self, with_diagonals: bool = True, cbar: bool = False) -> Axes:
        m = self.overlapping_matrix(with_diagonals)
        ax = sns.heatmap(m, xticklabels=False, yticklabels=False, cbar=cbar)
        return ax

of = OceanFloor([Vent.from_string(string) for string in input])

# part 1
_ = of.plot(False)
of.count_at_least_two_overlaps(False) # answer part 1

# part 2
_ = of.plot(True)
of.count_at_least_two_overlaps(True) # answer part 2
