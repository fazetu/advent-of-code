import re

from utils import read_input

lines = read_input(1)


# part 1
def prep1_single(line: str) -> str:
    line = re.sub("[a-zA-Z]", "", line)
    return line[0] + line[-1]


def prep1(lines: list[str]) -> list[str]:
    return [prep1_single(line) for line in lines]


print(sum(map(int, prep1(lines))))

# part 2
map_number_words_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

test_lines = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]


def prepend_first_number_word(line: str, m: dict[str, str]) -> str:
    # going from the front of the string, replace the first number word
    slice = ""
    for i, char in enumerate(line):
        slice += char

        for word, digit in m.items():
            if slice.endswith(word):
                return slice[: (i - len(word) + 1)] + digit + word + line[(i + 1) :]

    return line


assert prepend_first_number_word("abcone", map_number_words_to_digit) == "abc1one"
assert prepend_first_number_word("ttttwo", map_number_words_to_digit) == "ttt2two"
assert prepend_first_number_word("eight8asdf", map_number_words_to_digit) == "8eight8asdf"


def append_last_number_word(line: str, m: dict[str, str]) -> str:
    # reverse the mapping key and apply the going-forward direction one
    m_rev = {k[::-1]: v for k, v in m.copy().items()}
    return prepend_first_number_word(line[::-1], m_rev)[::-1]


assert append_last_number_word("abcdone", map_number_words_to_digit) == "abcdone1"
assert append_last_number_word("abcdone123", map_number_words_to_digit) == "abcdone1123"
assert append_last_number_word("one1234", map_number_words_to_digit) == "one11234"


def prep2_single(line: str) -> str:
    first = line[0]
    last = line[-1]

    # don't do extra work on this line if it already starts and ends with digit
    if (
        first in map_number_words_to_digit.values()
        and last in map_number_words_to_digit.values()
    ):
        pass
    elif first in map_number_words_to_digit.values():
        line = append_last_number_word(line, map_number_words_to_digit)
    elif last in map_number_words_to_digit.values():
        line = prepend_first_number_word(line, map_number_words_to_digit)
    else:
        line = prepend_first_number_word(
            append_last_number_word(line, map_number_words_to_digit),
            map_number_words_to_digit,
        )

    line = re.sub("[a-z]", "", line)
    return line[0] + line[-1]


assert prep2_single(test_lines[0]) == "29"
assert prep2_single(test_lines[1]) == "83"
assert prep2_single(test_lines[2]) == "13"
assert prep2_single(test_lines[3]) == "24"


def prep2(lines: list[str]) -> list[str]:
    return [prep2_single(line) for line in lines]


assert sum(map(int, prep2(test_lines))) == 281

print(sum(map(int, prep2(lines))))
