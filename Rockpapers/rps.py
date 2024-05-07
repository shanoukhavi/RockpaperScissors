import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def main():
    print("Enter...\n1 for rock,\n2 for paper,\n3 for scissors:")
    player_choice = input()
    
    try:
        player = int(player_choice)
    except ValueError:
        sys.exit("Invalid input. Please enter a number.")
    
    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")
    
    computer_choice = random.choice([1, 2, 3])
    computer = RPS(computer_choice)
    player = RPS(player)

    print(f"\nYou chose {player.name}.")
    print(f"Python chose {computer.name}.\n")

    if (player == RPS.ROCK and computer == RPS.SCISSORS) or \
       (player == RPS.PAPER and computer == RPS.ROCK) or \
       (player == RPS.SCISSORS and computer == RPS.PAPER):
        print("🥳 User wins!")
    elif player == computer:
        print("😒 Tie game, my friend.")
    else:
        print("🐍 Computer wins!")

if __name__ == "__main__":
    main()

