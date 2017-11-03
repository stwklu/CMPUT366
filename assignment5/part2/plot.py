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

  for i, alpha in enumerate(alpha_sweep):
    load = np.load("output"+str(alpha)+".npy")
    data.append(np.mean(load))

  print(data)  
  
  # fig, ax = plt.subplots()
  # ax.set_xticklabels((" ", "0.03125", "0.0625", "0.125", "0.25", "0.5", "1.0"))
  # ax.set_xlabel("Alpha")
  # ax.set_ylabel("Average steps per episode over first 50 episodes")
  # bars = ax.bar(np.arange(6), data)
  plt.ylim([25,30])
  plt.plot(data)

  plt.savefig("Dyna-Q.png")