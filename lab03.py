import numpy as np
import matplotlib.pyplot as plt

A = np.array([5., 30., 45., 22.]) 
B = np.array([5., 25., 50., 20.])
C = np.array([3.,  4.,  12.,  11.])

X = np.arange(4)

plt.bar(X, A, color = 'b')
plt.bar(X, B, color = 'g', bottom = A)
plt.bar(X, C, color = 'r', bottom = A + B)

plt.show()