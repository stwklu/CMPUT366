#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Andrew
  Jacobsen, Victor Silva, Sina Ghiassian
  Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
  Last Modified by: Mohammad M. Ajallooeian, Sina Ghiassian
  Last Modified on: 21/11/2017

"""

from rl_glue import *  # Required for RL-Glue
RLGlue("mountaincar", "sarsa_lambda_agent")

import numpy as np

if __name__ == "__main__":
    num_episodes = 200
    num_runs = 50

    steps = np.zeros([num_runs,num_episodes])

    runs_errors = np.zeros(num_runs)

    np.random.seed(366609)
    for r in range(num_runs):
        print "run number : ", r
        RL_init()
        run_total = 0.0
        for e in range(num_episodes):
            # print '\tepisode {}'.format(e+1)
            RL_episode(0)
            steps[r,e] = RL_num_steps()
            run_total += RL_return()
        runs_errors[r] = run_total
    
    original_mean = np.mean(runs_errors)
    original_std = np.std(runs_errors)
    original_error = original_std / (num_runs**0.5)
    
    print("Unmodified")
    print("Mean: " + str(original_mean))
    print("Std: " + str(original_std))
    print("Error: " + str(original_error))

    RLGlue("mountaincar", "sarsa_lambda_agent_modified")

    steps = np.zeros([num_runs,num_episodes])

    runs_errors = np.zeros(num_runs)

    np.random.seed(366609)
    for r in range(num_runs):
        print "run number : ", r
        RL_init()
        run_total = 0.0
        for e in range(num_episodes):
            # print '\tepisode {}'.format(e+1)
            RL_episode(0)
            steps[r,e] = RL_num_steps()
            run_total += RL_return()
        runs_errors[r] = run_total
    
    mod_mean = np.mean(runs_errors)
    mod_std = np.std(runs_errors)
    mod_error = mod_std / (num_runs**0.5)
    
    print("Modified")
    print("Mean: " + str(mod_mean))
    print("Std: " + str(mod_std))
    print("Error: " + str(mod_error))


    print("Did it Change?")

    if original_error > mod_error:
        larger_error = original_error
    else:
        larger_error = mod_error


    imp = (mod_mean - original_mean) / larger_error

    print("Improvement: " + str(imp))

    np.save('steps', steps)

