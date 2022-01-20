import random

moves = ["rock", "paper", "scissors"]

class Move:
    rock = False
    paper = False
    scissors = False

    def __init__(self, val: str):
        if val == "rock":
            self.rock = True
        elif val == "paper":
            self.paper = True
        elif val == "scissors":
            self.scissors = True
        else:
            raise ValueError("value is not supported")

    def beats(self, other):
        if (self.rock and other.scissors) or (self.paper and other.rock) or (self.scissors and other.paper):
            return True
        else:
            return False
    
    def __str__(self) -> str:
        if self.rock:
            return "rock"
        elif self.paper:
            return "paper"
        elif self.scissors:
            return "scissors"
        else:
            return None

def get_move():
    move = input("Input your move (rock, paper, scissors): ").lower()
    if not move in moves:
        raise ValueError("move is not rock or paper or scissors")
    return Move(move)

def lwins(left: Move, right: Move) -> bool:
    if left.beats(right):
        return True
    else:
        return False

def draw(left: Move, right: Move) -> bool:
    return str(left) == str(right)

def main():
    playing = True
    while playing:
        move = get_move()
        c_move = random.choice(moves)
        if lwins(move, Move(c_move)):
            print(f"player wins! ({move} beats {c_move})")
        elif draw(move, c_move):
            print(f"its a draw! (both had {move})")
        else:
            print(f"computer wins! ({c_move} beats {move})")
        again = input("play again? (Y/n) ").lower()
        if again == "n":
            playing = False


if __name__ == "__main__":
    main()
