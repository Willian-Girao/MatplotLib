import matplotlib.pyplot as plt
import numpy as np

X = np.random.randn(10000)

plt.hist(X, bins=20)

plt.show()