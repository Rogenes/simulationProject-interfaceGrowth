# Rugosity => for each t, create a new point (x,y) = (t, rugosity(t))
import numpy as np
from randomNumberGenerator import RandomNumberGenerator
from rugosity import getRugosity
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import time as clockTime
import random
from numba import jit, int32

@jit(nopython=True)
def runSamples(sampleMax, tMax, currentSubstractLenght):
    sampleSubstract = np.zeros(dtype=int32, shape=currentSubstractLenght)
    sampleRugosity = np.zeros(tMax)
    finalRugosity = np.zeros(tMax)
    rng = RandomNumberGenerator(currentSubstractLenght)

    snapshotQuantity = 10
    finalSnapshot = np.zeros(shape=(snapshotQuantity,currentSubstractLenght))

    snapshotPosition = 0

    substractLengthMinusOne = currentSubstractLenght - 1
    
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
                finalSnapshot[snapshotPosition] = sampleSubstract
                snapshotPosition += 1

        finalRugosity = np.add(finalRugosity, sampleRugosity)
        sampleSubstract.fill(0)
        sampleRugosity.fill(0)
    
    return finalRugosity, finalSnapshot

#|||||||||||||||||||||||||||||||||||
#|||||||||||||| START |||||||||||||| 
#|||||||||||||||||||||||||||||||||||

start = clockTime.time()
print("START")

substracts = {
    'l200': np.zeros(dtype=int, shape=200),
    'l400': np.zeros(dtype=int, shape=400),
    'l500': np.zeros(dtype=int, shape=500),
    'l800': np.zeros(dtype=int, shape=800),
    'l1600': np.zeros(dtype=int, shape=1600)
}

# Config params
sample = 0
sampleMax = 10**2
t = 0
tMax = 10**4
currentSubstractName = 'l200'
#  end of config params

currentSubstract = substracts[currentSubstractName]
currentSubstractLenght = len(currentSubstract)

#  running samples 
finalRugosity, finalSnapshot = runSamples(sampleMax=sampleMax, tMax=tMax, currentSubstractLenght=currentSubstractLenght)

finalRugosity /= sampleMax
time = np.arange(0, tMax, 1)

# polyfit to find coefficients
fit = np.polyfit(time, finalRugosity, 1)
print(fit)

end = clockTime.time()
print(f'END: {end - start}')

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle(f'Snapshot and Rugosity by time')

xAxis = np.arange(0, currentSubstractLenght, 1)
for index, plot in enumerate(reversed(finalSnapshot)):
    ax1.plot(xAxis, plot, 'o', label=f'{index}')
    # ax1.fill_between(xAxis, plot)


ax2.plot(time, finalRugosity, label='real')
# plt.plot(np.unique(time), np.poly1d(fit)(np.unique(time)), label='polyfit')
# plt.xscale('log')
# plt.yscale('log')
plt.show()
