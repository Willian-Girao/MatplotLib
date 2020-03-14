import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100, 3)

print(data)

plt.boxplot(data)
plt.show()