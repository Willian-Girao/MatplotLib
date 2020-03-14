import matplotlib.pyplot as plt
import numpy as np

data = np.random.standard_normal((100, 2))

plt.scatter(data[:,0], data[:,1], color = '.90', edgecolor = '.00')
plt.show()