#!/usr/bin/env python

"""
 Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian, Zach Holland
 Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
"""

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
   V = np.load('ValueFunction.npy')
   plt.show()
   print V.shape
   for i, episode_num in enumerate([100, 1000, 8000]):
     plt.plot(V[i, :], label='episode : ' + str(episode_num))
     plt.xlim([0,100])
     plt.xticks([1,25,50,75,99])
     plt.xlabel('Capital')
     plt.ylabel('Value estimates')
     plt.legend()
   plt.show()