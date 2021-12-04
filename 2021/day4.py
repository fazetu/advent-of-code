from typing import Dict, List
import re

input = [
    "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
    "",
    "22 13 17 11  0",
    " 8  2 23  4 24",
    "21  9 14 16  7",
    " 6 10  3 18  5",
    " 1 12 20 15 19",
    "",
    " 3 15  0  2 22",
    " 9 18 13 17  5",
    "19  8  7 25 23",
    "20 11 10 24  4",
    "14 21 16 12  6",
    "",
    "14 21 17 24  4",
    "10 16 15  9 19",
    "18  8 23 26 20",
    "22 11 13  6  5",
    " 2  0 12  3  7",
]

# with open("day4-input.txt", "r") as f:
#     input = [line.strip() for line in f.readlines()]

# part 1
def parse_input(input: List[str]) -> Dict[str, List]:
    called_numbers = [int(val) for val in input[0].split(",")]
    boards = []
    board = []

    # first line of input is the called numbers, second line is blank
    for line in input[2:]:
        if line == "":
            boards.append(board)
            board = [] # reset since we have reached the end of that board
        else:
            board.append(line)

    # add the last one even if now end line
    boards.append(board)

    return {"called_numbers": called_numbers, "boards": boards}

def parse_board(board: List[str]) -> List[List[int]]:
    return [[int(val) for val in re.split("\\s+", row.strip())] for row in board]

class Bingo:
    def __init__(self, board: List[str]):
        parsed_board = parse_board(board)
        self.board = parsed_board
        self.filled_board = self.make_blank_board(parsed_board)
        self.last_called_number = ""
        self.winning_turn = 0

    @staticmethod
    def make_blank_board(board: List[List[int]]) -> List[List[str]]:
        return [[""] * len(row) for row in board]
    
    def fill_number(self, number: int):
        self.last_called_number = number
        r, c = (0, 0)
        for r, row_list in enumerate(self.board):
            for c, val in enumerate(row_list):
                # if self.filled_board[r][c] == "X":
                #     next
                if val == number:
                    self.filled_board[r][c] = "X"
                    return None
    
    def check_winner(self) -> bool:
        # check row winners
        for row in self.filled_board:
            if all([val == "X" for val in row]):
                return True

        # check column winners
        n_cols = len(self.filled_board[0])
        for c in range(n_cols):
            col_vals = [row[c] for row in self.filled_board]
            if all([val == "X" for val in col_vals]):
                return True

        return False

    def play(self, called_numbers: List[int]):
        for called_number in called_numbers:
            self.winning_turn += 1
            self.fill_number(called_number)
            is_winner = self.check_winner()
            if is_winner:
                return None

    def get_score(self) -> int:
        score = 0

        for r, row_list in enumerate(self.board):
            for c, val in enumerate(row_list):
                if self.filled_board[r][c] == "":
                    # the score is the sum of all unmarked numbers
                    score += val

        return score * self.last_called_number


p = parse_input(input)

bingos = [Bingo(board) for board in p["boards"]]

for bingo in bingos:
    bingo.play(p["called_numbers"])

max([bingo.get_score() for bingo in bingos]) # answer part 1

# part 2
p = parse_input(input)

bingos = [Bingo(board) for board in p["boards"]]

for bingo in bingos:
    bingo.play(p["called_numbers"])

# find highest winning turn
most = 0
for i, bingo in enumerate(bingos):
    if bingo.winning_turn > most:
        j = i
        most = bingo.winning_turn

[bingo.get_score() for bingo in bingos][j]
