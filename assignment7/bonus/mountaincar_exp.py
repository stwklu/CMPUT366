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
    num_runs = 5

    steps = np.zeros([num_runs,num_episodes])

    runs_errors = np.zeros(num_runs)

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
    
    print(runs_errors)
    print(np.mean(runs_errors))
    np.save('steps',steps)