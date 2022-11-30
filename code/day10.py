from typing import Optional, Tuple
import numpy as np

input = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]

with open("day10-input.txt", "r") as f:
    input = [line.strip() for line in f.readlines()]

chunk_chars = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

# part 1
def first_illegal_character(line: str) -> Tuple[Optional[str], Optional[str]]:
    """Returns expected, found characters that cause the first illegal character"""
    opened = []

    for char in line:
        if char in chunk_chars.keys():
            # keys are the open characters
            opened.append(char)
        elif char in chunk_chars.values():
            # values are the close characters
            # char should close the last character in opened
            if chunk_chars[opened[len(opened) - 1]] != char:
                expected = chunk_chars[opened[len(opened) - 1]]
                return (expected, char)
            else:
                opened.pop()

    return (None, None)

def score_first_illegal_characters(line: str) -> int:
    score_chars = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    _, illegal_char = first_illegal_character(line)

    if illegal_char is None:
        return 0
    else:
        return score_chars[illegal_char]

[first_illegal_character(line) for line in input]
sum([score_first_illegal_characters(line) for line in input]) # answer part 1

# part 2
def is_corrupted_line(line: str) -> bool:
    _, illegal_char = first_illegal_character(line)
    return illegal_char is not None

incomplete_lines = [line for line in input if not is_corrupted_line(line)]

def find_completion_string(line: str) -> str:
    opened = []

    for char in line:
        if char in chunk_chars.keys():
            # keys are the open characters
            opened.append(char)
        elif char in chunk_chars.values():
            # values are the close characters
            # char should close the last character in opened
            if chunk_chars[opened[len(opened) - 1]] != char:
                raise ValueError("Found a corrupted line still!")
            else:
                opened.pop()

    res = ""
    for char in reversed(opened):
        res += chunk_chars[char]

    return res

def score_completion_string(line: str) -> int:
    score_chars = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    compl_str = find_completion_string(line)
    score = 0

    for char in compl_str:
        score *= 5
        score += score_chars[char]

    return score

[score_completion_string(line) for line in incomplete_lines]
int(np.median([score_completion_string(line) for line in incomplete_lines])) # answer part 2
