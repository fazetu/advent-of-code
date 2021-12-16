from typing import List, Optional
import numpy as np
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

    def find_next_random_move(self, position: Point, path: List[Point]) -> Optional[Point]:
        pos = self.find_next_possible_moves(position, path)

        if len(pos) == 0:
            return None

        risks = [self.grid.get(point) for point in pos]

        if len(risks) == 1:
            probs = [1.0]
        else:
            total_risk = sum(risks)
            reverse_risks = [total_risk - risk for risk in risks]
            # pick point based on risk
            # higher risk means we should stay away from that point
            probs = [risk / sum(reverse_risks) for risk in reverse_risks]

        i = np.random.choice(np.arange(len(pos)), size=1, p=probs)
        j = i[0]
        return pos[j]

    def find_random_path(self) -> Optional[List[Point]]:
        path = []
        start = (0, 0)
        r, c = self.grid.dim
        end = (r - 1, c - 1)

        position = start
        path.append(position)

        while position != end:
            n = self.find_next_random_move(position, path)
            if n is None:
                return None
            path.append(n)
            position = n

        return path

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

    def calculate_total_risk(self, path: List[Point]) -> int:
        risks = [self.grid.get(point) for point in path]
        return sum(risks)

    def total_risk(self) -> int:
        self.navigate_cave()
        risks = [self.grid.get(point) for point in self.path]
        return sum(risks)

runs = []
rl = RiskLevel(input)

for _ in range(100000):
    rand_path = rl.find_random_path()

    if rand_path is not None:
        risk = rl.calculate_total_risk(rand_path)
    else:
        risk = None

    runs.append({"path": rand_path, "risk": risk})

min([run["risk"] for run in runs if run["risk"] is not None])
