#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Andrew
  Jacobsen, Victor Silva, Sina Ghiassian
  Purpose: Implementation of the interaction between the Gambler's problem environment
  and the Monte Carlon agent using RL_glue. 
  For use in the Reinforcement Learning course, Fall 2017, University of Alberta

"""

from rl_glue import *  # Required for RL-Glue
RLGlue("maze_env", "dyna-q_agent")

import numpy as np
import pickle


if __name__ == "__main__":
    num_episodes = 50
    max_steps = 2500
    num_runs = 10

    n_sweep = [0,5,50]

    data = np.zeros((num_episodes, num_runs))

    for n in n_sweep:
        RL_agent_message(["n", n])
        RL_agent_message(["alpha", 0.1])

        for run in range(num_runs):
            np.random.seed(366609 + run)
            # print("Seed = " + str(366 + run))
            print("run number: " + str(run))
            RL_init()
            for episode in range(num_episodes):
                RL_episode(max_steps)
                data[episode][run] = RL_num_steps()
                # if episode == 0:
                #     print("First Episode Length = " + str(RL_num_steps()))
            RL_cleanup()

        average_over_runs = np.mean(data, axis=1) # axis=1 does mean by row, ie per episode
        print(average_over_runs)
        average_over_runs[0] = None # do not plot first episode
        filename = "output" + str(n)
        np.save(filename, average_over_runs)