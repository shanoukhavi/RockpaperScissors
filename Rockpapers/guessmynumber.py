import sys
import random
import argparse
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def rps(name="PlayerOne"):
    game_count = 0
    player_wins = 0

    def play_rps():
        nonlocal player_wins, game_count

        player_choice = input(f"\n{name}, guess which number I'm thinking about (1=Rock, 2=Paper, 3=Scissors):\n\n")
        if player_choice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()

        player = int(player_choice)
        computer = random.randint(1, 3)

        print(f"\n{name}, you chose {RPS(player).name}.")
        print(f"Python chose {RPS(computer).name}.")

        if player == computer:
            player_wins += 1
            win_message = f"🥳 {name} wins! Your winning percentage is 100.00%."
        elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
            win_message = f"Sorry {name}, better luck next time. Your winning percentage is 33.33%."
        else:
            win_message = f"Sorry {name}, better luck next time. Your winning percentage is 50%."

        print(win_message)
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")

        while True:
            play_again = input(f"\n{name}, play again? (Y for yes or Q to quit):\n")
            if play_again.lower() not in ["y", "q"]:
                continue
            if play_again.lower() == "y":
                return play_rps()
            else:
                print("\nBetter luck next time!")
                sys.exit(f"Bye {name}!")

    return play_rps

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Provides a personalized game experience.")
    parser.add_argument("-n", "--name", metavar="name", required=True, help="The name of the person playing the game.")
    args = parser.parse_args()
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()


