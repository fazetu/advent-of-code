from typing import Any
import os
from utils import read_input

# input = [
#     "$ cd /",
#     "$ ls",
#     "dir a",
#     "14848514 b.txt",
#     "8504156 c.dat",
#     "dir d",
#     "$ cd a",
#     "$ ls",
#     "dir e",
#     "29116 f",
#     "2557 g",
#     "62596 h.lst",
#     "$ cd e",
#     "$ ls",
#     "584 i",
#     "$ cd ..",
#     "$ cd ..",
#     "$ cd d",
#     "$ ls",
#     "4060174 j",
#     "8033020 d.log",
#     "5626152 d.ext",
#     "7214296 k",
# ]

input = read_input(7)


def dict_insert_add(d: dict[Any, int], k: Any, v: int):
    # modifies dictionary in place!
    if k in d:
        d[k] += v
    else:
        d[k] = v


def join_path(*args: str) -> str:
    return os.path.normpath(os.path.join(*args)).replace("\\", "/")


def get_all_sizes(lines: list[str]) -> dict[str, tuple[str, int]]:
    in_ls = False
    all_sizes: dict[str, tuple[str, int]] = {"/": ("dir", 0)}
    curr_location = []

    for line in lines:
        if line.startswith("$ cd"):
            in_ls = False
            nm = line.replace("$ cd", "").strip()
            curr_location.append(nm)
        elif line == "$ ls":
            in_ls = True
        elif line.startswith("dir"):
            if in_ls:
                nm = line.replace("dir", "").strip()
                all_sizes[join_path(*curr_location, nm)] = ("dir", 0)
        else:
            if in_ls:
                size, nm = line.split(" ")
                all_sizes[join_path(*curr_location, nm)] = ("file", int(size))

    return all_sizes


def get_all_dirs(sizes: dict[str, tuple[str, int]]) -> list[str]:
    dirs = []
    for k, (type, _) in sizes.items():
        if type == "dir":
            dirs.append(k)

    return dirs


def get_dir_size(sizes: dict[str, tuple[str, int]], dir_name: str) -> int:
    total_size = 0

    for path, (_, size) in sizes.items():
        if path.startswith(dir_name):
            total_size += size

    return total_size


all_sizes = get_all_sizes(input)
dir_sizes = {
    dir_name: get_dir_size(all_sizes, dir_name) for dir_name in get_all_dirs(all_sizes)
}


# part 1
small_sizes = [size for size in dir_sizes.values() if size < 100_000]

# answer 1
print(sum(small_sizes))

# answer 2
total_space = 70_000_000
needed_space = 30_000_000
total_used = dir_sizes["/"]
total_free = total_space - total_used
to_free = needed_space - total_free
delete_candidates = [
    dir_name for dir_name, size in dir_sizes.items() if size >= to_free
]
to_delete = sorted(delete_candidates, key=lambda x: dir_sizes[x])[0]

# answer 2
print(dir_sizes[to_delete])
