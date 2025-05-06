import sys
from random import randint
def RPS():
    user = input("R/P/S")
    Computer = randint(1,3)
    # 1 = R 2 = P 3 = S
    # Draw conditions
    if user =="R" and Computer == "1":
        print('DRAW')
    elif user =="P" and Computer == 2:
        print("DRAW")
    elif user == "S" and Computer == 3:
        print("DRAW")
    elif user == "R":
        if Computer == 3:
            print("You win!")
        else:
            print("You lose!")
    elif user == "P":
        if Computer == 1:
            print("You win!")
        else:
            print("You lose!")
    elif user == "S":
        if Computer == 2:
            print("You win!")
        else:
            print("You lose!")
    else:
        print("Invalid input!")
    status = input("are you going to play again?(y/n)")
    if status == "y":
        RPS()
    elif status == "n":
        sys.exit()
    else:
        print("???")
        sys.exit()
RPS()