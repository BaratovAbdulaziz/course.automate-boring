from random import randint

target_number = randint(1, 31)
print("The number is between 1 and 31")

for attempt in range(7):
    guess = int(input("What number are you going to check?: "))

    if guess == target_number:
        print(f"{guess} is the correct answer 🎉")
        break  # stop the game if correct
    elif guess > target_number:
        print(f"{guess} is too high, please try again.")
    elif guess < target_number:
        print(f"{guess} is too low, please try again.")

    # if it's the last guess and still wrong
    if attempt == 6:
        print(f"😢 You've used all your chances. The correct number was: {target_number}")
