#!/usr/bin/env python

"""
  Author: Adam White, Mohammad M. Ajallooeian, Sina Ghiassian
  Purpose: Code for the Gambler's problem environment from the Sutton and Barto
  Reinforcement Learning: An Introduction Chapter 4.
  For use in the Reinforcement Learning course, Fall 2017, University of Alberta 
"""

from utils import rand_norm, rand_in_range, rand_un
import numpy as np

current_state = [0, 3]
goal = [7, 3]
wind = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]
max_x = 9 #inclusive
max_y = 6 #inclusive

def env_init():
    global current_state
    current_state = np.zeros(1)


def env_start():
    """ returns numpy array """
    global current_state

    state = rand_in_range(num_total_states) + 1 # This is required for exploring starts
    current_state = np.asarray([state])
    return current_state

def env_step(action):
    """
    Arguments
    ---------
    action : int
        the action taken by the agent in the current state

    Returns
    -------
    result : dict
        dictionary with keys {reward, state, isTerminal} containing the results
        of the action taken
    """
    global current_state
    if action < 1 or action > np.minimum(current_state[0], num_total_states + 1 - current_state[0]):
        print "Invalid action taken!!"
        print "action : ", action
        print "current_state : ", current_state
        exit(1)

    if rand_un() < head_probability:
        current_state[0] = current_state[0] + action
    else:
        current_state[0] = current_state[0] - action
    
    reward = 0.0
    is_terminal = False
    if current_state[0] == num_total_states + 1:
        is_terminal = True
        current_state = None
        reward = 1.0
    elif current_state[0] == 0:
        is_terminal = True
        current_state = None

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
