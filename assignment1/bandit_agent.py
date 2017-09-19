#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian
  Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
 
  agent does *no* learning, selects actions randomly from the set of legal actions
 
"""

from utils import rand_in_range
import numpy as np

last_action = None # last_action: NumPy array

num_actions = 10
q_estimates = None

### PARAMETER SETTINGS ###		
alpha = 0.1		
epsilon = 0		
q1 = 5

def agent_init():
    global last_action, epsilon 

    q_estimates = np.zeros(num_actions) + epsilon

    last_action = np.zeros(1) # generates a NumPy array with size 1 equal to zero

def agent_start(this_observation): # returns NumPy array, this_observation: NumPy array
    global last_action

    last_action[0] = rand_in_range(num_actions)

    local_action = np.zeros(1)
    local_action[0] = rand_in_range(num_actions)

    return local_action[0]


def agent_step(reward, this_observation): # returns NumPy array, reward: floating point, this_observation: NumPy array
    global last_action, q_estimates

    local_action = np.zeros(1)
    local_action[0] = rand_in_range(num_actions)

    if np.random.uniform() < epsilon: # Explore
        last_action[0] = np.random.randint(num_actions)
    else: # Exploit
        last_action[0] = np.argmax(q_estimates)
    # might do some learning here

    # last_action = local_action

    return last_action

def agent_end(reward): # reward: floating point
    # final learning update at end of episode
    return

def agent_cleanup():
    # clean up
    return

def agent_message(inMessage): # returns string, inMessage: string
    # might be useful to get information from the agent

    if inMessage == "what is your name?":
        return "my name is skeleton_agent!"
  
    # else
    return "I don't know how to respond to your message"
