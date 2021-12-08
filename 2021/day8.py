from typing import Dict, Set, Any, List

input = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
]

with open("day8-input.txt", "r") as f:
    input = [line.strip() for line in f.readlines()]

# part 1
def count_easy_digits(lines: List[str]) -> int:
    n = 0

    for line in lines:
        _, output_values = line.split(" | ")
        for encoded_segment in output_values.split(" "):
        # 2, 4, 3, 7 are the number of segments for
        # 1, 4, 7, 8 respectively
        # these segment counts are unique for those digits
            n += len(encoded_segment) in [2, 4, 3, 7]

    return n

count_easy_digits(input) # answer part 1

# part 2
#  aaaa 
# b    c
# b    c
#  dddd 
# e    f
# e    f
#  gggg 
DIGIT_SEGMENTS = {
    0: "abcefg",  # 6
    1: "cf",      # 2 *
    2: "acdeg",   # 5
    3: "acdfg",   # 5
    4: "bcdf",    # 4 *
    5: "abdfg",   # 5
    6: "abdefg",  # 6
    7: "acf",     # 3 *
    8: "abcdefg", # 7 *
    9: "abcdfg",  # 6
}

{k: len(v) for k, v in DIGIT_SEGMENTS.items()}

def same_letters(x: str, y: str) -> bool:
    if len(x) != len(y):
        return False
    return len(set(x).intersection(set(y))) == len(x)

def single_set_value(x: Set) -> Any:
    if len(x) == 1:
        return list(x)[0]
    else:
        raise ValueError("More than 1 value in set")

def make_segment_mapping(ten_encoded_digits: str) -> Dict[str, str]:
    digits = ten_encoded_digits.split(" ")

    # check for standard expected input
    if len(digits) != 10:
        raise ValueError("Couldn't find 10 digits in input")

    # pick out known digits
    one = [val for val in digits if len(val) == 2][0]
    four = [val for val in digits if len(val) == 4][0]
    seven = [val for val in digits if len(val) == 3][0]
    eight = [val for val in digits if len(val) == 7][0]

    # pick out remaining categories
    seg5s = [val for val in digits if len(val) == 5] # digits 2, 3, and 5
    seg6s = [val for val in digits if len(val) == 6] # digits 0, 6, and 9

    # the difference between 7 and 1 is the a segment
    segments_a = set(seven) - set(one)

    # the difference between 8 and 4 are the a, e, g segments
    segments_aeg = set(eight) - set(four)

    # the difference between 8 and 7 are the b, d, e, g segments
    segments_bdeg = set(eight) - set(seven)

    # the common segments in all the segment 5 digits are a, d, g segments
    segments_adg = set.intersection(*[set(l) for l in seg5s])

    # the common segments in all the segment 6 digits are a, b, f, g segments
    segments_abfg = set.intersection(*[set(l) for l in seg6s])

    # some more sets
    segments_ag = set.intersection(segments_aeg, segments_adg)
    segments_cf = set(one)

    # set math to determine remaining singles
    segments_g = segments_ag - segments_a
    segments_e = segments_aeg - segments_ag
    segments_d = segments_adg - segments_ag
    segments_b = segments_bdeg - segments_d - segments_e - segments_g
    segments_f = segments_abfg - segments_a - segments_b - segments_g
    segments_c = segments_cf - segments_f

    return {
        single_set_value(segments_a): "a",
        single_set_value(segments_b): "b",
        single_set_value(segments_c): "c",
        single_set_value(segments_d): "d",
        single_set_value(segments_e): "e",
        single_set_value(segments_f): "f",
        single_set_value(segments_g): "g",
    }

def decode_digit(encoded_digit: str, mapping: Dict[str, str]) -> str:
    return "".join([mapping[s] for s in encoded_digit])

def encoded_digit_to_int(encoded_digit: str, mapping: Dict[str, str]) -> int:
    decoded_digit = decode_digit(encoded_digit, mapping)

    for k, v in DIGIT_SEGMENTS.items():
        if same_letters(v, decoded_digit):
            return k
    
    raise ValueError("Did not find a decoded int!!")

def decode_line(line: str) -> int:
    ten_encoded_digits, output_digits = line.split(" | ")
    mapping = make_segment_mapping(ten_encoded_digits)

    res = ""
    for encoded_digit in output_digits.split(" "):
        n = encoded_digit_to_int(encoded_digit, mapping)
        res += str(n)
    
    return int(res)

sum([decode_line(line) for line in input]) # answer part 2
