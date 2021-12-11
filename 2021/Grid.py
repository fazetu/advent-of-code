from typing import List, Optional, Tuple

IntGrid = List[List[int]]
Point = Tuple[int, int]
OptionalPoint = Optional[Point]

class Grid:
    def __init__(self, grid: IntGrid):
        self.grid = grid

    @property
    def dim(self) -> Point:
        nr = len(self.grid)
        nc = len(self.grid[0])
        return (nr, nc)

    def check_valid_point(self, point: Point):
        nr, nc = self.dim
        mr = nr - 1 # max row number
        mc = nc - 1 # max column number
        r, c = point

        if (r < 0) or (r > mr):
            raise ValueError(f"point's row value, {r}, is invalid")

        if (c < 0) or (c > mc):
            raise ValueError(f"point's column value, {c}, is invalid")
    
    def try_return_point(self, point: Point) -> OptionalPoint:
        try:
            self.check_valid_point(point)
            return point
        except:
            return None

    def up(self, point: Point) -> OptionalPoint:
        r, c = point
        return self.try_return_point((r - 1, c))

    def down(self, point: Point) -> OptionalPoint:
        r, c = point
        return self.try_return_point((r + 1, c))

    def left(self, point: Point) -> OptionalPoint:
        r, c = point
        return self.try_return_point((r, c - 1))

    def right(self, point: Point) -> OptionalPoint:
        r, c = point
        return self.try_return_point((r, c + 1))

    def upleft(self, point: Point) -> OptionalPoint:
        r, c = point
        return self.try_return_point((r - 1, c - 1))

    def upright(self, point: Point) -> OptionalPoint:
        r, c = point
        return self.try_return_point((r - 1, c + 1))

    def downleft(self, point: Point) -> OptionalPoint:
        r, c = point
        return self.try_return_point((r + 1, c - 1))

    def downright(self, point: Point) -> OptionalPoint:
        r, c = point
        return self.try_return_point((r + 1, c + 1))

    def adjacent_points(self, point: Point, with_diagonals: bool = True) -> List[Point]:
        up = self.up(point)
        down = self.down(point)
        left = self.left(point)
        right = self.right(point)

        res = []
        if up is not None:
            res.append(up)
        if down is not None:
            res.append(down)
        if left is not None:
            res.append(left)
        if right is not None:
            res.append(right)

        if not with_diagonals:
            return res
        
        ul = self.upleft(point)
        ur = self.upright(point)
        dl = self.downleft(point)
        dr = self.downright(point)

        if ul is not None:
            res.append(ul)
        if ur is not None:
            res.append(ur)
        if dl is not None:
            res.append(dl)
        if dr is not None:
            res.append(dr)

        return res

    def get(self, point: Point) -> int:
        r, c = point
        return self.grid[r][c]

    def set(self, point: Point, value: int) -> int:
        r, c = point
        self.grid[r][c] = value
