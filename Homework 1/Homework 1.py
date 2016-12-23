import math
import numpy
import matplotlib.pyplot as plt

''' Want: 1000 Uniform Random Variables
    U is a random sample (n = 1000) from Uniform(0,1)
    U[0], U[1], ..., U[999] ~ Uniform(0,1) iid
'''
U = numpy.random.uniform(low=0,high=1,size=1000)

''' f_inverse(x) = 1 - exp((-1/3)x) for x > 0 #
    Input: x ~ U(0,1)
    Expected Output: an exponential random variable
'''
def f_inverse(x):
    return -3 * math.log(1-x)

''' Want: 1000 Exponential Random Variables, i.e. e[0], ..., e[999],
    via Inversion Method, where
    e[k] = f_inverse(U[k]) for k = 0,..., 999
'''
e = []
for k in range(0,1000):
    # e will now be a list of 1000 exponential random variables
    # i.e. e[0], e[1], ..., e[999] ~ Exponential(3) iid
    e.append(f_inverse(U[k]))

print("Sample Mean:",numpy.mean(e))
print("Sample Variance:",numpy.var(e))

''' Returns a histogram with the values of the random samples on the x-axis,
    and the number of occurences on the y-axis
'''
plt.hist(e, 50)

# Histogram Title Stuff
xbar = str(numpy.mean(e))[0:4]
s2 = str(numpy.var(e))[0:4]
title = r'A Plot of 1000 Random Samples $\bar X = {0}$, $S^2 = {1}$'.format(xbar,s2)
plt.xlabel(r'$e_k$')
plt.ylabel('Occurences')
plt.title(title,fontsize=16)

plt.show()
