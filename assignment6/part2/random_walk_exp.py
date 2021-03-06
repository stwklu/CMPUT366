#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Andrew
  Jacobsen, Victor Silva, Sina Ghiassian
  Purpose: Implementation of the interaction between the Gambler's problem environment
  and the Monte Carlon agent using RL_glue. 
  For use in the Reinforcement Learning course, Fall 2017, University of Alberta

"""

from rl_glue import *  # Required for RL-Glue

import numpy as np
import pickle

import rndmwalk_policy_evaluation
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # Uncomment (or modify!) agents list to match the agents you want to run!

    agents = [  'tabular', # main agents asked for in the assignment
                'tile_coding', 
                'aggregation', 
                'polynomial20003'] 
    # agents = [  'polynomial', # for polynomial level experiment
    #             'polynomial2', 
    #             'polynomial3', 
    #             'polynomial4']
    # agents = [  'polynomial201', # for alpha tuning experiment v1
    #             'polynomial2001', 
    #             'polynomial20001']
    # agents = [  'polynomial2003', # for alpha tuning experiment v2
    #             'polynomial2001', 
    #             'polynomial20003']
    runs = 10
    num_episodes = 5000
    max_steps = 10000
    seed = 366609

    data = np.zeros((len(agents), runs, num_episodes))

    try:
        print("Loading TrueValueFunction.npy")
        true_value = np.load("TrueValueFunction.npy")
    except:
        print("File not found.")
        print("Calculating True Value Function")
        true_value = rndmwalk_policy_evaluation.compute_value_function()
        np.save("TrueValueFunction", true_value)

    for agent_number, agent in enumerate(agents):
        print("Starting agent: " + agent)
        RLGlue("random_walk_env", agent + "_agent")
        for run in range(runs):
            np.random.seed(seed+run)
            print("Run: #" + str(run))
            RL_init()
            run_RMSE_array = np.zeros(num_episodes)
            for episode in range(num_episodes):
                if episode % (num_episodes/10) == 0:
                    percent = float(episode)/num_episodes*100
                    print(str(episode) + "/" + str(num_episodes) + "   " + str(percent) + "% of run")
                    print(run_RMSE_array[episode-1])

                RL_episode(max_steps)

                episode_values = RL_agent_message("RMSE")
                RMSE = np.sqrt(np.mean((true_value[1:] - episode_values[1:])**2))
                run_RMSE_array[episode] = RMSE

            data[agent_number-1][run] = run_RMSE_array
            RL_cleanup()
            # print(np.random.randint(100,1000)) # Check that randomness same across episodes
        
        plt.plot(np.mean(data[agent_number-1], axis=0), label=agent)
    
    plt.xlabel("Episodes")
    plt.ylabel("RMSE")
    plt.legend()
    plt.savefig("random_walk.png")
    plt.show()

