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
