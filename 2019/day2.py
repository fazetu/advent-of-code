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
        self.pointer = self.orig_pointer
        self.program = self.orig_program

    def current_code(self):
        return self.program[self.pointer]

    def op1(self):
        if self.current_code() != 1:
            return None

        i = self.pointer
        prog = self.program.copy()
        j1 = prog[i + 1]
        j2 = prog[i + 2]
        j3 = prog[i + 3]
        prog[j3] = prog[j1] + prog[j2]
        self.program = prog

    def op2(self):
        if self.current_code() != 2:
            return None

        i = self.pointer
        prog = self.program.copy()
        j1 = prog[i + 1]
        j2 = prog[i + 2]
        j3 = prog[i + 3]
        prog[j3] = prog[j1] * prog[j2]
        self.program = prog

    def move_pointer(self, op_code):
        if op_code == 1 or op_code == 2:
            self.pointer += 4
        
    def op(self, op_code):
        if op_code == 1:
            self.op1()
            self.move_pointer(op_code)
        elif op_code == 2:
            self.op2()
            self.move_pointer(op_code)

    def run(self):
        op_code = self.current_code()
        while op_code != 99:
            self.op(op_code)
            op_code = self.current_code()

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
             

# cp = IntComputer([1,9,10,3,2,3,11,0,99,30,40,50])
# cp.run()
# cp.show()

# read input
f = open("2019/day2-input.txt")
raw = f.readline()
f.close()
program = [int(x) for x in raw.replace("\n", "").split(",")]

# part 1
cp = IntComputer(program)
cp.run_noun_verb(12, 2)
cp.program[0] # answer

# part 2
cp = IntComputer(program)
res = cp.find_noun_verb(19690720, True)
100 * res[0] + res[1] # answer
