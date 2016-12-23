# Hey Mark, use Python 3 

import matplotlib.pyplot as plt
import numpy as np
from collections import deque

# Let every song correspond to a number between 1 and 5
def shuffle():
    '''
    Note: lower bound is inclusive, upper bound is exclusive, so high = 6 means
    at most we get 5. That's the way numpy is, I don't know why they designed it that way
    '''
    return np.random.randint(low=1, high=6, size=1)[0]
    
def sample_path():
    already_heard = set() # Empty set
    X_n = np.array([0]) # X_0 = 0
    
    # Stop growing path once each song has been played
    while len(already_heard) < 5:
        # Python sets only have unique elements, just like the ones in math 
        already_heard.add(shuffle())
        
        # On each step add the number of songs we already heard to X_n
        X_n = np.append(X_n,len(already_heard))

    return X_n
    
# 10a. Simulate one path
first_path = sample_path()

## 10b/c. Simulate 10000 paths and estimate probabilities of 
over_nine_thousand = deque()

# For 10c. Example: X[5] will have the values of X_5 from all of our 10000 sample paths 
X = {}
N_0 = range(5,21)
tau = {} # For 10e
k = range(1,6) # For 10e

# Initalize
for n in N_0: # Loop over 5, ..., 19
    X[n] = np.array([])

for j in k:
    tau[j] = np.array([])
    
# Generate 10,000 sample paths
for n in range(0,10000):
    current_path = sample_path()
    over_nine_thousand.append(current_path)
    
    # For 10c
    for m in N_0:
        if m + 1 > len(current_path): 
            current_value = 5
        else:
            current_value = current_path[m]
        
        X[m] = np.append(X[m],current_value)
    
    # For 10e
    for j in k:
        first_occur = np.where(current_path==j)[0][0]
        tau[j] = np.append(tau[j],first_occur)
        
# 10c.
probs = {}
for n in N_0:
    # Explanation of formula: X[n] == 5 returns number of values equal to 5
    # np.sum() counts the numbers of Trues. Then we divide by the size of the list.
    probs[n] = np.sum(X[n] == 5)/len(X[n])
    
print("Probability that X_n = 5",probs,sep="\n")
                             
# 10e. Calculate expectations of tau_k for k = 1,..., 5
# e.g. tau_3 = minimum number of steps (n) until X_n = 3

mean_tau = {}
for j in k:
    mean_tau[j] = np.mean(tau[j])
    
print("","Values of tau_k",mean_tau,sep="\n")