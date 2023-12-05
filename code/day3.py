from dataclasses import dataclass

import numpy as np
from utils import read_input

lines = read_input(3)

test_lines = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]

digits = [*"1234567890"]


# use this so typing doesn't complain
def shape(x: np.ndarray) -> tuple[int, int]:
    row, col = x.shape
    return (row, col)


def lines_to_grid(lines: list[str]) -> np.ndarray:
    grid = np.array([[*line] for line in lines])
    return grid


@dataclass
class Symbol:
    value: str
    row: int
    col: int


@dataclass
class PartNumber:
    value: int
    row: int  # row of the part number
    cols: list[
        int
    ]  # columns the part number spans e.g. [0, 1, 2, 3] if it spans those 4 cols


def get_adjacent_coordinates(
    grid_shape: tuple[int, int], point: tuple[int, int]
) -> list[tuple[int, int]]:
    row, col = point
    up_a_row = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1)]
    current_row = [(row, col - 1), (row, col + 1)]
    down_a_row = [(row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
    possible_coordinates = up_a_row + current_row + down_a_row

    valid_coordinates = []
    grid_row, grid_col = grid_shape

    for r, c in possible_coordinates:
        # can't go negative row/col and can't go beyond the grid
        if 0 <= r < grid_row and 0 <= c < grid_col:
            valid_coordinates.append((r, c))

    return valid_coordinates


def get_possible_part_numbers_from_row(
    row: np.ndarray, row_number: int
) -> list[PartNumber]:
    n = len(row)
    res = []

    run = ""
    cols = []
    for i, val in enumerate(row):
        if val in digits:
            run += val
            cols.append(i)

            # special case where the current position is a digit, but we are done with the row
            if i == (n - 1) and len(run) > 0:
                res.append(PartNumber(int(run), row_number, cols))
        elif len(run) > 0:
            # the current value is not a digit - the run is done
            res.append(PartNumber(int(run), row_number, cols))

            # reset
            run = ""
            cols = []

    return res


assert len(get_possible_part_numbers_from_row(np.array([*"123*123"]), 0)) == 2
assert len(get_possible_part_numbers_from_row(np.array([*"123*123.1"]), 0)) == 3


def possible_part_number_is_a_part_number(
    possible_part_number: PartNumber,
    symbols: list[Symbol],
    grid_shape: tuple[int, int],
) -> bool:
    row = possible_part_number.row
    cols = possible_part_number.cols

    for col in cols:
        point = (row, col)
        adj = get_adjacent_coordinates(grid_shape, point)

        for adj_point in adj:
            for symbol in symbols:
                if adj_point == (symbol.row, symbol.col):
                    return True

    return False


def make_part_numbers_and_symbols(
    grid: np.ndarray,
) -> tuple[list[PartNumber], list[Symbol]]:
    nrows, ncols = grid.shape

    part_numbers = []
    symbols = []

    for ri in range(nrows):
        # get all the part numbers in this row
        part_numbers += get_possible_part_numbers_from_row(grid[ri], ri)

        for ci in range(ncols):
            val = grid[ri, ci]

            if val not in digits + ["."]:
                symbols.append(Symbol(val, ri, ci))

    return (part_numbers, symbols)


def solve1(lines: list[str]) -> int:
    grid = lines_to_grid(lines)
    part_numbers, symbols = make_part_numbers_and_symbols(grid)
    valid_part_numbers = [
        p
        for p in part_numbers
        if possible_part_number_is_a_part_number(p, symbols, shape(grid))
    ]
    return sum([p.value for p in valid_part_numbers])


# get_valid_part_numbers(lines_to_grid(test_lines))
# get_valid_part_numbers(lines_to_grid(lines))

assert solve1(test_lines) == 4361
print(solve1(lines))


def symbol_is_adjacent_to_part_number(
    symbol: Symbol, part_number: PartNumber, grid_shape: tuple[int, int]
) -> bool:
    point = (symbol.row, symbol.col)
    adj_points = get_adjacent_coordinates(grid_shape, point)

    for adj_point in adj_points:
        for col in part_number.cols:
            if adj_point == (part_number.row, col):
                return True

    return False


def symbol_gear_ratio(
    symbol: Symbol, part_numbers: list[PartNumber], grid_shape: tuple[int, int]
) -> int:
    if symbol.value != "*":
        return 0

    adjacent_part_numbers = [
        p
        for p in part_numbers
        if symbol_is_adjacent_to_part_number(symbol, p, grid_shape)
    ]

    if len(adjacent_part_numbers) == 2:
        a, b = adjacent_part_numbers
        return a.value * b.value
    else:
        return 0


def solve2(lines: list[str]) -> int:
    grid = lines_to_grid(lines)
    part_numbers, symbols = make_part_numbers_and_symbols(grid)
    gear_ratios = [
        symbol_gear_ratio(symbol, part_numbers, shape(grid)) for symbol in symbols
    ]
    return sum(gear_ratios)


assert solve2(test_lines) == 467835
print(solve2(lines))
