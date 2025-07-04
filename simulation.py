import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt



part_pos = np.random.rand(100, 2) * 10

velocities = np.random.randn(100, 2)

timesteps = 1000

for i in range(timesteps):
    part_pos += velocities * timesteps

mask_x = (part_pos[:, 0] < 0) | (part_pos[:, 0] > 10)
mask_y = (part_pos[:, 1] < 0) | (part_pos[:, 1] > 10)

velocities[mask_x, 0] *= -1
velocities[mask_y, 1] *= -1



plt.clf()
plt.scatter(part_pos[:, 0], part_pos[:, 1], c='blue')
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.pause(0.01)
plt.show()