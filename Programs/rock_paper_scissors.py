import sys
from random import randint

def play_rock_paper_scissors():
    user_choice = input("Enter R, P, or S: ").upper()
    computer_number = randint(1, 3)
    computer_choice = "R" if computer_number == 1 else "P" if computer_number == 2 else "S"

    if user_choice not in ("R", "P", "S"):
        print("Invalid input!")
    elif user_choice == computer_choice:
        print("DRAW")
    elif (user_choice == "R" and computer_choice == "S") or \
         (user_choice == "P" and computer_choice == "R") or \
         (user_choice == "S" and computer_choice == "P"):
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        play_rock_paper_scissors()
    elif play_again == "n":
        sys.exit()
    else:
        print("Invalid response. Exiting.")
        sys.exit()

play_rock_paper_scissors()
