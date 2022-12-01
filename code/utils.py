from typing import List
import os


def read_input(day: int) -> List[str]:
    code_dir = os.path.dirname(__file__)
    input_dir = os.path.normpath(os.path.join(code_dir, "..", "input"))
    input_file = os.path.join(input_dir, f"day{day}.txt")

    with open(input_file, "r") as f:
        lines = f.readlines()

    return [line.strip() for line in lines]
