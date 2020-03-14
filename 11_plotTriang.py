import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

data = np.random.rand(100, 2)
triangles = tri.Triangulation(data[:,0], data[:,1])

print(data)

plt.triplot(triangles)
plt.show()