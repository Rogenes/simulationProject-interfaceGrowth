# Rugosity => for each t, create a new point (x,y) = (t, rugosity(t))
import numpy as np
from rugosity import getRugosity
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import time as clockTime
import random
from numba import jit, int32
import math
import csv

@jit(nopython=True)
def runSamples(sampleMax, tMax):
    lengths = [200, 400, 800, 1600] 
        
    sampleRugosity = np.zeros(tMax)
    finalRugosity = np.zeros(tMax)
    
    snapshotQuantity = 10
    newFinalSnapshots = {
        200: np.zeros(shape=(snapshotQuantity, 200)),
        400: np.zeros(shape=(snapshotQuantity, 400)),
        800: np.zeros(shape=(snapshotQuantity, 800)),
        1600: np.zeros(shape=(snapshotQuantity, 1600)),
    }

    newFinalRugosity = {
        200: np.zeros(tMax),
        400: np.zeros(tMax),
        800: np.zeros(tMax),
        1600: np.zeros(tMax),
    }


    for substractLength in lengths:
    
        snapshotPosition = 0
        currentSubstractLenght = substractLength
        substractLengthMinusOne = currentSubstractLenght - 1
        sampleSubstract = np.zeros(dtype=int32, shape=currentSubstractLenght)

        for sample in range(sampleMax):
            for t in range(tMax):
                for depositionQuantity in range(currentSubstractLenght):

                    depositionPosition = random.randint(0, currentSubstractLenght)
                    sampleSubstract[depositionPosition] += 1
            
                sampleRugosity[t] = getRugosity(sampleSubstract)
                
                if sample == 0 and t%(25) == 0  and snapshotPosition < snapshotQuantity:
                    newFinalSnapshots[currentSubstractLenght][snapshotPosition] = sampleSubstract 
                    snapshotPosition += 1

            currentRugosity = newFinalRugosity[currentSubstractLenght]
            newFinalRugosity[currentSubstractLenght] = np.add(currentRugosity, sampleRugosity)
            
            sampleSubstract.fill(0)
            sampleRugosity.fill(0)
        
    return newFinalRugosity, newFinalSnapshots

#|||||||||||||||||||||||||||||||||||
#|||||||||||||| START |||||||||||||| 
#|||||||||||||||||||||||||||||||||||

start = clockTime.time()
print("START")

lengths = [200, 400, 800, 1600]
substracts = {
    'l200': np.zeros(dtype=int, shape=200),
    'l400': np.zeros(dtype=int, shape=400),
    'l800': np.zeros(dtype=int, shape=800),
    'l1600': np.zeros(dtype=int, shape=1600)
}

# Config params
sample = 0
sampleMax = 10**2
t = 0
tMax = 10**4

#  running samples 
finalRugosity, finalSnapshot = runSamples(sampleMax=sampleMax, tMax=tMax)

time = np.arange(0, tMax, 1)

for index, substractLength in enumerate(finalRugosity):    
    finalRugosity[substractLength] = finalRugosity[substractLength]/sampleMax
    
end = clockTime.time()
print(f'END: {end - start}')

for substractLength in finalRugosity:
    rugosityArray = finalRugosity[substractLength]
    with open(f'data/DA/DA{substractLength}.csv', mode='w') as myCsv:
        for rugosityTime, rugosity in  enumerate(rugosityArray):
            file = csv.writer(myCsv, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            file.writerow([rugosityTime, rugosity])
    
# PLOT SNAPSHOT
# fig, axes = plt.subplots(2, 2)
# indexes = {
#     0: (0,0),
#     1: (0,1),
#     2: (1,0),
#     3: (1,1),
# }
# for index, substractLength in enumerate(finalSnapshot):
#     xAxis = np.arange(0, substractLength, 1)
#     substractSnapshots = np.flip(finalSnapshot[substractLength])
    
#     for snapshotInstance in substractSnapshots:
#         axes[indexes[index]].plot(xAxis, snapshotInstance)
#         axes[indexes[index]].fill_between(xAxis, snapshotInstance)
#     axes[indexes[index]].set_title(f'substract {substractLength}')

# PLOT CURVE
for substractLength in finalRugosity:
    plt.plot(time, finalRugosity[substractLength], label=f'substract {substractLength}')
    plt.legend()
plt.title('DA')
plt.xscale('log')
plt.yscale('log')

plt.show()





                