#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Andrew
  Jacobsen, Victor Silva, Sina Ghiassian
  Purpose: Implementation of the interaction between the Gambler's problem environment
  and the Monte Carlon agent using RL_glue. 
  For use in the Reinforcement Learning course, Fall 2017, University of Alberta

"""

from rl_glue import *  # Required for RL-Glue
RLGlue("gambler_env", "tabular_agent")

import numpy as np
import pickle


if __name__ == "__main__":

    runs = 10
    num_episodes = 1000
    max_steps = 10000

    for run in range(runs):
        RL_init()
        for episode in range(num_episodes):
            if episode % 100 == 0:
                print(episode)
            RL_episode(max_steps)
        RL_cleanup()
