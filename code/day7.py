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

def dir_name(d: str) -> str:
    return d.replace("dir", "").strip()

def size_of_file(f: str) -> int:
    size, _ = f.split(" ")
    return int(size)

def get_all_dirs(lines: list[str]) -> set[str]:
    dirs = set()

    for line in lines:
        if line.startswith("$ cd"):
            nm = line.replace("$ cd", "").strip()
        elif line.startswith("dir"):
            nm = dir_name(line)
        else:
            continue

        if nm != "..":
            dirs.add(nm)

    return dirs

def get_contents_of_dir(d: str, lines: list[str]) -> set[str]:
    contents = set()
    in_dir = False

    for line in lines:
        if line.startswith(f"$ cd {d}"):
            in_dir = True

        if in_dir:
            if line.startswith("$ ls") or line.startswith(f"$ cd {d}"):
                continue
            elif line.startswith("$ cd"):
                in_dir = False
            else:
                contents.add(line)

    return contents

def get_size_of_dir(d: str, lines: list[str]) -> int:
    print(d)
    contents = get_contents_of_dir(d, lines)
    files = set(filter(lambda x: not x.startswith("dir"), contents))
    dirs = contents.difference(files)
    size = sum([size_of_file(file) for file in files])

    if len(dirs) > 0:
        for d in dirs:
            size += get_size_of_dir(dir_name(d), lines)
        
    return size

# part 1
ds = get_all_dirs(input)
get_contents_of_dir("btc", input)
get_contents_of_dir("pjts", input)

# ds = ds.difference("/")  # don't include /
sizes = {d: get_size_of_dir(d, input) for d in ds}
sum_small = sum([size for size in sizes.values() if size < 100_000])

# answer 1
print(sum_small)
