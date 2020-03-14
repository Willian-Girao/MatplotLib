import numpy as np
import matplotlib.pyplot as plt

name_list = ('Mike', 'Brad', 'Stan', 'Jon', 'Matt')
value_list = np.random.randint(0, 99, size = len(name_list))
pos_list = np.arange(len(name_list))

plt.bar(pos_list, value_list, color = '.75', align = 'center')
plt.xticks(pos_list, name_list)
plt.show()