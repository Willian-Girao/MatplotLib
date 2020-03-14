import numpy as np
import matplotlib.pyplot as plt

A = np.random.standard_normal((100, 2))
A += np.array((-1, -1))

B = np.random.standard_normal((100, 2))
B += np.array((1, 1))

plt.scatter(A[:,0], A[:,1], color = '0.55', marker = 'x')
plt.scatter(B[:,0], B[:,1], color = '0.25', marker = '^')
plt.show()