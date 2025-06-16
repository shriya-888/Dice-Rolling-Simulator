# 🔢 1. Number Guessing Game
# Concept: The computer randomly selects a number, and the user has to guess it.
# Use random.randint() to generate a number.
# Add hints like “Too high” or “Too low”.
# Optionally, count the number of attempts.

import random

value= random.randint(0,100)
attempts = 0
for i in range (attempts,10,1):
    guess = int(input("Guess a number between 0 and 100:  "))
    attempts += 1
    if guess < value:
        print("Too low")
    elif guess > value:
        print("Too high")
    else:
        print(f"Congratulations! You guessed the number {value} in {attempts} attempts.")
        break

