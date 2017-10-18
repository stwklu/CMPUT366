#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Andrew
  Jacobsen, Victor Silva, Sina Ghiassian
  Purpose: Implementation of the interaction between the Gambler's problem environment
  and the Monte Carlon agent using RL_glue. 
  For use in the Reinforcement Learning course, Fall 2017, University of Alberta

"""

from rl_glue import *  # Required for RL-Glue
RLGlue("gambler_env", "mc_agent")

import numpy as np
import pickle

if __name__ == "__main__":
  max_steps = 8000

  RL_init()

  RL_episode(max_steps)
  print(RL_num_episodes(), RL_num_steps())