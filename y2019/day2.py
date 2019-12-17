# type: ignore
import y2019.IntComputer as IC

# tests
cp = IC.IntComputer([1,0,0,0,99])
cp.run()
cp.program == [2,0,0,0,99]

cp = IC.IntComputer([2,3,0,3,99])
cp.run()
cp.program == [2,3,0,6,99]

cp = IC.IntComputer([2,4,4,5,99,0])
cp.run()
cp.program == [2,4,4,5,99,9801]

cp = IC.IntComputer([1,1,1,4,99,5,6,0,99])
cp.run()
cp.program == [30,1,1,4,2,5,6,0,99]

# read input
f = open("y2019/day2-input.txt")
raw = f.readline()
f.close()
program = [int(x) for x in raw.replace("\n", "").split(",")]

# part 1
cp = IC.IntComputer(program)
cp.run_noun_verb(12, 2)
cp.program[0] # answer

# part 2
cp = IC.IntComputer(program)
res = cp.find_noun_verb(19690720)
100 * res[0] + res[1] # answer
