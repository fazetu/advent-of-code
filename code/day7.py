
input = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
]

def get_all_dirs(lines: list[str]) -> set[str]:
    dirs = set()

    for line in lines:
        if line.startswith("$ cd"):
            dir_name = line.replace("$ cd", "").strip()
        elif line.startswith("dir"):
            dir_name = line.replace("dir", "").strip()
        else:
            continue

        if dir_name != "..":
            dirs.add(dir_name)

    return dirs

def get_contents_of_dir(d: str, lines: list[str]) -> set[str]:
    contents = set()
    in_dir = False

    for line in lines:
        if line.startswith(f"$ cd {d}"):
            in_dir = True

        if in_dir:
            if line.startswith("$ ls"):
                continue
            elif line.startswith(f"$ cd {d}"):
                continue
            elif line.startswith("$ cd"):
                in_dir = False
            else:
                contents.add(line)

    return contents

# get_all_dirs(input)

contents = get_contents_of_dir("a", input)
files = set(filter(lambda x: not x.startswith("dir"), contents))
dirs = contents.difference(files)
