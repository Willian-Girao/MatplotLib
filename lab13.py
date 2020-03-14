import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-4, 4, 1024)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

plt.text(1., 2., 'Nice Curve')

plt.plot(X, Y, c = 'k') 
plt.show() 