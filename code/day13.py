from typing import List, Tuple
import copy
from Grid import IntGrid

small_input = [
    "6,10",
    "0,14",
    "9,10",
    "0,3",
    "10,4",
    "4,11",
    "6,0",
    "6,12",
    "4,1",
    "0,13",
    "10,12",
    "3,4",
    "3,0",
    "8,4",
    "1,10",
    "2,14",
    "8,10",
    "9,0",
    "",
    "fold along y=7",
    "fold along x=5",
]

with open("day13-input.txt", "r") as f:
    input = [line.strip() for line in f.readlines()]


def parse_input(input: List[str]) -> Tuple[List[str], List[str]]:
    brk = [i for i, line in enumerate(input) if line == ""][0]
    points = input[:brk]
    folds = input[(brk + 1) :]
    return (points, folds)


def make_grid(points: List[str]) -> IntGrid:
    int_points = [
        (int(x), int(y)) for x, y in [point.split(",") for point in points]
    ]
    mc = max([x for x, _ in int_points]) + 1
    mr = max([y for _, y in int_points]) + 1
    grid = [[0 for _ in range(mc)] for _ in range(mr)]
    for point in int_points:
        x, y = point
        grid[y][x] = 1
    return grid


def or_grids(grid1: IntGrid, grid2: IntGrid) -> IntGrid:
    res = []

    for row1, row2 in zip(grid1, grid2):
        r = []
        for v1, v2 in zip(row1, row2):
            if v1 == 1 or v2 == 1:
                r.append(1)
            else:
                r.append(0)
        res.append(r)

    return res


def extend_above(grid: IntGrid, by: int) -> IntGrid:
    g = copy.deepcopy(grid)
    c = len(grid[0])
    for _ in range(by):
        row = [0 for _ in range(c)]
        g.insert(0, row)
    return g


def extend_right(grid: IntGrid, by: int) -> IntGrid:
    g = copy.deepcopy(grid)
    for row in g:
        for _ in range(by):
            row.append(0)
    return g


def make_horizontal_fold(grid: IntGrid, hline: int) -> IntGrid:
    top = grid[:hline]
    bottom = grid[(hline + 1) :]
    bottom_flipped = list(reversed(bottom))

    size_top = len(top)
    size_bottom = len(bottom_flipped)

    if size_top != size_bottom:
        if size_top > size_bottom:
            # there are more rows in top than bottom
            need_n = size_top - size_bottom
            # add 0 rows to the top of bottom_flipped
            bottom_flipped = extend_above(bottom_flipped, need_n)
        else:
            # there are less rows in top than bottom
            need_n = size_bottom - size_top
            # add 0 rows to the top of top
            top = extend_above(top, need_n)

    return or_grids(top, bottom_flipped)


def make_vertical_fold(grid: IntGrid, vline: int) -> IntGrid:
    left = [row[:vline] for row in grid]
    right = [row[(vline + 1) :] for row in grid]
    left_flipped = [list(reversed(row)) for row in left]

    size_left = len(left_flipped[0])
    size_right = len(right[0])

    if size_left != size_right:
        if size_left > size_right:
            need_n = size_left - size_right
            right = extend_right(right, need_n)
        else:
            need_n = size_right - size_left
            left_flipped = extend_right(left_flipped, need_n)

    return or_grids(left_flipped, right)


def apply_folds(init_grid: IntGrid, folds: List[str]) -> IntGrid:
    grid = copy.deepcopy(init_grid)

    for fold in folds:
        direction, line = fold.replace("fold along ", "").split("=")

        if direction == "x":
            grid = make_vertical_fold(grid, vline=int(line))
        elif direction == "y":
            grid = make_horizontal_fold(grid, hline=int(line))

    return grid


def count_dots(grid: IntGrid) -> int:
    return sum([val for row in grid for val in row])


#input = small_input

points, folds = parse_input(input)
init_grid = make_grid(points)

# part 1
grid = apply_folds(init_grid, [folds[0]])
count_dots(grid)  # answer part 1

# part 2
grid = apply_folds(init_grid, folds)

import seaborn as sns
sns.heatmap([list(reversed(row)) for row in grid], xticklabels=False, yticklabels=False, cbar=False)
