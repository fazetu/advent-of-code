# type: ignore
class IntComputer:
    def __init__(self, program, pointer = 0):
        self.pointer = pointer
        self.program = program
        self.orig_pointer = pointer
        self.orig_program = program.copy()

    def run_noun_verb(self, noun, verb):
        prog = self.program.copy()
        prog[1] = noun
        prog[2] = verb
        self.program = prog
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

    def show(self):
        print(self.program)

    def reset(self):
        self.pointer = self.orig_pointer
        self.program = self.orig_program.copy()

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

    def op3(self, input):
        if self.get_current() != 3:
            return None
        j = self.get(self.pointer + 1)
        self.program[j] = input
        self.pointer += 2

    def op4(self):
        if self.get_current() != 4:
            return None
        j = self.get(self.pointer + 1)
        self.pointer += 2
        return self.program[j]
        
    def op(self, op_code, input):
        if op_code == 1:
            self.op1()
        elif op_code == 2:
            self.op2()
        elif op_code == 3:
            self.op3(input)
        elif op_code == 4:
            self.op4()

    def run(self, input):
        op_code = self.get_current()
        while op_code != 99:
            if op_code == 4:
                return self.op4()
            else:
                self.op(op_code, input)
            op_code = self.get_current()
