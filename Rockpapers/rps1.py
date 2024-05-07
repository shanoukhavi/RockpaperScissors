import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True


while playagain:
    playerchoice = input("\nenter...\n1 for rock,\n2 for paper,\n3 for scissors:\n\n")
    player = int(playerchoice)
    if player < 1 or player > 3:
        sys.exit("you must enter 1 , 2  ,3")

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("your chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Python choise " + str(RPS(computer)).replace("RPS.", "") + ".")

    if player == 1 and computer == 3:
        print("🥳User win")
    elif player == 2 and computer == 1:
        print("🥳User win")
    elif player == 3 and computer == 2:
        print("🥳User win")

    elif player == computer:
        print("😒this  game got tied my friend")
    else:
        print("🐍computer wins")
    playagain = input("\n Play Again? \n Y for yes or \n Q to quit \n\n")
    if playagain.lower() == "y":
        continue #its like contininug ur game if u click the yes for it
    else:
        print("\n")
        print("Thank you for playing\n")
        playagain = False
        # break
sys.exit("bye game is over done tata")
