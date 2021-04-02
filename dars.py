# Rugosity => for each t, create a new point (x,y) = (t, rugosity(t))
import numpy as np
from rugosity import getRugosity
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import time as clockTime
import random
from numba import jit, int32

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
                    # depositionPosition = rng.getRandomNumber()
                    depositionPosition = random.randint(0, currentSubstractLenght)
                    
                    current = depositionPosition
                    lower = (depositionPosition - 1) if (depositionPosition > 0) else 0
                    upper = (depositionPosition + 1) if (depositionPosition < substractLengthMinusOne) else (substractLengthMinusOne)

                    finalPosition = current

                    if sampleSubstract[lower] < sampleSubstract[current] and sampleSubstract[lower] < sampleSubstract[upper]:
                        finalPosition = lower
                    elif sampleSubstract[upper] < sampleSubstract[current] and sampleSubstract[upper] < sampleSubstract[lower]:
                        finalPosition = upper
                    else:
                        finalPosition = current

                    sampleSubstract[finalPosition] += 1

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

substracts = {
    'l200': np.zeros(dtype=int, shape=200),
    'l400': np.zeros(dtype=int, shape=400),
    'l800': np.zeros(dtype=int, shape=800),
    'l1600': np.zeros(dtype=int, shape=1600)
}

# Config params
sample = 0
sampleMax = 10**1
t = 0
tMax = 10**4
# currentSubstractName = 'l1600'
#  end of config params

# currentSubstract = substracts[currentSubstractName]
# currentSubstractLenght = len(currentSubstract)

#  running samples 
finalRugosity, finalSnapshot = runSamples(sampleMax=sampleMax, tMax=tMax)

time = np.arange(0, tMax, 1)
# time = {
#     200: np.arange(0, tMax, 1),
#     400: np.arange(0, tMax, 1),
#     800: np.arange(0, tMax, 1),
#     1600: np.arange(0, tMax, 1),
# }

for substractLength in finalRugosity:
    finalRugosity[substractLength] /= sampleMax
    # finalRugosity[substractLength] /= (substractLength**0.5)    
    # time[substractLength] = time[substractLength]/(substractLength**2)

# polyfit to find coefficients
# fit = np.polyfit(time, finalRugosity, 1)
# print(fit)

end = clockTime.time()
print(f'END: {end - start}')

# fig, (ax1, ax2) = plt.subplots(1, 2)
# fig.suptitle(f'Snapshot and Rugosity by time')

# xAxis = np.arange(0, currentSubstractLenght, 1)
# for index, plot in enumerate(reversed(finalSnapshot)):
#     ax1.plot(xAxis, plot, label=f'{index}')
#     ax1.fill_between(xAxis, plot)

for substractLength in finalRugosity:
    plt.plot(time, finalRugosity[substractLength], label=f'substract {substractLength}')
    plt.legend()
# plt.plot(np.unique(time), np.poly1d(fit)(np.unique(time)), label='polyfit')
# plt.xscale('log')
# plt.yscale('log')
plt.show()
