import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-6, 6, 1024)
Y1 = np.sinc(X)
Y2 = np.sinc(X) + 1

plt.plot(X, Y1, marker = 'o', color = '.45', markevery = 50)
plt.plot(X, Y2, marker = 'o', color = 'b', markevery = 100)
plt.show()