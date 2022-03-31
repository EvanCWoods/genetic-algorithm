import random
import matplotlib.pyplot as plt
import numpy as np


end = []
# This function defines the test that is run every iteration of the algorithm to test fitness
def objective(x,y,z):
    return 6*x**3 + 9*y**2 + 90*z -25   # The goal is to get the output of this as close to 0 as possible


# This function tests the actual fitness of the generation
def fitness(x,y,z):
    ans = objective(x,y,z)

    if (ans == 0):
        return 99999
    
    else:
        return abs(1/ans)

solutions = []
# Start the process with some random numbers
for s in range(1000):
    solutions.append( 
        (random.uniform(0, 10000), 
        random.uniform(0, 10000), 
        random.uniform(0, 10000)) 
    )

# Rank the solutions and run the process until the objective function is met
for i in range(1000):
    rankedSolutions = [];
    for s in solutions:
        rankedSolutions.append( (fitness(s[0], s[1], s[2]), s) )
    
    rankedSolutions.sort()
    rankedSolutions.reverse()
    print(f"=== Gen {i} best solutions ===")

    if rankedSolutions[0][0] > 999:
        print(objective( rankedSolutions[0][1][0], rankedSolutions[0][1][1], rankedSolutions[0][1][2] ))
        break
    print(rankedSolutions[0])
    end.append(objective( rankedSolutions[0][1][0], rankedSolutions[0][1][1], rankedSolutions[0][1][2] ))

    bestSolutions = rankedSolutions[:100]
    elements = []
    for s in bestSolutions:
        elements.append( s[1][0])
        elements.append( s[1][1])
        elements.append( s[1][2])

    newGeneration = [];
    for _ in range(1000):
        e1 = random.choice(elements) * random.uniform(0.995, 1.05) # Mutation within 0.5% of the actual number
        e2 = random.choice(elements) * random.uniform(0.995, 1.05) # Mutation within 0.5% of the actual number
        e3 = random.choice(elements) * random.uniform(0.995, 1.05) # Mutation within 0.5% of the actual number

        newGeneration.append( (e1, e2, e3) )

        solutions = newGeneration

plt.figure(figsize=(10,6))
plt.plot(np.arange(0, len(end)), end)
plt.show()