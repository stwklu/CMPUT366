#!/usr/bin/env python

"""
 Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian, Zach Holland
 Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
"""

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
      V = np.load('Value.npy')
      plt.show()
      plt.plot(V,label="Value")
      plt.xlim([0,100])
      # plt.ylim([0,1])
      plt.xticks([1,25,50,75,99])
      plt.xlabel('Capital')
      plt.ylabel('Value Estimates')
      plt.legend()
      plt.show()