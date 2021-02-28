# Rugosity => for each t, create a new point (x,y) = (t, rugosity(t))
import numpy as np
from randomNumberGenerator import RandomNumberGenerator
from rugosity import getRugosity
import matplotlib.pyplot as plt

t = 0
tMax = 10**3

lValues = [200,400,800,1600]

l200 = np.zeros(dtype=int, shape=200)
l400 = np.zeros(dtype=int, shape=400)
l800 = np.zeros(dtype=int, shape=800)
l1600 = np.zeros(dtype=int, shape=1600)

##########################
##### for tests only #####
##########################
lCurrent = 200
rng = RandomNumberGenerator(l=lCurrent)
sample200 = [] 
# single sample
while t < tMax:
    for depositionNumber in range(lCurrent):
        depositionPosition = rng.getRandomNumber()
        l200[depositionPosition] += 1
    sample200.append((t,getRugosity(l200))) 
    t+=1

# plt.bar(np.arange(0,200), l200)
# plt.ylabel(f'substrate - 1 sample')
# plt.show()

divided = list(zip(*sample200)) 
plt.plot(divided[0], divided[1])
plt.ylabel(f'Rugosity 200 - 1 sample')
plt.show()