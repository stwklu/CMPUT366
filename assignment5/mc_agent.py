#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian
  Purpose: Skeleton code for Monte Carlo Exploring Starts Control Agent
           for use on A3 of Reinforcement learning course University of Alberta Fall 2017
 
"""

from utils import rand_in_range, rand_un
import numpy as np
import pickle
import random

### PARAMETERS ###
alpha = 0.1
epsilon = 0.1
gamma = 0.95
n = 5
### PARAMETERS ###

### GLOBALS ###
Q = None
model = None
S = None
last_action = None
S_ = None
previous_states = None
### GLOBALS ###


def agent_init():
    """
    Hint: Initialize the variables that need to be reset before each run begins
    Returns: nothing
    """
    globals Q, model, previous_states

    Q = np.zeros((6,9,4))
    model = np.zeros((6,9,4))
    previous_states  []

def agent_start(state):
    """
    Hint: Initialize the variavbles that you want to reset before starting a new episode
    Arguments: state: numpy array
    Returns: action: integer
    """
    # pick the first action, don't forget about exploring starts 
    globals S, epsilon, last_action,

    S = state

    if rand_un() < epsilon:
        action = rand_in_range(4)
    else:
        action = np.argmax(maze[S])
    
    last_action = action
    
    if [state, action] not in previous_states:
        previous_states.append([state, action])

    return action


def agent_step(reward, state): # returns NumPy array, reward: floating point, this_observation: NumPy array
    """
    Arguments: reward: floting point, state: integer
    Returns: action: integer
    """
    # select an action, based on Q
    globals epsilon, maze, Q, last_action, S, alpha, S_, model, n

    S_ = state

    if [state, action] not in previous_states:
        previous_states.append([state, action])

    Q[S][last_action] += alpha * (reward + gamma * np.argmax(Q[S_]) - Q[S][last_action])
    model[S][last_action] = [reward, S_]

    for  i in range(n):
        rand = random.choice(previous_states)
        S_rand = rand[0]
        A_rand = rand[1]
        R_model = model[S_rand][A_rand[0]
        S_model = model[S_rand][A_rand[1]

        Q[S_rand][A_rand] += alpha * (R_model + gamma * np.argmax(Q[S_model]) - Q[S_rand][A_rand])


    if rand_un() < epsilon:
        action = rand_in_range(4)
    else:
        action = np.argmax(maze[S[0]][S[1]])
    
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

