# Practice coding
Practice coding
Site: https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

Task 1: Dice Roll Simulator

import math, random

def roll():
    '''Simulates a dice roll, where the user chooses the number of sides on the dice.
    The user can also reroll.'''
    numSides = int(input("Enter the number of sides your dice have:"))
    rollResult1 = random.randint(1, numSides)
    rollResult2 = random.randint(1, numSides)
    print("You rolled a", rollResult1, "and a", rollResult2, ".")
    rollAgain = input("Would you like to roll again?")
    if rollAgain == "Yes" or rollAgain == "yes":
        roll()
    elif rollAgain == "No" or rollAgain == "no":
        print("Goodbye. Have a nice day.")
        return
    else:
        print("An error occured. Please rerun the program.")
        return
                      
    
roll()

Task 2: Number Guesser



Task 3: Madlibs



Task 4: Adventure Game



Task 5: Hangman
