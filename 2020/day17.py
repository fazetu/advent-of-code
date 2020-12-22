input = [".#.", "..#", "###"]
grid = [[1 if char == "#" else 0 for char in line] for line in input]

class Layer:
    def __init__(self, grid):
        self.grid = grid

    def expand(self):
        # expand grid out by 1 in all directions
        grid = self.grid
        new_grid = [[0] + row + [0] for row in self.grid]
        r = [0] * len(new_grid[0])
        self.grid = [r] + new_grid + [r]
        

l1 = Layer(grid=grid)
l1.grid
l1.expand()
l1.grid
