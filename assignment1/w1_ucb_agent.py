#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian
  Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
 
  agent does *no* learning, selects actions randomly from the set of legal actions
 
"""

from utils import rand_in_range
from math import sqrt, log
from copy import copy
import numpy as np

np.random.seed(123)

last_action = None # last_action: NumPy array

num_actions = 10
q_estimates = None
q_pulls = None
steps = None
c = .7

### PARAMETER SETTINGS ###		
# Question 1
# alpha = 0.1		
# epsilon = 0
# q1 = 5
# Question 2
alpha = 0.1
epsilon = 0.1
q1 = 0

def agent_init():
    global last_action, epsilon, q_estimates, q_pulls, steps

    q_estimates = np.zeros(num_actions) + q1
    q_pulls = np.ones(num_actions)
    steps = 1

    last_action = np.zeros(1) # generates a NumPy array with size 1 equal to zero

def agent_start(this_observation): # returns NumPy array, this_observation: NumPy array
    global last_action

    last_action[0] = rand_in_range(num_actions)

    local_action = np.zeros(1)
    local_action[0] = rand_in_range(num_actions)

    return local_action[0]


def agent_step(reward, this_observation): # returns NumPy array, reward: floating point, this_observation: NumPy array
    global last_action, q_estimates, q_pulls, num_actions, steps, c

    local_action = np.zeros(1)

    q_estimates[int(last_action[0])] = q_estimates[int(last_action[0])] + alpha * (reward - q_estimates[int(last_action[0])])

    ucb_estimates = copy(q_estimates)

    for i in range(num_actions):
        ucb_estimates[i] += c * sqrt(log(steps) / q_pulls[i])
    local_action[0] = np.argmax(ucb_estimates)

    last_action = local_action
    q_pulls[int(local_action[0])] += 1
    steps += 1

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
