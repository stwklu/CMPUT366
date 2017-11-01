#!/usr/bin/env python

"""
 Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian, Zach Holland
 Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
"""

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
  output0 = np.load('output0.npy')
  output5 = np.load('output5.npy')
  output50 = np.load('output50.npy')

  plt.xlim([0,50])
  plt.ylim([0,850])
  plt.xlabel("Episodes")
  plt.ylabel("Steps per episode")

  plt.plot(output0, label="n = 0 (direct RL only)")
  plt.plot(output5, label="n = 5")
  plt.plot(output50, label="n = 50")

  plt.legend()

  plt.show()