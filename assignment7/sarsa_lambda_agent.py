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

current_state = None
last_state = None
weights = None

alpha = 0.1/tilings
gamma = 1
lambda = 0.9
epsilon = 0.0

tilings = 8 
shape = [8,8]
iht = IHT(4096)
features = {}

def agent_init():
    """
    Hint: Initialize the variables that need to be reset before each run begins
    Returns: nothing
    """
    #initialize the policy array in a smart way
    global weights, current_state, last_state

    weights = np.zeros(1001)
    current_state = None
    last_state = None

def agent_start(state):
    """
    Hint: Initialize the variavbles that you want to reset before starting a new episode
    Arguments: state: numpy array
    Returns: action: integer
    """
    # pick the first action, don't forget about exploring starts 
    global current_state, last_state

    current_state = 500
    last_state = current_state

    action = get_random_action()

    return action


def agent_step(reward, state): # returns NumPy array, reward: floating point, this_observation: NumPy array
    """
    Arguments: reward: floting point, state: integer
    Returns: action: integer
    """
    # select an action, based on Q
    global current_state, last_state, weights

    current_state = state
    action = get_random_action()
    features = get_feature_vector(current_state)

    TD_error  = alpha * (reward + gamma * get_value(current_state, weights) - get_value(last_state, weights))

    weights = np.add(weights, TD_error * get_feature_vector(last_state))
    # weights += (TD_error * get_feature_vector(last_state))

    last_state = current_state

    return action

def agent_end(reward):
    """
    Arguments: reward: floating point
    Returns: Nothing
    """
    # do learning and update pi
    global weights, last_state

    TD_error  = alpha * (reward - get_value(last_state, weights))

    weights = np.add(weights, TD_error * get_feature_vector(last_state))
    # weights += (TD_error * get_feature_vector(last_state))

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
    else:
        return "I don't know what to return!!"

def get_random_action():
    while True:
        action = np.random.randint(-100,101)
        if action != 0:
            return action

def get_feature_vector(state):
    if state in features:
        return features[state]
    else:
        temp = np.zeros(1001)
        mytiles = tiles(iht, tilings, [float(state)/200])
        for tile in mytiles:
            temp[tile] = 1
        features[state] = temp
        return features[state]

def get_value(state, weights):
    features = get_feature_vector(state)
    return np.dot(weights, features)