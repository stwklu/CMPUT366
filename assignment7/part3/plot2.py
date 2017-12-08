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


  x = np.arange(-1.2, 0.5, 1.7 / 50)
  y = np.arange(-0.07, 0.07, 0.14 / 50)
  # x = np.arange(0, 50, 1)
  # y = np.arange(0, 50, 1)

  data = data.reshape(len(x), len(y))
  x1, y1 = np.meshgrid(x, y)


  ax.set_xticks([-1.2, 0.5])
  ax.set_yticks([0.07, -0.07])
  ax.set_zticks([0, np.max(data)])
  ax.set_ylabel('Velocity')
  ax.set_xlabel('Position')
  ax.set_zlabel('Cost To Go')
  # ax.plot_wireframe(x1, y1, data)
  ax.plot_surface(x1,y1,data, cstride=1, rstride=1)
  plt.savefig('part3.png')
  plt.show()