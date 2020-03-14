import numpy as np
from matplotlib import pyplot as plt
import matplotlib

X = np.arange(0.0, 50.0, 2.0)
Y = X ** 1.3 + np.random.rand(*X.shape) * 30.0
S = np.random.rand(*X.shape) * 800 + 500

plt.scatter(X, Y, S, color = 'g', alpha = 0.5, marker = r'$\clubsuit$', label = "Luck")
plt.xlabel("Leprechauns")
plt.ylabel("Gold")
plt.legend(loc=2)
plt.show()