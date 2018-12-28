import math, random

def generate_number():
    '''Generates a random positive integer from 1 to 1000.'''
    num = random.randint(1, 1000)
    return num


def guess_number(num):
    '''Allows the user to guess the generated number.'''
    guess = int(input("What is your guess?"))
    while guess != num:
        if guess > num:
            print("Your guess was larger than my number. Please guess again.")
        elif guess < num:
            print("Your guess was smaller than my number. Please guess again.")
        else:
            print("An error occurred while evaluating your guess. Please try again.")
        guess = int(input("What is your guess?"))

def check_input():
    return


num = generate_number
print(num)
