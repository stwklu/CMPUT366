#!/usr/bin/env python

"""
  Author: Adam White, Mohammad M. Ajallooeian, Sina Ghiassian
  Purpose: Code for the Gambler's problem environment from the Sutton and Barto
  Reinforcement Learning: An Introduction Chapter 4.
  For use in the Reinforcement Learning course, Fall 2017, University of Alberta 
"""

from utils import rand_norm, rand_in_range, rand_un
import numpy as np

maze = np.zeros((6,9))
start = np.array([3,0])
goal = np.array([5,8])
walls = np.array([[1,2], [2,2], [3,2], [4,5], [0,7], [1,7], [2,7]])

for wall in walls:
    maze[wall[0]][wall[1]] = 1

current_state = start


def env_init():
    global current_state, start
    current_state = start


def env_start():
    """ returns numpy array """
    global current_state, start

    state = start
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
    global current_state, maze, goal

    new_state = current_state
    
    if action == 1: #east
        new_state += [1,0]
    elif action == 2: #south
        new_state += [0,1]
    elif action == 3: #west
        new_state += [-1,0]
    elif action == 4: #north
        new_state += [0,-1]
    else:
        raise Exception("Unknown action taken!")

    # Check within bounds
    if new_state[0] < maze.shape[0] and new_state[0] >= 0:
        if new_state[1] < maze.shape[1] and new_state[1] >= 1:
            # Check for wall
            if maze[new_state] != 1:
                current_state = new_state
    
    
    if current_state ==  goal:
        reward = 1
        is_terminal = True
    else:
        reward = 0
        is_terminal = False

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
