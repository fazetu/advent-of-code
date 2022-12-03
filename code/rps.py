
class RPS:
    shapes = ["Rock", "Paper", "Scissors"]
    outcomes = ["Win", "Lose", "Draw"]

    def validate_shape(self, shape: str):
        if shape not in self.shapes:
            raise ValueError(f"Got {shape}, must be one of {', '.join(self.shapes)}")

    def validate_outcome(self, outcome: str):
        if outcome not in self.outcomes:
            raise ValueError(f"Got {outcome}, must be one of {', '.join(self.outcomes)}")

    def shape_i(self, shape: str) -> int:
        self.validate_shape(shape)

        for i, s in enumerate(self.shapes):
            if shape == s:
                return i

    def shape_wins(self, shape: str) -> str:
        """Get what shape the input shape wins to"""
        i = self.shape_i(shape)
        return self.shapes[(i - 1) % 3]

    def shape_loses(self, shape: str) -> str:
        """Get what shape the input shape loses to"""
        self.validate_shape(shape)
        i = self.shape_i(shape)
        return self.shapes[(i + 1) % 3]

    def play(self, your_shape: str, opponent_shape: str) -> str:
        """From your perspective do you win, lose, or draw the game"""
        self.validate_shape(your_shape)
        self.validate_shape(opponent_shape)

        if your_shape == opponent_shape:
            return self.outcomes[2]
        elif self.shape_wins(your_shape) == opponent_shape:
            return self.outcomes[0]
        else:
            return self.outcomes[1]

    def shape_for_outcome(self, shape: str, outcome: str) -> str:
        """Given your opponent's shape and an outcome, what you play for that outcome"""
        self.validate_shape(shape)
        self.validate_outcome(outcome)

        if outcome == self.outcomes[2]:
            return shape
        elif outcome == self.outcomes[0]:
            return self.shape_loses(shape)
        else:
            return self.shape_wins(shape)


if __name__ == "__main__":
    rps = RPS()
    
    assert rps.shape_wins("Rock") == "Scissors"
    assert rps.shape_wins("Paper") == "Rock"
    assert rps.shape_wins("Scissors") == "Paper"

    assert rps.shape_loses("Rock") == "Paper"
    assert rps.shape_loses("Paper") == "Scissors"
    assert rps.shape_loses("Scissors") == "Rock"

    assert rps.play("Rock", "Rock") == "Draw"
    assert rps.play("Rock", "Scissors") == "Win"
    assert rps.play("Rock", "Paper") == "Lose"

    assert rps.play("Paper", "Rock") == "Win"
    assert rps.play("Paper", "Paper") == "Draw"
    assert rps.play("Paper", "Scissors") == "Lose"

    assert rps.play("Scissors", "Rock") == "Lose"
    assert rps.play("Scissors", "Paper") == "Win"
    assert rps.play("Scissors", "Scissors") == "Draw"

    assert rps.shape_for_outcome("Rock", "Win") == "Paper"
    assert rps.shape_for_outcome("Rock", "Lose") == "Scissors"
    assert rps.shape_for_outcome("Rock", "Draw") == "Rock"

    assert rps.shape_for_outcome("Paper", "Win") == "Scissors"
    assert rps.shape_for_outcome("Paper", "Lose") == "Rock"
    assert rps.shape_for_outcome("Paper", "Draw") == "Paper"

    assert rps.shape_for_outcome("Scissors", "Win") == "Rock"
    assert rps.shape_for_outcome("Scissors", "Lose") == "Paper"
    assert rps.shape_for_outcome("Scissors", "Draw") == "Scissors"
