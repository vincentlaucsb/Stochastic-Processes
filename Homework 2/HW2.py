# Hi Mark, use Python 3

import math
import numpy as np
import matplotlib.pyplot as plt

# 10) a. Generate X[0], ... X[999] ~ N(0,1) iid
X = np.random.normal(loc=0,scale=1,size=1000)

print("X1, ..., X1000 ~ N(0, 1)")
print("Mean:",np.mean(X))
print("Variance",np.var(X))

# Y[0], ..., Y[999] ~ N(0,1) iid
Y = np.random.normal(loc=0,scale=1,size=1000)

# 10) b. Compute Vi = (Xi^2 Yi^2)/2
V = (X**2 + Y**2)/2    
U = np.array(1 - np.exp(np.array(-1 * V)))

## 10) d. Compute Empirical Distribution Function
    
''' Empirical Distribution Function:
    Inputs:
        samples: X_1, ..., X_n iid
        x:       Some real number

'''
def emp_cdf(samples,x):
    ''' Indicator Function for Empirical Distribution:
        1: if X_i <= x
        0: otherwise
        
        sample = X_i
    '''
    def indicator(sample):
        # Note: This function will grab the value of "x" from the scope of the parent function.
        if sample <= x: return 1
        else: return 0
    sigma = 0
    n = len(samples)
    
    for X_i in samples:
        sigma += indicator(X_i)
    return (1/n) * sigma

# Function is a string with a matematical expression, e.g. function='x+5'
# Input: function is a f: R --> R
def graph(function,xmin,xmax):
    dom = np.arange(xmin,xmax+0.05,0.05) # Domain
    # See http://stackoverflow.com/questions/477486/python-decimal-range-step-value
    # for an explanation of arange
    
    fx = np.array([]) # Range
    
    # Generate range
    for x in dom:
        # Note: y evaluates to inf in case of div by zero
        y = eval(function)
        fx = np.append(arr=fx,values=y)
    
    plt.plot(dom,fx)
    
# ==== Verify that V ~ Exp(beta=1) ====
plt.figure(2)
plt.hist(x=V,bins=20,normed=True)
plt.title("V ~ Exponential(1)")
graph("math.e**-x",xmin=0,xmax=16) # Plot the Exponential(beta=1) PDF

# ==== Plot the Empirical Distribution Function ====
plt.figure(1)
plt.title(r'Graph of $F_n$, $F_U$')
graph("emp_cdf(U,x)",xmin=0,xmax=1)
graph("x",xmin=0,xmax=1)
plt.legend(['Empirical Distribution','Uniform(0,1) CDF'],loc='upper left')
plt.xlabel(r'$X$')
plt.ylabel(r'$P (X \leq x)$')

# ==== Try Emp CDF Function on Another Distribution ====
plt.figure(3)
plt.title("Test Case: Exponential(10)")
exp10 = np.random.exponential(scale=10,size=1000)
graph("emp_cdf(exp10,x)",xmin=0,xmax=100)
graph("1 - math.e**(-x/10)",xmin=0,xmax=100)

# ==== Show the Graphs ====
plt.show()