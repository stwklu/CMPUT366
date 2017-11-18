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

import rndmwalk_policy_evaluation
import matplotlib.pyplot as plt

if __name__ == "__main__":

    runs = 10
    num_episodes = 5000
    max_steps = 10000

    try:
        print("Loading TrueValueFunction.npy")
        true_value = np.load("TrueValueFunction.npy")
    except:
        print("File not found.")
        print("Calculating True Value Function")
        true_value = rndmwalk_policy_evaluation.compute_value_function()
        np.save("TrueValueFunction", true_value)

    for run in range(runs):
        print("Run: #" + str(run))
        RL_init()
        run_RMSE_array = np.zeros(num_episodes)
        for episode in range(num_episodes):
            if episode % 100 == 0:
                print(episode)

            RL_episode(max_steps)

            episode_values = RL_agent_message("RMSE")
            RMSE = np.sqrt(np.mean((true_value - episode_values)**2))
            run_RMSE_array[episode] = RMSE
        plt.plot(run_RMSE_array)
        plt.show()

        RL_cleanup()
