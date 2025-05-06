from random import randint

secret_number = randint(1, 31)
print("The number is between 1 and 31")

for guesses in range(7):
    user_guess = int(input("What number are you going to check?: "))

    if user_guess == secret_number:
        print(f"{user_guess} is the correct answer 🎉")
        break  # stop the game if correct
    elif user_guess > secret_number:
        print(f"{user_guess} is too high, please try again.")
    elif user_guess < secret_number:
        print(f"{user_guess} is too low, please try again.")

    # if it's the last guess and still wrong
    if guesses == 6:
        print(f"😢 You've used all your chances. The correct number was: {secret_number}")
