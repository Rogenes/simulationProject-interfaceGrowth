import random

GREATEST_INT = 2**31

class RandomNumberGenerator:
    randomNumberList = []
    randomNumberListCurrentIndex = -1
    l = 200

    def __init__(self, l=200):
        # generates a 10^7 position list with random numbers.
        # more than suficient for 10^4 iterations.
        # Do not increase this number. May not have enought RAM.
        self.randomNumberList = random.sample(range(GREATEST_INT), 10**7) 
        self.l = l

    def getRandomNumber(self):
        self.randomNumberListCurrentIndex += 1
        x0 = self.randomNumberList[self.randomNumberListCurrentIndex]
        # we do not need abs value, since random.sample always use positive values
        # x1 = abs(x0)
        x2 = x0*((self.l-1)/GREATEST_INT)
        # if we execute step (iv) from dissertation we would never had a x3 = 0 and would have a x3 = l.
        # This causes out of bounds error, since array position goes from 0 to l-1.
        x3 = round(x2)
        return x3