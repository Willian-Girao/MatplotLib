import numpy as np
import matplotlib.pyplot as plt

values = np.random.rand(8)
color_set = ('.00', '.25', '.50', '.75')

plt.pie(values, colors = color_set)
plt.show()