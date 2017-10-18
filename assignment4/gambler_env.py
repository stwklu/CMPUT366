#!/usr/bin/env python

"""
  Author: Adam White, Mohammad M. Ajallooeian, Sina Ghiassian
  Purpose: Code for the Gambler's problem environment from the Sutton and Barto
  Reinforcement Learning: An Introduction Chapter 4.
  For use in the Reinforcement Learning course, Fall 2017, University of Alberta 
"""

from utils import rand_norm, rand_in_range, rand_un
import numpy as np

start = [0, 3]
current_state = [0, 0]
goal = [7, 3]
wind = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]
max_x = 9 #inclusive
max_y = 6 #inclusive

def env_init():
    global current_state
    # current_state = np.zeros(1)

    pass

def env_start():
    """ returns numpy array """
    global current_state, start

    current_state = start
    return current_state

def env_step(action):
    """
    Arguments
    ---------
    action : array = [change_in_x, change_in_y]
        the action taken by the agent in the current state

    Returns
    -------
    result : dict
        dictionary with keys {reward, state, isTerminal} containing the results
        of the action taken
    """
    global current_state, goal, wind, max_x, max_y
    new_state = [0, 0]

    # (deep) copy?
    new_state[0] = current_state[0] + action[0]
    new_state[1] = current_state[1] + (action[1] + wind[current_state[0]])

    if new_state[0] > max_x:
        new_state[0] = max_x
    if new_state[0] < 0:
        new_state[0] = 0
    if new_state[1] > max_y:
        new_state[1] = max_y
    if new_state[1] < 0:
        new_state[1] = 0
    
    current_state = new_state
    
    reward = 0.0
    is_terminal = False
    if current_state[0] == goal[0] and current_state[1] == goal[1]:
        is_terminal = True
        # current_state = None
        # reward = 1.0
    else:
        # is_terminal = True
        # current_state = None
        reward = -1.0

    result = {"reward": reward, "state": current_state, "isTerminal": is_terminal}

    return result

def env_cleanup():
    #
    return

def env_message(in_message): # returns string, in_message: string
    """
    Arguments
    ---------
    inMessage : string
        the message being passed

    Returns
    -------
    string : the response to the message
    """
    return ""
