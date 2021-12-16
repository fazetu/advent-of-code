from typing import List
from Grid import Grid, Point

input = [
    "1163751742",
    "1381373672",
    "2136511328",
    "3694931569",
    "7463417111",
    "1319128137",
    "1359912421",
    "3125421639",
    "1293138521",
    "2311944581",
]

def which_mins(vals: List[int]) -> List[int]:
    return [i for i, val in enumerate(vals) if val == min(vals)]

class RiskLevel:
    def __init__(self, lines: List[str]):
        self.grid = Grid([[int(char) for char in line] for line in lines])
        self.position = (0, 0)
        self.path: List[Point] = []

    def find_next_possible_moves(self, position: Point, path: List[Point]) -> List[Point]:
        return [point for point in self.grid.adjacent_points(position, False) if point not in path]

    def find_next_best_moves(self, position: Point, path: List[Point]) -> List[Point]:
        nexts = self.find_next_possible_moves(position, path)
        best_risk = min([self.grid.get(point) for point in nexts])
        best_nexts = []
        for point in nexts:
            if self.grid.get(point) == best_risk:
                best_nexts.append(point)
        return best_nexts

    def find_next_best_move(self, position, path: List[Point]) -> Point:
        possible = self.find_next_best_moves(position, path)
        return possible[0]

    def move(self):
        self.path.append(self.position)
        self.position = self.find_next_best_move(self.position, self.path)

    def navigate_cave(self):
        r, c = self.grid.dim

        while self.position != (r - 1, c - 1):
            self.move()

    def total_risk(self) -> int:
        self.navigate_cave()
        risks = [self.grid.get(point) for point in self.path]
        return sum(risks)


rl = RiskLevel(input)

# part 1
rl.total_risk() # answer part 1
