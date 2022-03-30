import random

def foo(x,y,z):
    return 6*x**3 + 9*y**2 + 90*z -25


def fitness(x,y,z):
    ans = foo(x,y,z)

    if (ans == 0):
        return 99999
    
    else:
        return abs(1/ans)

solutions = []

for s in range(1000):
    solutions.append( 
        (random.uniform(0, 10000), 
        random.uniform(0, 10000), 
        random.uniform(0, 10000)) 
    )


for i in range(10000):
    rankedSolutions = [];
    for s in solutions:
        rankedSolutions.append( (fitness(s[0], s[1], s[2]), s) )
    
    rankedSolutions.sort()
    rankedSolutions.reverse()
    print(f"=== Gen {i} best solutions ===")

    if rankedSolutions[0][0] > 999:
        break
    print(rankedSolutions[0])

    bestSolutions = rankedSolutions[:100]
    elements = []
    for s in bestSolutions:
        elements.append( s[1][0])
        elements.append( s[1][1])
        elements.append( s[1][2])

    newGeneration = [];
    for _ in range(1000):
        e1 = random.choice(elements) * random.uniform(0.99, 1.01)
        e2 = random.choice(elements) * random.uniform(0.99, 1.01)
        e3 = random.choice(elements) * random.uniform(0.99, 1.01)

        newGeneration.append( (e1, e2, e3) )

        solutions = newGeneration