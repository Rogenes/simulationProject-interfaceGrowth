import random
import numpy as np
from numba import int32, jit
from numba.experimental import jitclass

GREATEST_INT = 2**31    
LOWEST_INT = -GREATEST_INT

spec = [("l", int32),("x", int32),]

@jitclass(spec)
class RandomNumberGenerator:
    def __init__(self, l=200):
        self.l = l
        self.x = 2222

    @staticmethod
    def lgc(seed):
        M = GREATEST_INT
        A = 843314861
        B = 453816693
        return  (A * seed + B) % M
    
    def getRandomNumber(self):
        # x0 = random.randint(LOWEST_INT, GREATEST_INT-1)
        x0 = self.lgc(seed=self.x)
        self.x = x0
        x1 = abs(x0)
        x2 = x0*((self.l-1)/GREATEST_INT)
        # if we execute step (iv) from dissertation we would never had a x3 = 0 and would have a x3 = l.
        # This causes out of bounds error, since array position goes from 0 to l-1.
        x3 = round(x2)
        return x3