import numpy as np

# ==== Part i ====
def mc(state=1):
    U = np.random.randint(low=0,high=2) # Returns 0 or 1 with probability 1/2 for each
    if state == 1:
        if U == 0: return 1
        else: return 2
    elif (state == 2) or (state == 3):
        if U == 0: return state - 1
        else: return state + 1
    else:
        if U == 0: return 3
        else: return 4
        
# Markov Chain with 50 Steps
def mc_50(n=50):
    last_state = 1
    for i in range(0,n):
        last_state = mc(state=last_state)
    
    return last_state
    
# Repeat 10000 times
mc_final_states = np.array([])

for i in range(0,10000):
    mc_final_states = np.append(mc_final_states,mc_50())
    
# Find limiting distribution
p1 = sum(mc_final_states == 1)/10000
p2 = sum(mc_final_states == 2)/10000
p3 = sum(mc_final_states == 3)/10000
p4 = sum(mc_final_states == 4)/10000

print(p1,p2,p3,p4)