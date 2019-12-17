# type: ignore
class IntComputer:
    def __init__(self, program, pointer = 0):
        self.pointer = pointer
        self.program = program
        self.orig_pointer = pointer
        self.orig_program = program.copy()

    def show(self):
        print(self.program)

    def reset(self):
        self.pointer = self.orig_pointer.copy()
        self.program = self.orig_program

    def get(self, i):
        return self.program[i]

    def get_current(self):
        return self.get(self.pointer)

    def op1(self):
        if self.get_current() != 1:
            return None
        j1 = self.get(self.pointer + 1)
        j2 = self.get(self.pointer + 2)
        j3 = self.get(self.pointer + 3)
        self.program[j3] = self.get(j1) + self.get(j2)
        self.pointer += 4

    def op2(self):
        if self.get_current() != 2:
            return None
        j1 = self.get(self.pointer + 1)
        j2 = self.get(self.pointer + 2)
        j3 = self.get(self.pointer + 3)
        self.program[j3] = self.get(j1) * self.get(j2)
        self.pointer += 4
        
    def op(self, op_code):
        if op_code == 1:
            self.op1()
        elif op_code == 2:
            self.op2()

    def run(self):
        op_code = self.get_current()
        while op_code != 99:
            self.op(op_code)
            op_code = self.get_current()

    def run_noun_verb(self, noun, verb):
        self.program[1] = noun
        self.program[2] = verb
        self.run()

    def find_noun_verb(self, value, verbose = False):
        for noun in range(100):
            for verb in range(100):
                self.run_noun_verb(noun, verb)
                first_val = self.program[0]
                if verbose:
                    print(f"noun: {noun}, verb: {verb}, value: {first_val}")
                if first_val == value:
                    return (noun, verb)
                else:
                    self.reset()
             
# tests
"""
program = [1,9,10,3,2,3,11,0,99,30,40,50]
cp = IntComputer(program)
cp.run()
cp.show()
"""

# read input
f = open("2019/day2-input.txt")
raw = f.readline()
f.close()
program = [int(x) for x in raw.replace("\n", "").split(",")]

"""
# part 1
cp = IntComputer(program)
cp.run_noun_verb(12, 2)
cp.program[0] # answer
"""

# part 2
cp = IntComputer(program)
res = cp.find_noun_verb(19690720, True)
100 * res[0] + res[1] # answer
