import os
from matplotlib import pyplot as plt
import numpy as np

import mpl_toolkits.mplot3d
import matplotlib

filename = 'heights.npy'

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


if os.path.exists(filename):
  inp = np.load(filename)
  data = np.array([])
  data = np.append(data, inp)
  print(data)


  x = np.arange(-1.2, 0.5, 1.7 / 50)
  y = np.arange(-0.07, 0.07, 0.14 / 50)
  # x = np.arange(0, 50, 1)
  # y = np.arange(0, 50, 1)
  data = data.reshape(len(x), len(y))
  x1, y1 = np.meshgrid(x, y)


  ax.set_xticks([-1.2, 0.5])
  ax.set_yticks([-0.07, 0.07])
  ax.set_zticks([0, np.amax(data)])
  ax.set_ylabel('Position')
  ax.set_xlabel('Velocity')
  ax.set_zlabel('Height')
  ax.plot_wireframe(x1, y1, data)
  plt.savefig('3d.png')
  plt.show()