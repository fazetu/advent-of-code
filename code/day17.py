import numpy as np

input = [".#.", "..#", "###"]
grid = [[1 if char == "#" else 0 for char in line] for line in input]
grid = np.array(grid)

class Layer:
    def __init__(self, grid):
        self.grid = grid

    def expand(self):
        # expand grid out by 1 in all directions
        new_grid = np.zeros(shape=(self.grid.shape[0] + 2, self.grid.shape[1] + 2))
        for i, row in enumerate(grid):
            grid[i] = np.concatenate((np.array([0]), row, np.array([0])))
        
        

l1 = Layer(grid=grid)
l1.grid
l1.expand()
l1.grid


