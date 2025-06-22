import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import tkinter as tk
plt.style.use ('seaborn-v0_8-poster')


#print(plt.style.available)

part_pos_x = np.random.rand(5)
part_pos_y = np.random.rand(5)
part_pos_z = np.random.rand(5)

print(part_pos_z)

plt.scatter(part_pos_x, part_pos_y)
plt.show()