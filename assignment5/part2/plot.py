#!/usr/bin/env python

"""
 Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian, Zach Holland
 Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
"""

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
  alpha_sweep = [0.03125, 0.0625, 0.125, 0.25, 0.5, 1.0]

  data = []

  fig = plt.figure()

  for i, alpha in enumerate(alpha_sweep):
    ax = fig.add_subplot(3,3,i+1) # create separate graph for each alpha value
    data = np.load("output"+str(alpha)+".npy")
    plt.xlim([0,50])
    plt.ylim([0,1000])
    # plt.xlabel("Episodes")
    # plt.ylabel("Steps per episode")
    plt.plot(data, label="alpha = " + str(alpha))
    plt.legend(prop={'size': 6})
    # ax.imshow(()

  # plt.show()
  plt.savefig("Dyna-Q.png")