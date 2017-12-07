#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Andrew
  Jacobsen, Victor Silva, Sina Ghiassian
  Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
  Last Modified by: Mohammad M. Ajallooeian, Sina Ghiassian
  Last Modified on: 21/11/2017

"""

from rl_glue import *  # Required for RL-Glue
from sarsa_lambda_agent import F
RLGlue("mountaincar", "sarsa_lambda_agent")

import numpy as np

if __name__ == "__main__":
    num_episodes = 1000
    num_runs = 1

    steps = np.zeros([num_runs,num_episodes])

    for r in range(num_runs):
        print "run number : ", r
        RL_init()
        for e in range(num_episodes):
            # print '\tepisode {}'.format(e+1)
            RL_episode(0)
            steps[r,e] = RL_num_steps()
    weights = RL_agent_message("3d")

    fout = open('value', 'w')
    steps = 50
    data = np.zeros([steps, steps])
    for i in range(steps): # POSITION
        for j in range(steps): # VELOCITY
            values = []
            for a in range(3):
                # tilecode ([pos = -1.2 + (i * 1.7 / steps), vel = -0.07 + (j * 0.14 / steps)], action = [a]) => inds
                position = 8.0 * (float(i)/steps) # add lower bound 1.2 to get positives only, divide by range
                velocity = 8.0 * (float(j)/steps)
                tile = [position, velocity]

                inds = F(tile, a)

                value = np.sum(weights[inds])
                # values.append(-Q(inds,w))
                values.append(value)
            # height = max of values
            height = max(values)

            data[j,i] = - height
            fout.write(repr(height) + ' ')
        fout.write('\n')
    fout.close()

    np.save('heights', data)
    np.save('steps',steps)