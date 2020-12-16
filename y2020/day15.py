# input = [0, 3, 6]
input = [17, 1, 3, 16, 19, 0]

class Game:
    def __init__(self, start):
         # last number said
        self.turn = len(start)
        self.last = start[self.turn - 1]
        self.said_history = {num: [i + 1] for i, num in enumerate(start)}

    def next_number(self):
        self.turn += 1
        x = self.said_history.get(self.last, None)

        if len(x) == 1:
            # it was the first time the number was said
            self.last = 0
        elif len(x) >= 2:
            # number has been said before
            self.last = x[len(x) - 1] - x[len(x) - 2]

        # update history of numbers said
        if not self.last in self.said_history.keys():
            self.said_history[self.last] = [self.turn]
        else:
            self.said_history[self.last].append(self.turn)

    def find_number_on_turn(self, turn):
        for key, val in self.said_history.items():
            if turn in val:
                return key

# part 1
n = 2_020
game = Game(input)
for i in range(n - len(input)):
    game.next_number()
game.find_number_on_turn(n)

# part 2
n = 30_000_000
game = Game(input)
for i in range(n - len(input)):
    game.next_number()
game.find_number_on_turn(n)
