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
alpha = None
epsilon = 0.1
gamma = 0.95
n = None
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
    global Q, model, previous_states

    Q = np.zeros((6,9,4))
    model = np.zeros((6,9,4), object)
    previous_states = {}

def agent_start(state):
    """
    Hint: Initialize the variavbles that you want to reset before starting a new episode
    Arguments: state: numpy array
    Returns: action: integer
    """
    # pick the first action, don't forget about exploring starts 
    global S, epsilon, last_action, Q

    S = state

    if rand_un() < epsilon:
        action = rand_in_range(4)
    else:
        action = argmax(Q[S[0]][S[1]])
    
    last_action = action

    return action


def agent_step(reward, state): # returns NumPy array, reward: floating point, this_observation: NumPy array
    """
    Arguments: reward: floting point, state: integer
    Returns: action: integer
    """
    # select an action, based on Q
    global epsilon, maze, Q, last_action, S, alpha, S_, model, n

    S_ = state

    if (S[0],S[1]) not in previous_states:
        previous_states[(S[0],S[1])] = []
    previous_states[(S[0],S[1])].append(last_action)

    Q[S[0]][S[1]][last_action] += alpha * (reward + gamma * max(Q[S_[0]][S_[1]]) - Q[S[0]][S[1]][last_action])
    model[S[0]][S[1]][last_action] = (reward, S_[0], S_[1])

    for  i in range(n):
        S_planning = random.choice(previous_states.keys())
        A_planning = random.choice(previous_states[S_planning])
        # print(model[S_planning[0]][S_planning[1]][A_planning])
        reward_planning, x_planning, y_planning = model[S_planning[0]][S_planning[1]][A_planning]

        Q[S_planning[0]][S_planning[1]][A_planning] += alpha * (reward_planning + gamma * max(Q[x_planning][y_planning]) -  Q[S_planning[0]][S_planning[1]][A_planning])

    if rand_un() < epsilon:
        action = rand_in_range(4)
    else:
        action = argmax(Q[S[0]][S[1]])

    S = S_
    last_action = action
    
    return action

def agent_end(reward):
    """
    Arguments: reward: floating point
    Returns: Nothing
    """
    # do learning and update pi

    Q[S[0]][S[1]][last_action] += alpha * (reward + gamma * max(Q[S_[0]][S_[1]]) - Q[S[0]][S[1]][last_action])

    return

def agent_cleanup():
    """
    This function is not used
    """
    # clean up
    return

def agent_message(in_message): # returns string, in_message: string
    global n, alpha
    """
    Arguments: in_message: string
    returns: The value function as a string.
    This function is complete. You do not need to add code here.
    """
    # should not need to modify this function. Modify at your own risk
    if (in_message[0] == "n"):
        n = in_message[1]
    elif (in_message[0] == "alpha"):
        alpha = in_message[1]
    else:
        return "I don't know what to return!!"

def argmax(a):
    # Robert Kern
    # https://mail.scipy.org/pipermail/numpy-discussion/2015-March/072459.html
    return np.random.choice(np.where(a == a.max())[0])