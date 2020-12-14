# part 2
with open("day13-input.txt") as f:
    input = f.readlines()

buses = input[1].strip().split(",")
buses = ["x" if x == "x" else int(x) for x in buses]

mods = {bus: -i % bus for i, bus in enumerate(buses) if bus != "x"}

vals = list(reversed(sorted(mods)))
val = mods[vals[0]]
r = vals[0]

for b in vals[1:]:
    while val % b != mods[b]:
        val += r
    r *= b

val # answer 2
