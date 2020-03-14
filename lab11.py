import numpy as np
import matplotlib.pyplot as plt

M = np.random.standard_normal((1000, 2))
R = np.sum(M ** 2, axis = 1)

plt.scatter(M[:, 0], M[:, 1], c = 'b', marker = 's', s = 10 * R)
plt.show()