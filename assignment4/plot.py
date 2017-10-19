#!/usr/bin/env python

"""
 Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian, Zach Holland
 Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
"""

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
  output = open("output.dat", "r")
  data_x = []
  data_y = []

  for episode in output:
    episode_data = episode.strip().split(",")
    data_x.append(episode_data[0])
    data_y.append(episode_data[1])

  for i in range(len(data_x)-1):
    plt.plot(int(data_x[i]), int(data_y[i]), "ro")

  plt.show()