import numpy as np
import matplotlib.pyplot as plt

N = 8
A = np.random.random(N)
B = np.random.random(N)
X = np.arange(N)

plt.bar(X, A, color = '.45', hatch = 'x')
plt.bar(X, A + B, bottom = A, color = '.89', hatch = '/')
plt.show()