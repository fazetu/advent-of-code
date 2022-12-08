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
    all_sizes: dict[str, tuple[str, int]] = {}
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

def get_dir_sizes(all_sizes: dict[str, tuple[str, int]]) -> dict[str, int]:
    dir_sizes: dict[str, int] = {}

    for path, (type, size) in all_sizes.items():
        if type == "file":
            dict_insert_add(dir_sizes, os.path.dirname(path), size)

    return dir_sizes

def is_top_dir(d: str) -> bool:
    return d.count("/") == 1

def all_top_dirs(dir_sizes: dict[str, int]) -> bool:
    nms = list(dir_sizes.keys())
    return all([is_top_dir(nm) for nm in nms])

def combine_dir_sizes(dir_sizes: dict[str, int], include_orig: bool = True) -> dict[str, int]:
    orig_dirs: dict[str, int] = {}

    while not all_top_dirs(dir_sizes):
        new_dir_sizes: dict[str, int] = {}

        for path, size in dir_sizes.items():
            if not is_top_dir(path):
                dname = os.path.dirname(path)
                dict_insert_add(new_dir_sizes, dname, size)
                dict_insert_add(orig_dirs, path, size)
            else:
                dict_insert_add(new_dir_sizes, path, size)

        dir_sizes = new_dir_sizes

    if include_orig:
        return {**dir_sizes, **orig_dirs}
    else:
        return dir_sizes

# part 1
all_sizes = get_all_sizes(input)
dir_sizes = get_dir_sizes(all_sizes)
comb_sizes = combine_dir_sizes(dir_sizes)
small_sizes = [size for size in comb_sizes.values() if size <= 100_000]

print(all_sizes)
print("")
print(dir_sizes)
print("")
print(comb_sizes)
print("")

# answer 1
print(sum(small_sizes))
