from typing import Tuple, List
import warnings

input = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]

with open("day2-input.txt", "r") as f:
    input_ = f.readlines()

input = [line.strip() for line in input_]

# part 1
def parse_command(command: str) -> Tuple[str, int]:
    direction, distance = command.split(" ")
    return (direction, int(distance))

def run_commands1(input: List[str]) -> Tuple[int, int]:
    horizontal = 0
    depth = 0

    for command in input:
        direction, distance = parse_command(command)
        if direction == "forward":
            horizontal += distance
        elif direction == "down":
            depth += distance
        elif direction == "up":
            depth -= distance
        else:
            warnings.warn(f"Unknown direction {direction}")
    
    return (horizontal, depth)

h, d = run_commands1(input)
h * d # answer part 1

# part 2
def run_commands2(input: List[str]) -> Tuple[int, int]:
    horizontal = 0
    depth = 0
    aim = 0

    for command in input:
        direction, distance = parse_command(command)

        if direction == "forward":
            horizontal += distance
            depth += (aim * distance)
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance
        else:
            warnings.warn(f"Unknown direction {direction}")
    
    return (horizontal, depth)

h, d = run_commands2(input)
h * d # answer part 2
