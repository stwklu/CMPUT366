#!/usr/bin/env python

"""
  Author: Adam White, Mohammad M. Ajallooeian
  Purpose: for use of Reinforcement learning course University of Alberta Fall 2017
 
  env *ignores* actions: rewards are all random
"""

from utils import rand_norm, rand_in_range, rand_un
import numpy as np

arm_count = 10
this_reward_observation = (None, None, None) # this_reward_observation: (floating point, NumPy array, Boolean)
arms_centres = np.zeros(arm_count)

def env_init():
    global arms_centres

    for i in range(arm_count):
        arms_centres[i] = rand_norm(0,1)

def env_start(): # returns NumPy array
    return this_reward_observation[1]

def env_step(this_action): # returns (floating point, NumPy array, Boolean), this_action: NumPy array
    global this_reward_observation, arms_centres
    the_reward = rand_norm(arms_centres[int(this_action)], 1.0) # rewards drawn from (seed, 1) Gaussian

    this_reward_observation = (the_reward, this_reward_observation[1], False)

    return this_reward_observation

def env_cleanup():
    #
    return

def env_message(inMessage): # returns string, inMessage: string
    if inMessage == "what is your name?":
        return "my name is skeleton_environment!"
  
    # else
    return "I don't know how to respond to your message"
