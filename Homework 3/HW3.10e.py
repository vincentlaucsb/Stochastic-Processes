import numpy as np
import matplotlib.pyplot as plt
from collections import deque

# Goal: Find the distribution of N #

def sample_path():
    path = np.array([])

    while np.sum(path) <= 120:
        path = np.append(path,np.random.random_integers(1, 6, 1))

    return path
        
# c) Generate 10000 sample paths
sample_paths = deque() # This will end up being an array of arrays
sample_path_tosses = np.array([]) # This will keep track of the number of tosses for each path

for i in range(0,50000):
    if (i%5000 == 0): print("Currently on {0}".format(i))
    current_path = sample_path()
    sample_paths.append(current_path)
    sample_path_tosses = np.append(sample_path_tosses,len(current_path))
        
# d) Generate histogram, mean, and variance
print("Mean N Tosses: {0}".format(np.mean(sample_path_tosses)))
print("Variance of N Tosses: {0}".format(np.var(sample_path_tosses)))

plt.hist(sample_path_tosses)
plt.title("Number of Tosses")
plt.xlabel("N Number of Tosses")
plt.ylabel("Occurences")
plt.show()