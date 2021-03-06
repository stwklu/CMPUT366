#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian
  Purpose: Skeleton code for Monte Carlo Exploring Starts Control Agent
           for use on A3 of Reinforcement learning course University of Alberta Fall 2017
 
"""

from utils import rand_in_range, rand_un
import numpy as np
import pickle

import matplotlib.pyplot as plt
from tiles3 import *

last_state = None
last_action = None
last_tile = None
weights = None 
values = None
Z = None

tilings = 8 
alpha = 0.1/tilings
gamma = 1.0
lambdah = 0.9
epsilon = 0.0
shape = [8,8] # where [0] is position, [1]  is velocity
iht = IHT(4096)


def agent_init():
    """
    Hint: Initialize the variables that need to be reset before each run begins
    Returns: nothing
    """
    #initialize the policy array in a smart way
    global weights, values

    values = np.zeros([shape[0], shape[1], 3]) # size of tiling shape and depth of # actions
    weights = np.random.uniform(-0.001, 0.0, 4096) # eClass said use 4096, same as IHT size


def agent_start(state):
    """
    Hint: Initialize the variavbles that you want to reset before starting a new episode
    Arguments: state: numpy array
    Returns: action: integer
    """
    # pick the first action, don't forget about exploring starts 
    global last_state, last_action, last_tile, Z

    # determine which tile index for position and velocity
    position = shape[0] * (state[0] + 1.2) / (1.2 + 0.5) # add lower bound 1.2 to get positives only, divide by range
    velocity = shape[1] * (state[1] + 0.07) / (0.07 + 0.07)
    tile = [position, velocity]

    action = get_epsilon_action(tile)

    last_state = state
    last_action = action
    last_tile = tile

    Z = np.zeros(len(weights)) # eClass - same length as weights

    return action


def agent_step(reward, state): # returns NumPy array, reward: floating point, this_observation: NumPy array
    """
    Arguments: reward: floting point, state: integer
    Returns: action: integer
    """
    # select an action, based on Q
    global last_state, last_action, last_tile, weights, Z, values

    TD_error = reward
    
    for i in F(last_tile, last_action):
        TD_error -= weights[i]
        Z[i] = 1.0

    position = shape[0] * (state[0] + 1.2) / (1.2 + 0.5) # add lower bound 1.2 to get positives only, divide by range
    velocity = shape[1] * (state[1] + 0.07) / (0.07 + 0.07)
    tile = [position, velocity]

    action = get_epsilon_action(tile)
    
    activated = np.zeros(len(weights))

    for i in F(tile, action):
        activated[i] = 1.0
        TD_error += gamma * weights[i]

    weights += alpha * TD_error * Z
    Z = gamma * lambdah * Z

    last_state = state
    last_action = action
    last_tile = tile

    return action

def agent_end(reward):
    """
    Arguments: reward: floating point
    Returns: Nothing
    """
    # do learning and update pi
    global weights, Z

    # no need to get new tile from pos and vel

    TD_error = reward

    for i in F(last_tile, last_action):
        TD_error -= weights[i]
        Z[i] = 1.0

    weights += alpha * TD_error * Z

    return


def agent_cleanup():
    """
    This function is not used
    """
    # clean up

    return


def agent_message(in_message): # returns string, in_message: string
    """
    Arguments: in_message: string
    returns: The value function as a string.
    This function is complete. You do not need to add code here.
    """
    # should not need to modify this function. Modify at your own risk
    if (in_message == 'RMSE'):
        estimated_values = np.zeros(1001)
        for state in range(1001):
            estimated_values[state] = get_value(state, weights)
        return estimated_values
    elif (in_message == '3d'):
        return weights
    else:
        return "I don't know what to return!!"


def get_epsilon_action(state):
    if np.random.uniform() < epsilon: # explore
        action = np.random.randint(3)
        print("Yeaaaaaaaaaaaaaaaaaaa this probably shouldn't have happened when eps=0, plz fix")
    else: # exploit
        options = []
        for action in range(3):
            tiles123 = F(state, action)
            options.append(np.sum(weights[tiles123]))
        options = np.array(options)
        action = argmax(options)
    return action


def argmax(a):
    # Robert Kern
    # https://mail.scipy.org/pipermail/numpy-discussion/2015-March/072459.html
    return np.random.choice(np.where(a == a.max())[0])


def F(state, action):
    return tiles(iht, tilings, state, [action])