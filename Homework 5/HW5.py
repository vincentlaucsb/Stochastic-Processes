import numpy as np

# ===== Part A =====
def offspring():
    x = np.random.randint(low=0,high=100,size=1)
    if 0 <= x <= 19:
        return 0
    elif 19 < x <= 39:
        return 1
    elif 39 < x <= 89:
        return 2
    else:
        return 3

# ===== Part B =====
current_gen = 1
children = 0
n = 0

while True:
    n += 1

    for k in range(0,current_gen):
        children += offspring()
       
    # Extinction
    if children == 0:
        print("Extinct at {0}th generation".format(n))
        break
        
    # Assumption: Population size diverges to infinity if children > 50
    elif children > 5000:
        print("We have {0} children. Population (currently: {1}) will very likely diverge to infinity.".format(children,current_gen))
        break
    
    # Keep making children
    else:
        current_gen = children
        print("{0}th generation has {1} individuals".format(n,current_gen))
        children = 0
        
# ===== Part C =====

# branch() simulates one population and returns
# * True if the population goes extinct
# * False if the population diverges to infinity
# We run this 10,000 times later
def branch():
    current_gen = 1
    children = 0
    n = 0

    while True:
        n += 1

        for k in range(0,current_gen):
            children += offspring()
           
        # Extinction
        if children == 0:
            extinct = True
            break
            
        # Assumption: Population size diverges to infinity if children > 50
        elif children > 50:
            extinct = False
            break
        
        # Keep making children
        else:
            current_gen = children
            children = 0
            
    return extinct
    
# == Simulate 10,000 branches ==
extinctions = np.array([])
for i in range(0,10000):
    branching_process = branch()
    if i%100 == 0:
        print("We are currently simulating the {0}th branch".format(i))
    
    if branching_process:
        extinctions = np.append(extinctions,1)
    else:
        extinctions = np.append(extinctions,0)

# Probability of extinctions = (# of extinctions)/10000        
print("Probability of extinction: {0}".format(np.sum(extinctions)/10000))