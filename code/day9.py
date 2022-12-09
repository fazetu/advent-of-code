from utils import read_input

# input = [
#     "R 4",
#     "U 4",
#     "L 3",
#     "D 1",
#     "R 4",
#     "D 1",
#     "L 5",
#     "R 2",
# ]

input = read_input(9)

Point = tuple[int, int]


def which_min(vals: list[float]) -> int:
    inds = [i for i, val in enumerate(vals) if val == min(vals)]
    return inds[0]


def get_direction_length(line: str) -> tuple[str, int]:
    d, l = line.split(" ")
    return (d, int(l))


def distance(x: Point, y: Point) -> float:
    x1, y1 = x
    x2, y2 = y
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1 / 2)


def move(x: Point, direction: str) -> Point:
    xx, xy = x

    match direction:
        case "R":
            return (xx + 1, xy)
        case "L":
            return (xx - 1, xy)
        case "U":
            return (xx, xy + 1)
        case "D":
            return (xx, xy - 1)

    raise ValueError(f"Invalid direction: {direction}")


def move_tail(H: Point, T: Point) -> Point:
    d = distance(H, T)

    if d <= 1.0:
        # T doesn't need to move
        return T
    elif d <= (2 ** (1 / 2)):
        # T doesn't need to move if we are 1 diagonal space away
        return T
    elif d <= 2.0:
        # not a diagonal move
        Hx, Hy = H
        Tx, Ty = T
        Tx_new = int((Hx + Tx) / 2)
        Ty_new = int((Hy + Ty) / 2)
        return (Tx_new, Ty_new)
    else:
        # diagonal move
        # try all diagonals and pick the closest option
        Tx, Ty = T

        d1 = ((Tx - 1), (Ty - 1))
        d2 = ((Tx - 1), (Ty + 1))
        d3 = ((Tx + 1), (Ty - 1))
        d4 = ((Tx + 1), (Ty + 1))
        diags = [d1, d2, d3, d4]

        distances = [distance(H, diag) for diag in diags]
        return diags[which_min(distances)]


assert distance((0, 0), (0, 0)) == 0
assert distance((0, 0), (1, 0)) == 1
assert move_tail((0, 0), (0, 0)) == (0, 0)
assert move_tail((1, 0), (0, 0)) == (0, 0)
assert move_tail((2, 0), (0, 0)) == (1, 0)
assert move_tail((3, 0), (1, 0)) == (2, 0)
assert move_tail((4, 0), (2, 0)) == (3, 0)
assert move_tail((4, 1), (3, 0)) == (3, 0)
assert move_tail((4, 2), (3, 0)) == (4, 1)
assert move_tail((4, 3), (4, 1)) == (4, 2)


START: Point = (0, 0)

# part 1
def show1(H: Point, T: Point):
    print(f"Head: {H} | Tail: {T}")


T_VISITS1: set[Point] = set((START,))
H: Point = START
T: Point = START
VERBOSE1 = False

if VERBOSE1:
    show1(H, T)

for line in input:
    d, l = get_direction_length(line)

    for _ in range(l):
        H = move(H, d)
        T = move_tail(H, T)
        T_VISITS1.add(T)

        if VERBOSE1:
            show1(H, T)

# answer 1
print(len(T_VISITS1))

# part 2
# input = [
#     "R 5",
#     "U 8",
#     "L 8",
#     "D 3",
#     "R 17",
#     "D 10",
#     "L 25",
#     "U 20",
# ]


def show2(knots: dict[int, Point]):
    print(" | ".join([f"Knot{k}: {v}" for k, v in knots.items()]))


T_VISITS2: set[Point] = set((START,))
KNOTS: dict[int, Point] = {i: START for i in range(10)}
VERBOSE2 = False

if VERBOSE2:
    print("Start state")
    show2(KNOTS)

for line in input:
    d, l = get_direction_length(line)

    for _ in range(l):
        # just the head moves
        H = KNOTS[0]  # current head
        H = move(H, d)  # head moves
        KNOTS[0] = H  # update the head in the list of knots

        # then make all the other knots follow the one in front of them
        for i in range(0, len(KNOTS) - 1):
            H = KNOTS[i]
            T = KNOTS[i + 1]
            T = move_tail(H, T)
            KNOTS[i + 1] = T

        # last knot is the tail
        T_VISITS2.add(KNOTS[len(KNOTS) - 1])

        if VERBOSE2:
            show2(KNOTS)

# answer 2
print(len(T_VISITS2))
