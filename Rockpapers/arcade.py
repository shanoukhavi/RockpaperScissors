import sys
import argparse
from rps8 import rps
from guessmynumbermodified import guess


def play_game(name="PlayerOne"):
    welcome_back = False

    while True:
        if welcome_back:
            print(f"\n{name}, welcome back to the Arcade menu.")

        player_choice = input(
            '\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press "x" to exit the Arcade\n\n'
        )

        if player_choice not in ["1", "2", "x"]:
            print(f"\n{name}, please enter 1, 2, or 'x'.")
            continue

        if player_choice == "x":
            print(f"\nSee you next time, {name}!\n")
            sys.exit("Bye! 👋")

        game = rps(name) if player_choice == "1" else guess(name)
        game()

        welcome_back = True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Provides a personalized game experience.")
    parser.add_argument("-n", "--name", metavar="name", required=True, help="The name of the person playing the game.")
    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the Arcade! 🤖")
    play_game(args.name)

