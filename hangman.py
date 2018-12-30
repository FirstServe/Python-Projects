import math, random, turtle

def generate_word():
    '''Generates a random word.'''
    wordList = []
    word = wordList[random.randint(0, len(wordList) - 1]
    return word

def number_letters():
    '''Splits the generated word into some number of letters.
    The user will need to guess these letters in the fashion of hangman.'''
    word = generate_word()
    numChar = len(word)
    return numChar

def play_hangman():
    '''Plays a game of hangman with the user.'''
    word = generate_word()
    numChar = number_letters()
    print("_" * numChar)
    wordGuess = input("What is your letter guess? (Please input a lowercase letter)"
    if wordGuess in word:
        print("You guessed a letter.")
        
