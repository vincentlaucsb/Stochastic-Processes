import numpy as np

# 10d. Calculate probabilities using Chapman-Kolmogorov Equations
transition_matrix = np.matrix('0 1 0 0 0 0; 0 0.2 0.8 0 0 0; 0 0 0.4 0.6 0 0; 0 0 0 0.6 0.4 0; 0 0 0 0.8 0.2 0; 0 0 0 0 0 1')

for i in range(5,21):
    print(transition_matrix**i)
    print("Probability X_{0} = 5 is {1}".format(i,np.array((transition_matrix**i)[0])[0][5]))