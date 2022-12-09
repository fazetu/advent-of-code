import numpy as np
from utils import read_input

# input = [
#     "30373",
#     "25512",
#     "65332",
#     "33549",
#     "35390",
# ]

input = read_input(8)


def make_matrix(lines: list[str]) -> np.ndarray:
    return np.array([[int(val) for val in line] for line in lines])


def lrud(
    m: np.ndarray, r: int, c: int
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    left = m[r, :][:c]
    right = m[r, :][(c + 1) :]
    up = m[:, c][:r]
    down = m[:, c][(r + 1) :]
    return (left, right, up, down)


def is_visible(m: np.ndarray, r: int, c: int) -> bool:
    h = m[r, c]
    left, right, up, down = lrud(m, r, c)

    if len(left) == 0 or all(left < h):
        return True

    if len(right) == 0 or all(right < h):
        return True

    if len(up) == 0 or all(up < h):
        return True

    if len(down) == 0 or all(down < h):
        return True

    return False


def is_visible_matrix(m: np.ndarray) -> np.ndarray:
    arr = []
    nr = len(m[0])
    nc = len(m)

    for r in range(nr):
        row = []

        for c in range(nc):
            row.append(is_visible(m, r, c))

        arr.append(row)

    return np.array(arr)


def direction_scenic_score(x: np.ndarray, h: int) -> int:
    score = 0

    for val in x:
        if val >= h:
            score += 1
            return score
        else:
            score += 1

    return score


def scenic_score(m: np.ndarray, r: int, c: int) -> int:
    h = m[r, c]
    left, right, up, down = lrud(m, r, c)

    return (
        direction_scenic_score(left[::-1], h)
        * direction_scenic_score(right, h)
        * direction_scenic_score(up[::-1], h)
        * direction_scenic_score(down, h)
    )


def scenic_score_matrix(m: np.ndarray) -> np.ndarray:
    arr = []
    nr = len(m[0])
    nc = len(m)

    for r in range(nr):
        row = []

        for c in range(nc):
            row.append(scenic_score(m, r, c))

        arr.append(row)

    return np.array(arr)


m = make_matrix(input)

# part 1
vis_m = is_visible_matrix(m)

# answer 1
print(vis_m.sum())

# part 2
sce_m = scenic_score_matrix(m)
print(sce_m.max())
