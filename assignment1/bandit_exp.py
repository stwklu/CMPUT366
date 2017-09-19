#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian
  Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
  Last Modified by: Andrew Jacobsen, Victor Silva, Mohammad M. Ajallooeian
  Last Modified on: 16/9/2017

  Experiment runs 2000 runs, each 1000 steps, of an n-armed bandit problem
"""

from rl_glue import *  # Required for RL-Glue
RLGlue("bandit_env", "bandit_agent")

import numpy as np
import sys

def save_results(data, data_size, filename): # data: floating point, data_size: integer, filename: string
    with open(filename, "w") as data_file:
        for i in range(data_size):
            data_file.write("{0}\n".format(data[i]))

if __name__ == "__main__":
    num_runs = 2000
    max_steps = 1000

    # array to store the results of each step
    optimal_action = np.zeros(max_steps)

    print "\nPrinting one dot for every run: {0} total Runs to complete".format(num_runs)
    for k in range(num_runs):
        RL_init()

        RL_start()
        for i in range(max_steps):
            # RL_step returns (reward, state, action, is_terminal); we need only the
            # action in this problem
            action = RL_step()[2]

            '''
            check if action taken was optimal

            you need to get the optimal action; see the news/notices
            announcement on eClass for how to implement this
            '''
            # update your optimal action statistic here

        RL_cleanup()
        print ".",
        sys.stdout.flush()

    save_results(optimal_action / num_runs, max_steps, "RL_EXP_OUT.dat")
    print "\nDone"
