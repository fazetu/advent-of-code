from typing import List, Tuple, Set
import re

input = [
    "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)",
    "trh fvjkl sbzzf mxmxvkd (contains dairy)",
    "sqjhc fvjkl (contains soy)",
    "sqjhc mxmxvkd sbzzf (contains fish)",
]

# with open("day21-input.txt", "r") as f:
#     input = [line.strip() for line in f.readlines()]

def parse_foods(foods: List[str]) -> Tuple[List[List[str]], List[List[str]]]:
    p = re.compile("^(.*) \\(contains (.*)\\)$")
    ingredients = []
    allergens = []

    for food in foods:
        found = p.findall(food)
        i, a = found[0]
        ingredients.append(i.split(" "))
        allergens.append(a.split(", "))

    return (ingredients, allergens)

def find_allergens_ingredients(
    ingredients: List[List[str]], allergens: List[List[str]], allergen: str
) -> Set[str]:
    x = list()

    for ing, all in zip(ingredients, allergens):
        if allergen in all:
            x.append(ing)

    return set.intersection(*[set(l) for l in x])

ingredients, allergens = parse_foods(input)

unique_ingredients = set.union(*[set(l) for l in ingredients])
unique_allergens = set.union(*[set(l) for l in allergens])

possible_allergen_ingredients = set.union(
    *[find_allergens_ingredients(ingredients, allergens, allergen) for allergen in list(unique_allergens)]
)
non_allergen_ingredients = unique_ingredients - possible_allergen_ingredients

# part 1
count = 0

for ing in non_allergen_ingredients:
    for food_ing in ingredients:
        count += ing in food_ing

count # answer part 1

# part 2
translator = {allergen: "" for allergen in unique_allergens}

while True:
    if all([v != "" for v in translator.values()]):
        break

    
    

for allergen in unique_allergens:
    ings = find_allergens_ingredients(ingredients, allergens, allergen)


for ing, all in zip(ingredients, allergens):
    if len(all) == 1:
        for i in ing:
            if i in possible_allergen_ingredients:
                translator[i] = all[0]


    if ing in possible_allergen_ingredients:
        translator[ing] = 

def find_ingredients_allergens(
    ingredients: List[List[str]], allergens: List[List[str]], ingredient: str
) -> Set[str]:
    x = list()

    for ing, all in zip(ingredients, allergens):
        if ingredient in ing:
            x.append(all)

    return set.intersection(*[set(l) for l in x])

find_ingredients_allergens(ingredients, allergens, "mxmxvkd")

for allergen in possible_allergen_ingredients:

    allergens_to_check = list()

    for ingredient_list, allergen_list in zip(ingredients, allergens):
        if ing in ingredient_list:
            allergens_to_check.append(allergen_list)

    translator[ing] = set.intersection(*[set(l) for l in allergens_to_check])

translator
