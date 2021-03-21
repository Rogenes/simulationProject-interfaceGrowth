# Rugosity => for each t, create a new point (x,y) = (t, rugosity(t))
import numpy as np
from randomNumberGenerator import RandomNumberGenerator
from rugosity import getRugosity
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit
import time as clockTime

start = clockTime.time()
print("START")

substracts = {
    'l200': np.zeros(dtype=int, shape=200),
    'l400': np.zeros(dtype=int, shape=400),
    'l500': np.zeros(dtype=int, shape=500),
    'l800': np.zeros(dtype=int, shape=800),
    'l1600': np.zeros(dtype=int, shape=1600)
}

sample = 0
sampleMax = 1

t = 0
tMax = 10**4

currentSubstractName = 'l500'
currentSubstract = substracts[currentSubstractName]
currentSubstractLenght = len(currentSubstract)

rng = RandomNumberGenerator(l=currentSubstractLenght)

sampleSubstract = np.zeros(dtype=int, shape=currentSubstractLenght)
sampleRugosity = np.zeros(tMax)
finalRugosity = np.zeros(tMax)

for sample in range(sampleMax):
    for t in range(tMax):
        for depositionNumber in range(currentSubstractLenght):
            depositionPosition = rng.getRandomNumber()
            sampleSubstract[depositionPosition] += 1
    
        sampleRugosity[t] = getRugosity(sampleSubstract)
    
    finalRugosity = np.add(finalRugosity, sampleRugosity)
     
    sampleSubstract = np.zeros(dtype=int, shape=currentSubstractLenght)
    sampleRugosity = np.zeros(tMax)

finalRugosity /= sampleMax
time = np.arange(0, tMax)

log10FinalRugosity = np.log10(finalRugosity)
log10time = np.log10(np.append(np.arange(1, tMax),tMax))


fit = np.polyfit(time, finalRugosity, 1)
print(fit)

end = clockTime.time()
print(f'END: {end - start}')

plt.plot(time, finalRugosity, 'o', markersize=2, label='real')
plt.plot(np.unique(time), np.poly1d(np.polyfit(time, finalRugosity, 1))(np.unique(time)), 
         label='numpy.polyfit')
plt.ylabel(f'Rugosity')
# plt.xscale('log')
# plt.yscale('log')
plt.show()
