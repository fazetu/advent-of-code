from typing import Any, Union, Optional
import os
import re
import inspect


def _read_input(input_file: str) -> list[str]:
    with open(input_file, "r") as f:
        lines = f.readlines()

    return [line.replace("\n", "") for line in lines]


def read_input(day: Optional[int] = None) -> list[str]:
    """Helper to read the given day's input file

    Assumes the input file is in the input folder with the name dayN.txt. Reads
    all the lines and strips ending new line characters.

    If assuming the day number, assumes the calling file is named dayN.py.

    Args:
        day (Optional[int], optional): Day number to read in. If left as None,
            tries to assume the day number from the calling file. Defaults to
            None.

    Returns:
        List[str]: Lines in the input file.
    """
    if day is None:
        frame = inspect.stack()[1]
        calling_filename = frame.filename
        s = re.sub("day(\\d+)\\.py", "\\1", os.path.basename(calling_filename))  # type: ignore
        day = int(s)

    code_dir = os.path.dirname(__file__)
    input_dir = os.path.normpath(os.path.join(code_dir, "..", "input"))
    input_file = os.path.join(input_dir, f"day{day}.txt")
    return _read_input(input_file)


def dict_insert_add(
    d: Union[dict[Any, int], dict[Any, float]], k: Any, v: Union[int, float]
) -> None:
    """Modifies the input dictionary by either inserting the key value pair if
    the key is not in the dictionary. Otherwise, if the key is in the
    dictionary, add the value to the existing value.

    Args:
        d (dict[Any, NUMBER]): Dictionary to modify inplace.
    """
    if k in d.keys():
        d[k] += v  # type: ignore
    else:
        d[k] = v  # type: ignore
