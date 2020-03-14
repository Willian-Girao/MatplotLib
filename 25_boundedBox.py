import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-4, 4, 1024)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

box = { 'facecolor' : '.75', 'edgecolor' : 'k', 'boxstyle' : 'round' }

plt.text(-0.5, -0.20, 'Nice curve in a box', bbox = box)
plt.plot(X, Y, c = 'k')
plt.show()