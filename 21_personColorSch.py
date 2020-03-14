import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('lines', linewidth = 2.)
mpl.rc('axes', facecolor = 'k', edgecolor = 'w')
mpl.rc('xtick', color = 'w')
mpl.rc('ytick', color = 'w')
mpl.rc('text', color = 'w')
mpl.rc('figure', facecolor = 'k', edgecolor = 'w')

X = np.linspace(0, 7, 1024)

plt.plot(X, np.sin(X), color = '0.95', label = 'sin')
plt.plot(X, np.cos(X), color = '0.65', label = 'cos')
plt.legend()
plt.show()