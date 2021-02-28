import random

GREATEST_INT = 2**31
LOWEST_INT = -GREATEST_INT

class RandomNumberGenerator:
    l = 200
    # Still needs to create a "real" random number generator. Super usefull... 

    def __init__(self, l=200):
        self.l = l

    def getRandomNumber(self):
        x0 = random.randint(LOWEST_INT, GREATEST_INT-1)
        # we do not need abs value, since random.sample always use positive values
        x1 = abs(x0)
        x2 = x0*((self.l-1)/GREATEST_INT)
        # if we execute step (iv) from dissertation we would never had a x3 = 0 and would have a x3 = l.
        # This causes out of bounds error, since array position goes from 0 to l-1.
        x3 = round(x2)
        return x3