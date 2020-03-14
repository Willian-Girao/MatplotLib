import numpy as np
import matplotlib.pyplot as plt

values = np.random.randn(100)

b = plt.boxplot(values)

for name, line_list in b.items():
	for line in line_list:
		line.set_color('.20')

plt.show()