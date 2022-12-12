from utils import _read_input, read_input, dict_insert_add

input = [
    "noop",
    "addx 3",
    "addx -5",
]
# input = _read_input("../input/day10-small.txt")
# input = read_input(10)

def build_cycle_ops(lines: list[str]) -> dict[int, int]:
    ops: dict[int, int] = {}

    for cycle_i, command in enumerate(lines):
        if command == "noop":
            dict_insert_add(ops, cycle_i, 0)
        elif command.startswith("addx"):
            _, amt = command.split(" ")
            dict_insert_add(ops, cycle_i, 0)
            dict_insert_add(ops, cycle_i + 1, int(amt))

    return ops


def apply_cycle_ops(cycle_ops: dict[int, int], register: int) -> list[tuple[int, int]]:
    r = register
    res = []

    for i in sorted(cycle_ops.keys()):
        amt = cycle_ops[i]
        res.append((r, r + amt))
        r += amt

    return res

ops = build_cycle_ops(input)
evolution = apply_cycle_ops(ops, 1)

for i, (start, end) in enumerate(evolution):
    print(f"Cycle {i + 1}: Start = {start}, End = {end}")
