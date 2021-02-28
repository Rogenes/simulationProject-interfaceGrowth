import numpy as np
import random

def getRandomNumber(l):
    greatestInt = 2**31
    lowestInt = -greatestInt

    x0 = random.randint(lowestInt, greatestInt-1)
    x1 = abs(x0)
    x2 = x1*(l-1)/greatestInt
    # if we execute step (iv) from dissertation we would never had a x3 = 0 and would have a x3 = l.
    # This causes out of bounds error, since array position goes from 0 to l-1.
    x3 = round(x2)
    return x3