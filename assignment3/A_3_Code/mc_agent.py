#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian
  Purpose: Skeleton code for Monte Carlo Exploring Starts Control Agent
           for use on A3 of Reinforcement learning course University of Alberta Fall 2017
 
"""

from utils import rand_in_range, rand_un
import numpy as np
import pickle

Q = np.full((101, 51), 0.0)
pi = np.zeros(101)
returns = {}
path = []


def agent_init():
    """
    Hint: Initialize the variables that need to be reset before each run begins
    Returns: nothing
    """

    global Q, pi, returns, path

    #initialize the policy array in a smart way
    Q = np.full((101, 51), 0.0)
    pi = np.zeros(101)
    returns = {}
    path = []
    
    for state in range(1,100):
        pi[state] = min(state, 100 - state)


def agent_start(state):
    """
    Hint: Initialize the variavbles that you want to reset before starting a new episode
    Arguments: state: numpy array
    Returns: action: integer
    """
    global Q, pi, returns, path

    # pick the first action, don't forget about exploring starts 
    action = np.random.random_integers(1, min(state[0], 100 - state[0]))
    path = [] # Clear path every episode or else would reward previous episode paths

    if action == 0:
        print("ACTION ZERO IN START")
    return action


def agent_step(reward, state): # returns NumPy array, reward: floating point, this_observation: NumPy array
    """
    Arguments: reward: floting point, state: integer
    Returns: action: integer
    """

    global Q, pi, returns, path

    # select an action, based on Q
    action = int(pi[state])

    if action == 0:
        print("Zero in step")

    path.append((state[0], action))

    return action

def agent_end(reward):
    """
    Arguments: reward: floating point
    Returns: Nothing
    """

    global Q, returns, path
    # do learning and update pi
    
    for stop in path:
        # print(stop)
        if stop in returns:
            returns[stop].append(reward)
        else:
            returns[stop] = [reward]

    # print("Rewards")
    # print(returns)

    # print(Q)
    for key in returns:
        # print(key)
        # print(key[0])
        # print(key[1])
        # print(Q[key[0]][key[1]])
        Q[key[0]][key[1]] = (sum(returns[(key[0], key[1])]) / len(returns[(key[0], key[1])]))
        # print(sum(returns[(key[0], key[1])] / len(returns[(key[0], key[1])])))

    # print()
    for state in range(1, 100):        
        if np.argmax(Q[state]) == 0:
            pi[state] = rand_in_range(min(state, 100 - state)) + 1
        else:
            pi[state] = np.argmax(Q[state])
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

