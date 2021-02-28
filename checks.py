from randomNumberGenerator import RandomNumberGenerator
import numpy as np
import matplotlib.pyplot as plt

# checking bounds
# outOfBounds = 0
# while outOfBounds == 0:
#     rand = getRandomNumber(l=200) 
#     print(rand)
#     if rand >= 200:
#         outOfBounds = 1
#     if rand < 0:
#         outOfBounds = 1

def checkRandomHistory():
    l=200

    # In case we need to create a new seed,
    #   we just have to instanciate a new RandomNumberGenerator object 
    rng = RandomNumberGenerator(l=l)

    coordinates = np.arange(0, 200)

    randomNumberHistory = np.zeros(dtype=int, shape=200)
    iterations = 10000

    # checking distribution
    iterationsConcluded = 0
    while iterationsConcluded < iterations:
        rand = rng.getRandomNumber()
        randomNumberHistory[rand] += 1
        iterationsConcluded += 1

    plt.bar(coordinates, randomNumberHistory)
    plt.ylabel(f'random generator behavior - {iterations} iterations')
    plt.show()

if __name__ == '__main__':
    checkRandomHistory()