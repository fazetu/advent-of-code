from __future__ import annotations
from typing import Dict, List

input = [
    "yw-MN",
    "wn-XB",
    "DG-dc",
    "MN-wn",
    "yw-DG",
    "start-dc",
    "start-ah",
    "MN-start",
    "fi-yw",
    "XB-fi",
    "wn-ah",
    "MN-ah",
    "MN-dc",
    "end-yw",
    "fi-end",
    "th-fi",
    "end-XB",
    "dc-XB",
    "yw-XN",
    "wn-yw",
    "dc-ah",
    "MN-fi",
    "wn-DG",
]

input1 = [
    "start-A",
    "start-b",
    "A-c",
    "A-b",
    "b-d",
    "A-end",
    "b-end",
]

input2 = [
    "dc-end",
    "HN-start",
    "start-kj",
    "dc-start",
    "dc-HN",
    "LN-dc",
    "HN-end",
    "kj-sa",
    "kj-HN",
    "kj-dc",
]

input3 = [
    "fs-end",
    "he-DX",
    "fs-he",
    "start-DX",
    "pj-DX",
    "end-zg",
    "zg-sl",
    "zg-pj",
    "pj-he",
    "RW-he",
    "fs-DX",
    "pj-RW",
    "zg-RW",
    "start-pj",
    "he-WI",
    "zg-he",
    "pj-fs",
    "start-RW",
]


class Path:
    def __init__(self, start: str, end: str):
        self.start = start
        self.end = end

    @classmethod
    def from_string(cls, string: str) -> Path:
        start, end = string.split("-")
        return cls(start, end)


class Caves:
    def __init__(self, paths: List[Path]):
        self.paths = paths

    @classmethod
    def from_strings(cls, strings: List[str]) -> Caves:
        paths = [Path.from_string(line) for line in strings]
        return cls(paths)

    @staticmethod
    def is_big_cave(cave: str) -> bool:
        return cave.isupper()

    def count_small_caves(self, visited_caves: List[str]) -> Dict[str, int]:
        small_cave_count = {}

        for cave in visited_caves:
            if not self.is_big_cave(cave):
                if cave in small_cave_count:
                    small_cave_count[cave] += 1
                else:
                    small_cave_count[cave] = 1

        return small_cave_count

    def cave_append(
        self, caves: List[str], visited: List[str], cave: str, part2: bool = False
    ):
        if cave in ["start", "end"]:
            if cave in visited:
                return None

        if self.is_big_cave(cave):
            caves.append(cave)
        else:
            if part2:
                count = self.count_small_caves(visited)
                if any([n == 2 for n in count.values()]):
                    # can only add if cave has not been visited yet
                    if cave not in visited:
                        caves.append(cave)
                else:
                    caves.append(cave)
            else:
                if cave not in visited:
                    caves.append(cave)

    def find_connections(
        self, cave: str, visited: List[str], part2: bool = False
    ) -> List[str]:
        res: List[str] = []

        if cave == "end":
            return res

        for path in self.paths:
            if cave == path.start:
                self.cave_append(res, visited, path.end, part2)
            elif cave == path.end:
                self.cave_append(res, visited, path.start, part2)

        return res

    def _find_paths(self, paths: List[List[str]] = [], part2: bool = False):
        for path in paths:
            next_caves = self.find_connections(path[len(path) - 1], path, part2)
            for n in next_caves:
                if n == "start":
                    continue
                paths.append(path + [n])

    def find_paths(self, part2: bool = False) -> List[List[str]]:
        paths = [["start"]]
        self._find_paths(paths, part2)
        return paths

    def find_final_paths(self, part2: bool = False) -> List[List[str]]:
        paths = self.find_paths(part2)
        final_paths = [path for path in paths if path[len(path) - 1] == "end"]
        return final_paths

    def answer_part_1(self) -> int:
        return len(self.find_final_paths(False))

    def answer_part_2(self) -> int:
        return len(self.find_final_paths(True))


# part 1
caves = Caves.from_strings(input)
caves.answer_part_1()  # answer part 1

caves = Caves.from_strings(input1)
caves.answer_part_1()  # 10

caves = Caves.from_strings(input2)
caves.answer_part_1()  # 19

caves = Caves.from_strings(input3)
caves.answer_part_1()  # 226

# part 2
caves = Caves.from_strings(input)
caves.answer_part_2()  # answer part 2

caves = Caves.from_strings(input1)
caves.answer_part_2()

caves = Caves.from_strings(input2)
caves.answer_part_2()

caves = Caves.from_strings(input3)
caves.answer_part_2()
