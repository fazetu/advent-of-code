# part 2
with open("day13-input.txt") as f:
    input = f.readlines()

buses = input[1].strip().split(",")
buses = ["x" if x == "x" else int(x) for x in buses]

buses = [7,13,"x","x",59,"x",31,19]

mods = {bus: (bus - i) % bus for i, bus in enumerate(buses) if bus != "x"}

buses_int = [x for x in buses if x != "x"]
buses_s = list(reversed(sorted(buses_int)))

increase = buses_s[0] # max bus number
t = mods[increase]

for bus in buses_s[1:]:
    while t % bus != mods[bus]:
        t += increase
    increase *= bus

t # answer 2
