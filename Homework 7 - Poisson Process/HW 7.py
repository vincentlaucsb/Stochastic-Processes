import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

class SSRandomWalk(OrderedDict):
    '''
    Simple Symmetric Random Walk
     * Models a SSRW using a Python dictionary
     * The keys of this dictionary are steps on the walk, e.g. value on the 10th step = SSRandomWalk()[10]
     * SSRandomWalk().tau_x(x) returns the minnimum n step where we encounter x
     
    Example of creating a Simple Symmetric Random Walk
    >>> my_drunk_walk = SSRandomWalk(steps=200)
    
    '''
    def __init__(self,steps=100):
        super(SSRandomWalk, self).__init__()
        self[0] = 0
        self.current_value = 0
        self.current_step = 0
        self.simulate(steps)
        
    def simulate(self,steps):
        for i in range(0,steps):
            U = np.random.uniform(0,1)
            if U <= 0.5:
                self.current_value += 1
            else:
                self.current_value -= 1
            
            # Keep track of what value S0, S1, ... Sn is
            self.current_step += 1
            self[self.current_step] = self.current_value
        
    def tau_x(self,x):
        # Return min{n: Sn = x}
        for n in range(0,self.current_step):
            if self[n] == x:
                return n
        
        # Return None if x is never encountered on our walk
        return None

class PoissonProcess(OrderedDict):
    '''
    Standard Poisson Process
     * Models a PP as a Python dictionary 
      * Option 1: Simulate Poisson Process for n events
      * Option 2: Simulate Poisson Process until time is exceeded
     * The keys of the dictionary correspond to times, e.g. PoissonProcess()[4.5]
     
    Example of a 200-event Poisson Process
    >>> earthquakes = PoissonProcess(mean=1)
    >>> earthquakes.simulate(n=200)
    '''
    def __init__(self,mean=1,n=0,time=0):
        # Specify EITHER a number n of events OR time but NOT BOTH
        super(PoissonProcess, self).__init__()
        self[0] = 0 # This is a standard Poisson Process
        self.mean = mean
        self.wait_times = OrderedDict()
        self.simulate(n,time)
        
    def __getitem__(self,key):
        # Keys should be time indices
        # If a requested key is not stored in the dictionary, return the value of the highest key that doesn't exceed the given key
        try:
            return super(PoissonProcess, self).__getitem__(key)
        except KeyError:
            keys = super(PoissonProcess, self).keys()
            key = max([t for t in keys if t < key])
            return super(PoissonProcess, self).__getitem__(key)
            
    def simulate(self,n,time):
        def one_step():
            wait_time = np.random.exponential(1/self.mean)
            prev_count = self[max(self.keys())]
            current_time = wait_time + max(self.keys())
            
            self[current_time] = prev_count + 1
            self.wait_times[prev_count + 1] = wait_time
            
        # Simulate n events in a Poisson Process
        if n:
            for i in range(0, n):
                one_step()
        
        # Simulate a Poisson Process until we exceed a time
        elif time:
            while max(self.keys()) < time:
                one_step()
            
    def when(self,n):
        # Return the time when the nth event occured
        for i in range(0,len(self.keys())):
            if self[list(self.keys())[i]] == n:
                return list(self.keys())[i]
   
# ==== 10a. Simple Symmetric Random Walk with 100 Steps ====
def estimate_s(n=100,sample_size=10000):
    samples = np.array([])
    for i in range(0,sample_size):
        S = SSRandomWalk(steps=n)
        samples = np.append(samples,S[n])
    
    return samples

plt.figure(1)
plt.suptitle("Distribution of $S_{100}$")
plt.hist(x=estimate_s(),bins=10,normed=True)

# ==== 10b. Estimate tau_x for x in Z (we'll estimate it for -5 <= x <= 6) ====
def estimate_tau_x(lower=-5,upper=6):
    tau = OrderedDict()

    for x in range(lower,upper+1):
        tau[x] = np.array([])
    
    for i in range(0,1000):
        steps = 1000
        S = SSRandomWalk(steps=steps)
        for x in range(lower,upper+1):
            tau_x = S.tau_x(x)
            if tau_x == None:
                tau[x] = np.append(tau[x],steps)
            else:
                tau[x] = np.append(tau[x],tau_x)
            
    return tau
    
tau_x = estimate_tau_x()
fig = 2
sub = 1
for x in range(-5,7):
    if sub == 5:
        fig += 1
        sub = 1
    
    plt.figure(fig)
    subplot = plt.subplot(2,2,sub)
    subplot.set_title(r'Plot of $\tau_{0}$'.format('{' + str(x) + '}'))
    plt.suptitle(r"Plot of $\tau_x$")
    plt.hist(x=tau_x[x],bins=50,normed=True)
    sub += 1
                    
# ==== 10c. Graph one sample path ====
def poisson_graph():
    # Generate points that can be plotted on a graph
    path = PoissonProcess(mean=2,n=50)

    # We want x between 0 and 20
    x = np.array([])
    y = np.array([])

    for i in range(0,1000):
        x = np.append(x,i/50)
        y = np.append(y,path[i/50])
        
    return (x,y)

data = poisson_graph()
plt.figure(fig + 1)
plt.plot(data[0],data[1],'o')
plt.suptitle('Plot of a Poisson Process with rate 2')

# ==== 10d. Estimate Expectation of N(10) ====
def estimate_mean(t=10):
    samples = np.array([]) # Values of N(10)
    
    for i in range(0,2000):
        N = PoissonProcess(mean=2,time=10)
        samples = np.append(samples, N[10])
        
    return np.mean(samples)

plt.figure(fig + 2)
plt.suptitle("Mean of N(10): {0}".format(estimate_mean()))
plt.show()