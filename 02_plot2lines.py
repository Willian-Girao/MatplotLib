import matplotlib.pyplot as plt
import numpy as np

# Returns number spaces evenly w.r.t interval. Similar to arange but instead of step it uses sample number.
X = np.linspace(0, 2 * np.pi, 100)

print(X)

Ya = np.sin(X)
Yb = np.cos(X)

plt.plot(X, Ya)
plt.plot(X, Yb)
plt.show()