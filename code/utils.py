from typing import Any, Union
import os


def _read_input(input_file: str) -> list[str]:
    with open(input_file, "r") as f:
        lines = f.readlines()
        
    return [line.replace("\n", "") for line in lines]


def read_input(day: int) -> list[str]:
    """Helper to read the given day's input file

    Assumes the input file is in the input folder with the name dayN.txt. Reads
    all the lines and strips ending new line characters.

    Args:
        day (int): Day number to read in.

    Returns:
        List[str]: Lines in the input file.
    """
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
