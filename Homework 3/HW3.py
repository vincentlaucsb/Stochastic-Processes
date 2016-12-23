# Use Python 3

import numpy as np
import matplotlib.pyplot as plt
from collections import deque

# a) Generate a random number by rolling a die once
die = np.random.random_integers(1, 6, 1)

# b) Generate a sample path of rolling die until the sum exceeds 120
def sample_path():
    path = np.array([])

    while np.sum(path) <= 120:
        path = np.append(path,np.random.random_integers(1, 6, 1))

    return path
        
sample_path_1 = sample_path()

# c) Generate 10000 sample paths
sample_paths = deque() # This will end up being an array of arrays
sample_path_sums = np.array([])
#sample_path_tosses = np.array([]) # This will keep track of the number of tosses for each path

for i in range(0,10000):
    current_path = sample_path()
    sample_paths.append(current_path)
    sample_path_sums = np.append(sample_path_sums,np.sum(current_path))
#    sample_path_tosses = np.append(sample_path_tosses,len(current_path))
    
# d) Generate histogram, mean, and variance
print("Mean: {0}".format(np.mean(sample_path_sums)))
print("Variance: {0}".format(np.var(sample_path_sums)))

# ===
#print("Mean N Tosses: {0}".format(np.mean(sample_path_tosses)))
#print("Variance of N Tosses: {0}".format(np.var(sample_path_tosses)))

#plt.figure(1)
plt.hist(sample_path_sums)
plt.title("Sums of 10,000 Sample Paths")
plt.xlabel("Sum Value")
plt.ylabel("Occurrences")

#plt.figure(2)
#plt.hist(sample_path_tosses)
#plt.title("Number of Tosses")
#plt.xlabel("x")
#plt.ylabel("y")
plt.show()
