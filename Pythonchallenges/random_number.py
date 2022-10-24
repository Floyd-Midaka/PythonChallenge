'''Challenge
Randomness
Define a function, random_number, that takes no parameters. 
The function must generate a random integer between 1 and 100, both inclusive, and return it.'''

from random import randint

def random_number():
    seed = randint(1,50)
    multiplier = randint(1,2)
    return seed*multiplier
print(random_number())