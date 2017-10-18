#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian
  Purpose: Skeleton code for Monte Carlo Exploring Starts Control Agent
           for use on A3 of Reinforcement learning course University of Alberta Fall 2017
 
"""

from utils import rand_in_range, rand_un
import numpy as np
import pickle

### PARAMETERS ###
alpha = 0.1
epsilon = 0.1
actions_permitted = 8
### PARAMETERS ###

### GLOBALS ###
Q = None # Where [0] is x and [1] is y
action_list = [
    [1, 0], # E
    [0, -1], # S
    [-1, 0], # W
    [0, 1], # N
    [1, 1], # NE
    [1, -1], # SE
    [-1, -1], # SW
    [-1, 1],  # NW
    [0, 0] # Nothing
]
last_action = None
### GLOBALS ###



def agent_init():
    """
    Hint: Initialize the variables that need to be reset before each run begins
    Returns: nothing
    """
    global actions_permitted, Q
    #initialize the policy array in a smart way

    Q = np.zeros((9, 6, actions_permitted)) # Size specific to our example

def agent_start(state):
    """
    Hint: Initialize the variavbles that you want to reset before starting a new episode
    Arguments: state: numpy array
    Returns: action: integer
    """
    global actions_permitted, Q, action_list
    # pick the first action, don't forget about exploring starts 

    if rand_un() < epsilon:
        action = action_list[rand_in_range(actions_permitted)]
    else:
        action = np.argmax(Q[state[0]][state[1]])

    return action


def agent_step(reward, state): # returns NumPy array, reward: floating point, this_observation: NumPy array
    """
    Arguments: reward: floting point, state: integer
    Returns: action: integer
    """
    # select an action, based on Q
    return action

def agent_end(reward):
    """
    Arguments: reward: floating point
    Returns: Nothing
    """
    # do learning and update pi

    return

def agent_cleanup():
    """
    This function is not used
    """
    # clean up
    return

def agent_message(in_message): # returns string, in_message: string
    global Q
    """
    Arguments: in_message: string
    returns: The value function as a string.
    This function is complete. You do not need to add code here.
    """
    # should not need to modify this function. Modify at your own risk
    if (in_message == 'ValueFunction'):
        return pickle.dumps(np.max(Q, axis=1), protocol=0)
    else:
        return "I don't know what to return!!"

