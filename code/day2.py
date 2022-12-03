from utils import read_input

# for both parts
opponent_key = {"A": "Rock", "B": "Paper", "C": "Scissors"}
outcome_score = {"Lose": 0, "Draw": 3, "Win": 6}
shape_score = {"Rock": 1, "Paper": 2, "Scissors": 3}

# input = ["A Y", "B X", "C Z"]
input = read_input(2)

# part 1
your_key = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}


def outcome_of_round(opponent: str, you: str) -> str:
    opponent_shape = opponent_key[opponent]
    your_shape = your_key[you]

    if opponent_shape == your_shape:
        return "Draw"

    if your_shape == "Rock" and opponent_shape == "Scissors":
        return "Win"
    elif your_shape == "Paper" and opponent_shape == "Rock":
        return "Win"
    elif your_shape == "Scissors" and opponent_shape == "Paper":
        return "Win"

    return "Lose"


def round_score1(opponent: str, you: str) -> int:
    your_shape = your_key[you]
    outcome = outcome_of_round(opponent, you)
    return outcome_score[outcome] + shape_score[your_shape]


scores1 = [round_score1(*line.split(" ")) for line in input]

# answer 1
print(sum(scores1))


# part 2
outcome_key = {"X": "Lose", "Y": "Draw", "Z": "Win"}


def your_shape_for_outcome(opponent: str, outcome: str) -> str:
    opponent_shape = opponent_key[opponent]
    outcome_ = outcome_key[outcome]

    if outcome_ == "Draw":
        return opponent_shape

    if outcome_ == "Win":
        if opponent_shape == "Rock":
            return "Paper"
        elif opponent_shape == "Paper":
            return "Scissors"
        else:
            # need to win and opponent picked scissors
            return "Rock"
    else:
        if opponent_shape == "Rock":
            return "Scissors"
        elif opponent_shape == "Paper":
            return "Rock"
        else:
            # need to lose and opponent picked scissors
            return "Paper"


def round_score2(opponent: str, outcome: str) -> int:
    your_shape = your_shape_for_outcome(opponent, outcome)
    outcome_ = outcome_key[outcome]
    return outcome_score[outcome_] + shape_score[your_shape]


scores2 = [round_score2(*line.split(" ")) for line in input]

# answer 2
print(sum(scores2))
