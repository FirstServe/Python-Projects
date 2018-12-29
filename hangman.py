import math, random

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
