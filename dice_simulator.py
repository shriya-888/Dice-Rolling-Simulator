# 🎲 2. Dice Rolling Simulator
# Concept: Simulate rolling one or more dice.

# Use random.randint(1, 6) for each die.

# Add ASCII art or a GUI (like Tkinter) for enhancement.


import random
value= random.randint(0,6)
attempts=0

for i in range(attempts,3,1):
    guess=int(input("Guess a number between 0 to 6: "))
    attempts+=1
    if guess>value:
            print("too high")
    elif guess<value:
             print("too low")
    else :
             print("conratulations ")