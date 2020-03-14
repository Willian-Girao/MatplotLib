import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-4, 4, 1024)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

plt.annotate('Low Point', ha = 'center', va = 'bottom', xytext = (-1.5, 3.), xy = (0.75, -2.7),
	arrowprops = {'facecolor': 'black', 'shrink': 0.05})

plt.plot(X, Y, c = 'k')
plt.show()