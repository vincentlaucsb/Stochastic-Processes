""" 
This is the third Python HW
By: Nathan Fritter
Professor Hohn
Section: W 10:00 - 10:50 am
TA: Mousavi
As a heads up, the part_c function calls part_d and part_e
"""

# Import necessary libraries
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def part_b():
    # Create necessary lists and counters for part b
    state_space = [0, 1, 2, 3, 4, 5]
    song_list = [1, 2, 3, 4, 5]
    songs_listened_to = []
    num_unique_songs = 0
    time_steps = 0
    
    # Begin while loop
    while num_unique_songs < 5:
        current_song = np.random.choice(song_list)
        time_steps += 1
        
        # If at time zero, add song to list and move on
        if num_unique_songs == 0:
            num_unique_songs += 1
            songs_listened_to.append(current_song)

        # If song has been listened to, continue
        if current_song in songs_listened_to:
            continue
        # Or else append the song to the list
        else: 
            songs_listened_to.append(current_song)
            num_unique_songs += 1

    # Print out number of time steps
    print("The number of time steps required to get to 5 unique songs was: %d" % time_steps)


def part_c():
    num_sim = 10000
    current_sim = 0
    sim_paths = []
    while current_sim < num_sim:

        # Taken from Part B
        # Create necessary lists and counters for part c
        state_space = [0, 1, 2, 3, 4, 5]
        song_list = [1, 2, 3, 4, 5]
        songs_listened_to = []
        num_unique_songs = 0
        time_steps = 0

        # Begin while loop
        while num_unique_songs < 5:
            current_song = np.random.choice(song_list)
            time_steps += 1
        
            # To take care of initial conditions
            if num_unique_songs == 0:
                num_unique_songs += 1
                songs_listened_to.append(current_song)
            # If we have already heard the song, increment and move on
            if current_song in songs_listened_to:
                continue
            # Or else append song number to list
            else: 
                songs_listened_to.append(current_song)
                num_unique_songs += 1

        # After each simulation finishes
        current_sim += 1

        # Add number of time steps to the list    
        sim_paths.append(time_steps)

    # Call Part D function
    part_d(sim_paths)

def part_d(sim_time_steps): 

    # Now to find probabilities
    num_sim = 10000
    n = 5
    probs = []
    while n < 21:
        num_times_correct = 0
        for entry in sim_time_steps:
            if entry == n:
                num_times_correct += 1
        
        prob = num_times_correct / num_sim
        print("The probability of playing the last unique song on time step number %d is: %.2f" % (n, prob)) 
        probs.append(prob)
        n += 1
            
    # Call Part E function
    part_e(probs)
        
    
def part_e(probabilities):
    time_steps = [i for i in range(5,21)]
    plt.bar(left = time_steps, height = probabilities, align = 'center', alpha = 0.5, color = 'r')
    plt.title('Number of Time Steps to 5 Unique Songs vs Probability of Drawing Fifth Unique Song')
    plt.show()


part_b()
part_c()

