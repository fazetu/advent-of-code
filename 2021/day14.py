from typing import Dict, List

input = [
    "NNCB",
    "",
    "CH -> B",
    "HH -> N",
    "CB -> H",
    "NH -> C",
    "HB -> C",
    "HC -> B",
    "HN -> C",
    "NN -> C",
    "BH -> H",
    "NC -> B",
    "NB -> B",
    "BN -> B",
    "BB -> N",
    "BC -> B",
    "CC -> N",
    "CN -> C",
]

# with open("day14-input.txt", "r") as f:
#     input = [line.strip() for line in f.readlines()]

def find_pairs(template: str) -> List[str]:
    l = len(template) + 1
    res = []

    for i in range(l - 2):
        res.append(template[i:(i + 2)])

    return res

def make_rules_dict(rules: List[str]) -> Dict[str, str]:
    res = {}
    
    for rule in rules:
        k, v = rule.split(" -> ")
        res[k] = v

    return res

def step(template: str, rules_dict: Dict[str, str]) -> str:
    pairs = find_pairs(template)
    res = ""

    for i, pair in enumerate(pairs):
        if pair in rules_dict:
            # since pairs overlap only add first value of pair
            # later iterations will add the previous pair's second value
            to_add = (pair[0] + rules_dict[pair])

            # for the last pair add the second value as well
            if i == (len(pairs) - 1):
                to_add += pair[1]

            res += to_add

    return res

def step_n(template: str, rules_dict: Dict[str, str], n: int) -> str:
    for _ in range(n):
        template = step(template, rules_dict)

    return template

def count_elements(template: str) -> Dict[str, int]:
    res = {}

    for element in template:
        if element in res:
            res[element] += 1
        else:
            res[element] = 1

    return res

rules = make_rules_dict(input[2:])

# part 1
res = step_n(input[0], rules, 10)
counts = count_elements(res)
max(counts.values()) - min(counts.values()) # answer part 1

# part 2
# must take a different approach for this many iterations - it grows too fast
res = step_n(input[0], rules, 40)
counts = count_elements(res)
max(counts.values()) - min(counts.values()) # answer part 2
