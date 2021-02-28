import numpy as np
import math

# substrateLength = 200,400,800 or 1600
# substrateSnapshot = an instance of substrate at an especific moment t
def getMeanHeight(substrateSnapshot):
    return np.mean(substrateSnapshot)

def getRugosity(substrateSnapshot):
    substrateLength = len(substrateSnapshot)
    meanHeight = getMeanHeight(substrateSnapshot)
    quadraticRugosity = np.sum(((substrateSnapshot - meanHeight)**2))/substrateLength
    rugosity = math.sqrt(quadraticRugosity)
    return rugosity