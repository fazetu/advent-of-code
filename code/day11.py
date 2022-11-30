from typing import List
from Grid import Grid, Point

input = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526",
]

input = [
    "8548335644",
    "6576521782",
    "1223677762",
    "1284713113",
    "6125654778",
    "6435726842",
    "5664175556",
    "1445736556",
    "2248473568",
    "6451473526",
]


class Octopuses:
    def __init__(self, energy_levels: List[str]):
        energy_grid = []

        for line in energy_levels:
            energy_grid.append([int(char) for char in line])

        self.grid = Grid(energy_grid)

    def increase_point(self, point: Point):
        val = self.grid.get(point)
        self.grid.set(point, val + 1)

    def increase_grid(self):
        nr, nc = self.grid.dim
        for r in range(nr):
            for c in range(nc):
                self.increase_point((r, c))

    def flash_points(self) -> List[Point]:
        nr, nc = self.grid.dim

        res = []
        for r in range(nr):
            for c in range(nc):
                pt = (r, c)
                val = self.grid.get(pt)
                if val > 9:
                    res.append(pt)

        return res

    def step(self) -> List[Point]:
        flashed = []
        self.increase_grid()
        flashers = self.flash_points()

        while len(flashers) > 0:
            for flasher in flashers:
                flashed.append(flasher)
                self.grid.set(flasher, 0)  # reset flashers
                adjacent_points = self.grid.adjacent_points(flasher, True)
                for adjacent_point in adjacent_points:
                    if adjacent_point not in flashed:
                        self.increase_point(adjacent_point)

            flashers = self.flash_points()

        return flashed

    def steps(self, n: int):
        for _ in range(n):
            _ = self.step()

    def count_flashes(self, n: int) -> int:
        count = 0

        for _ in range(n):
            flashed = self.step()
            count += len(flashed)

        return count

    def all_zero(self) -> bool:
        nr, nc = self.grid.dim

        for r in range(nr):
            for c in range(nc):
                val = self.grid.get((r, c))
                if val != 0:
                    return False
            
        return True

    def first_all_flash(self) -> int:
        i = 0
        all_flashed = False
        while not all_flashed:
            self.step()
            i += 1
            all_flashed = self.all_zero()

        return i


# part 1
octs = Octopuses(input)
octs.count_flashes(100) # answer part 1

# part 2
octs = Octopuses(input)
octs.first_all_flash() # answer part 2
