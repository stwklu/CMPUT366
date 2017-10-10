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
    num_episodes = 8000
    max_steps = 10000

    num_runs = 10
    key_episodes = [99, 999, 7999]

    v_over_runs={}
    # dict to hold data for key episodes
    for episode in key_episodes:
        v_over_runs[episode] = []

    for run in range(num_runs):
      counter = 0
      print "run number: ", run
      RL_init()
      print "\n"
      for episode in range(num_episodes):
        RL_episode(max_steps)
        if (episode in key_episodes):
          V = pickle.loads(RL_agent_message('ValueFunction'))
          # V is (n,) np.array
          v_over_runs[episode].append(V)
          counter += 1
      RL_cleanup()
      
    n = v_over_runs[key_episodes[0]][0].shape[0]
    n_valueFunc = len(key_episodes)
    average_v_over_runs = np.zeros((n_valueFunc,n))
    for i,episode in enumerate(key_episodes):
        # each item in dict is a list (one item per run), and each item is a value function 
        data = np.matrix(v_over_runs[episode])
        # therefore data is (num_runs x length of value fucntion)
        average_v_over_runs[i] = np.mean(data, axis=0)

    np.save("ValueFunction", average_v_over_runs)
