from random import *

def coinflip():
    '''Flips a coin'''
    x = random()
    if (x < 0.5):
        return 'H'
    else:
        return 'T'
    
sequence = ''
for i in range(100):
    sequence += coinflip()

print(sequence)
