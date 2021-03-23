import numpy as np
import math
from numba import jit

# substrateLength = 200,400,800 or 1600
# substrateSnapshot = an instance of substrate at an especific moment t
# def getMeanHeight(substrateSnapshot):
#     return np.mean(substrateSnapshot)

@jit(nopython=True)
def getRugosity(substrate):
    substrateSnapshot = substrate
    substrateLength = len(substrateSnapshot)
    meanHeight = np.mean(substrateSnapshot)
    quadraticRugosity = np.sum(((substrateSnapshot - meanHeight)**2))/substrateLength
    rugosity = math.sqrt(quadraticRugosity)
    return rugosity