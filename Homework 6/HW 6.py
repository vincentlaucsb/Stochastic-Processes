# Use Python 3

import numpy as np
from random import randint

'''
Simulate One Step in a Markov Chain
 * Used for i) and iv)

Inputs:
 * U ~ Uniform(0,1)     
 * Beginning state
Ouput: End state
'''
def mc(U,state):
    if state == 1:
        if U < 0.5: return 1
        else: return 2
    elif (state == 2) or (state == 3):
        if U < 0.5: return state - 1
        else: return state + 1
    else:
        if U < 0.5: return 3
        else: return 4

# ======== part i Find limiting distribution ========
# Markov Chain with 50 Steps
def mc_50(n=50):
    last_state = 1
    for i in range(0,n):
        U = np.random.uniform(low=0,high=1)
        last_state = mc(U,state=last_state)
    
    return last_state
    
# Repeat 10000 times
mc_final_states = np.array([])

for i in range(0,10000):
    mc_final_states = np.append(mc_final_states,mc_50())
    
final_states = {
    1: sum(mc_final_states == 1)/10000,
    2: sum(mc_final_states == 2)/10000,
    3: sum(mc_final_states == 3)/10000,
    4: sum(mc_final_states == 4)/10000
}

# ==== Print Results ====
print("Part i",final_states,"",sep="\n")

# ======== part iv: Exact Simulation ========
# Programmed according to algorithm described in slides 1-6 of
# http://cs.tau.ac.il/~amnon/Classes/2010-Seminar-Random-Walk/Presentations/Propp-Wilson.pdf
def exact_sim():
    # ==== Step 1 ====
    # Starting with m = 1 seems to cause issues, so we use a larger number instead
    m = 5
    S = (1,2,3,4) # State space
    
    # Return a sequence (1, 2, 4, 8, ...) where length is determined by m
    def N():
        seq = np.array([])
        for i in range(0,m):
            seq = np.append(seq,2**i)
        return seq
    
    # ==== Step 2 ====
    while True:
        U = np.array([])
        first_time = int(min(-N()))

        # Seed the random number generator
        seed=randint(a=0,b=9999999)
        rand = np.random.RandomState(seed)
        
        # Generate sequence of iid uniform R.V.s which is shared by all k chains
        for i in range(0,int(max(N()))):
            U = np.append(U,np.random.uniform(low=0,high=1))

        # Dictionary of states for each chain
        current_state = {}

        for s in S:
            # Initialize Markov Chain to start at s
            current_state[s] = s
            for t in range(first_time,1):
                # Update function
                current_state[s] = mc(U[t],state=current_state[s])

        # ==== Step 3: Check if all states are the same ====
        # Stop and return final state
        if current_state[1] == current_state[2] == current_state[3] == current_state[4]:
            return(current_state[1])
            break

        # ==== Step 4: ====
        else:
            m += 1
            
        # ==== End of while loop: Return to Step 2 ====
    
last_states = {1:0, 2:0, 3:0, 4:0}    

# ==== Output Results =====
print("Part iv")

# Take 10000 samples
for i in range(0,10000):
    last_states[exact_sim()] += 1/10000

print(last_states)