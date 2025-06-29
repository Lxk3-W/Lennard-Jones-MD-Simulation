import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import tkinter as tk


part_pos = np.random.rand(2, 2) * 10

velocities = np.random.rand(2, 2)

timesteps = 10

for i in range(timesteps):
    part_pos += velocities * timesteps




print(part_pos_z)

plt.clf
plt.scatter(part_pos, part_pos_y)
plt.show()