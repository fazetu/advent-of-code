from functools import reduce
from typing import List, Optional, Tuple
from matplotlib.axes import Axes
import seaborn as sns
Grid = List[List[int]]
Point = Tuple[int, int]

input = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678",
]

with open("day9-input.txt", "r") as f:
    input = [line.strip() for line in f.readlines()]

def coord_up_value(grid: Grid, r: int, c: int) -> Optional[int]:
    up_r = r - 1

    if 0 <= up_r <= (len(grid) - 1):
        return grid[up_r][c]
    else:
        return None

def coord_down_value(grid: Grid, r: int, c: int) -> Optional[int]:
    down_r = r + 1

    if 0 <= down_r <= (len(grid) - 1):
        return grid[down_r][c]
    else:
        return None

def coord_left_value(grid: Grid, r: int, c: int) -> Optional[int]:
    left_c = c - 1

    if 0 <= left_c <= (len(grid[0]) - 1):
        return grid[r][left_c]
    else:
        return None

def coord_right_value(grid: Grid, r: int, c: int) -> Optional[int]:
    right_c = c + 1

    if 0 <= right_c <= (len(grid[0]) - 1):
        return grid[r][right_c]
    else:
        return None

def coord_adjacent_values(grid: List[List[int]], r: int, c: int) -> List[int]:
    adj = []

    up = coord_up_value(grid, r, c)
    down = coord_down_value(grid, r, c)
    left = coord_left_value(grid, r, c)
    right = coord_right_value(grid, r, c)
    
    if up is not None:
        adj.append(up)

    if down is not None:
        adj.append(down)

    if left is not None:
        adj.append(left)

    if right is not None:
        adj.append(right)

    return adj


class Heightmap:
    def __init__(self, heights: List[str]):
        grid: List[List[int]] = [
            [int(line[i : (i + 1)]) for i in range(len(line))] for line in heights
        ]
        self.grid = grid

    def plot(self, cbar: bool = False) -> Axes:
        ax = sns.heatmap(self.grid, xticklabels=False, yticklabels=False, cbar=cbar)
        return ax

    @property
    def dim(self) -> Point:
        return len(self.grid), len(self.grid[0])

    def check_coords(self, r: int, c: int):
        nr, nc = self.dim
        mr = nr - 1  # max row index value is 1 less than the number of rows
        mc = nc - 1  # max column index value is 1 less than the number of columns

        if (r < 0) or (r > mr) or (c < 0) or (c > mc):
            raise ValueError(f"Coordinates are invalid. r: {r} c: {c}")

    def coord_adjacent_values(self, r: int, c: int) -> List[int]:
        self.check_coords(r, c)
        return coord_adjacent_values(self.grid, r, c)

    def coord_is_low_point(self, r: int, c: int) -> bool:
        self.check_coords(r, c)
        adj = self.coord_adjacent_values(r, c)
        val = self.grid[r][c]
        return all([val < v for v in adj])

    def find_all_low_point_coords(self) -> List[Point]:
        nr, nc = self.dim
        low_points = []

        for r in range(nr):
            for c in range(nc):
                if self.coord_is_low_point(r, c):
                    low_points.append((r, c))

        return low_points

    def find_low_point_risk_levels(self) -> List[int]:
        low_points = self.find_all_low_point_coords()
        risk_levels = []

        for r, c in low_points:
            val = self.grid[r][c]
            risk_levels.append(val + 1)

        return risk_levels

    def find_answer_part1(self) -> int:
        return sum(self.find_low_point_risk_levels())

    def extend_basin_from_low_point(self, low_point: Point, basin_points: List[Point] = []) -> List[Point]:
        basin_points.append(low_point)
        r, c = low_point
        up = coord_up_value(self.grid, r, c)
        down = coord_down_value(self.grid, r, c)
        left = coord_left_value(self.grid, r, c)
        right = coord_right_value(self.grid, r, c)

        if up is not None and up != 9:
            pt = (r - 1, c)
            if pt not in basin_points:
                self.extend_basin_from_low_point(pt, basin_points)

        if down is not None and down != 9:
            pt = (r + 1, c)
            if pt not in basin_points:
                self.extend_basin_from_low_point(pt, basin_points)

        if left is not None and left != 9:
            pt = (r, c - 1)
            if pt not in basin_points:
                self.extend_basin_from_low_point(pt, basin_points)

        if right is not None and right != 9:
            pt = (r, c + 1)
            if pt not in basin_points:
                self.extend_basin_from_low_point(pt, basin_points)

        return basin_points

    def find_basins(self) -> List[List[Point]]:
        low_points = self.find_all_low_point_coords()
        basins = []

        for low_point in low_points:
            basins.append(self.extend_basin_from_low_point(low_point, []))

        return basins

    def find_answer_part2(self) -> int:
        basins = self.find_basins()
        sizes = [len(basin) for basin in basins]
        top3 = sorted(sizes, reverse=True)[:3]
        return reduce(lambda x, y: x * y, top3)

hm = Heightmap(input)
_ = hm.plot()

# part 1
hm.find_answer_part1()  # answer part 1

# part 2
hm.find_answer_part2() # answer part 2
