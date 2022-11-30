from typing import Dict, List, Tuple, Union

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

with open("day14-input.txt", "r") as f:
    input = [line.strip() for line in f.readlines()]

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

def count_elements(template: Union[List[str], str]) -> Dict[str, int]:
    res = {}

    for element in template:
        if element in res:
            res[element] += 1
        else:
            res[element] = 1

    return res

# part 1
rules = make_rules_dict(input[2:])
res = step_n(input[0], rules, 10)
counts = count_elements(res)
max(counts.values()) - min(counts.values()) # answer part 1

# part 2
# must take a different approach for this many iterations - it grows too fast
# res = step_n(input[0], rules, 40)
# counts = count_elements(res)
# max(counts.values()) - min(counts.values()) # answer part 2

######################################################################

# Different approach
def make_rules_dict2(rules: List[str]) -> Dict[Tuple[str, str], str]:
    res = {}
    
    for rule in rules:
        k, v = rule.split(" -> ")
        a, b = k[0], k[1]
        res[(a, b)] = v

    return res

def count_pairs(template: str) -> Dict[Tuple[str, str], int]:
    counts = {}
    pairs = find_pairs(template)

    for pair in pairs:
        a, b = pair[0], pair[1]
        if (a, b) not in counts:
            counts[(a, b)] = 1
        else:
            counts[(a, b)] += 1

    return counts

def run_step_n(template: str, rules_lines: List[str], n: int = 10) -> Tuple[Dict[str, int], Dict[str, int]]:
    rules_dict = make_rules_dict(rules_lines)
    pairs_counts = count_elements(find_pairs(template))
    element_counts = count_elements(template)

    for i in range(n):
        # go through all pairs and insert new elements and count elements added
        orig = pairs_counts.copy()
        for pair, count in orig.items():
            if count == 0:
                continue

            add = rules_dict[pair]
            new1 = pair[0] + add
            new2 = add + pair[1]

            if add not in element_counts:
                element_counts[add] = 0

            if new1 not in pairs_counts:
                pairs_counts[new1] = 0

            if new2 not in pairs_counts:
                pairs_counts[new2] = 0

            pairs_counts[new1] += count
            pairs_counts[new2] += count
            element_counts[add] += count

            if (pairs_counts[pair] - count) <= 0:
                pairs_counts[pair] = 0
            else:
                pairs_counts[pair] -= count

    return (pairs_counts, element_counts)


# part 1
_, element_counts = run_step_n(input[0], input[2:], 10)
max(element_counts.values()) - min(element_counts.values()) # answer part 1

# part 2
_, element_counts = run_step_n(input[0], input[2:], 40)
max(element_counts.values()) - min(element_counts.values()) # answer part 2
