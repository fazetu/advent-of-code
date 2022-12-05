from __future__ import annotations
from typing import List, Tuple
import re
from utils import read_input


class Stack:
    def __init__(self, order: List[str]):
        # the order of the crates from bottom to top
        # append puts things on the top
        self.order = order

    def __str__(self) -> str:
        res = ""

        for item in self.order:
            res += f" [{item}]"

        return res.strip()

    def __repr__(self) -> str:
        return self.__str__()

    def take_from_top(self, n: int) -> List[str]:
        start = len(self.order) - n
        taken = self.order[start:]
        leftover = self.order[:start]
        self.order = leftover
        return taken

    def put_on_top(self, items: List[str]):
        # the order of the crates in items are from bottom to top
        self.order += items

    @property
    def top(self) -> str:
        return self.order[len(self.order) - 1]


class Stacks:
    def __init__(self, stacks: List[Stack]):
        self.stacks = stacks

    def __str__(self) -> str:
        lines = []

        for i, stack in enumerate(self.stacks):
            lines.append(f"{i + 1}: {stack.__str__()}")

        return "\n".join(lines)

    def __repr__(self) -> str:
        return str(self)

    @property
    def tops(self) -> List[str]:
        return [stack.top for stack in self.stacks]

    @property
    def answer(self) -> str:
        return "".join(self.tops)

    def move_n_from_i_to_j(self, n: int, i: int, j: int, one_at_a_time: bool = True):
        taken = self.stacks[i].take_from_top(n)

        if one_at_a_time:
            taken = list(reversed(taken))

        self.stacks[j].put_on_top(taken)

    def run_command(self, command: str, one_at_a_time: bool = True):
        m = re.match("move (\\d+) from (\\d+) to (\\d+)", command)

        if m:
            n, i, j = m.groups()
            n, i, j = int(n), int(i), int(j)
            # decrement i and j to match python's 0-based indexing
            self.move_n_from_i_to_j(n, i - 1, j - 1, one_at_a_time)
        else:
            raise ValueError(f"No matches found: {command}")

    def run_commands(
        self, commands: List[str], one_at_a_time: bool = True, verbose: bool = False
    ) -> None:
        if verbose:
            print("STEP 0")
            print(stacks)
            print("")

        for i, command in enumerate(commands):
            self.run_command(command, one_at_a_time)

            if verbose:
                print(stacks)
                print(f"STEP {i + 1}")
                print("")

    @classmethod
    def from_strings(cls, strings: List[str]) -> Stacks:
        id_i = len(strings) - 1
        id_line = strings[id_i]
        ids = re.findall("\\d", id_line)

        crate_lines = strings[:id_i]
        crate_lines_top_to_bottom = list(reversed(crate_lines))

        stacks = []

        for id in ids:
            i = id_line.find(id)
            o = []

            for row in crate_lines_top_to_bottom:
                crate = row[i]

                if crate != " ":
                    o.append(crate)

            stack = Stack(o)
            stacks.append(stack)

        return cls(stacks)


def split_input(input: List[str]) -> Tuple[List[str], List[str]]:
    i = 0

    for i, line in enumerate(input):
        if line == "":
            break

    return (input[:i], input[(i + 1) :])


# input = [
#     "    [D]    ",
#     "[N] [C]    ",
#     "[Z] [M] [P]",
#     " 1   2   3 ",
#     "",
#     "move 1 from 2 to 1",
#     "move 3 from 1 to 3",
#     "move 2 from 2 to 1",
#     "move 1 from 1 to 2",
# ]

input = read_input(5)

# part 1
crate_lines, command_lines = split_input(input)
stacks = Stacks.from_strings(crate_lines)
stacks.run_commands(command_lines, one_at_a_time=True)

# answer 1
print(stacks.answer)

# part 2
crate_lines, command_lines = split_input(input)
stacks = Stacks.from_strings(crate_lines)
stacks.run_commands(command_lines, one_at_a_time=False)

# answer 2
print(stacks.answer)
