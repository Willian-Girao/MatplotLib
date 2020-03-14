import matplotlib.pyplot as plt
import numpy as np

women_pop = np.array([5.,30.,45.,22.])
men_pop = np.array([5.,25.,50.,20.])

X = np.arange(4)

print(X)

plt.barh(X, women_pop, color = '.15')
plt.barh(X, -men_pop, color = '.85')

plt.show()