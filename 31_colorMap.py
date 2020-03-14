import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

N = 500

# Constructing colormap
current_palette = sns.color_palette("muted", n_colors=5)
cmap = ListedColormap(sns.color_palette(current_palette).as_hex())

data1 = np.random.randn(N)
data2 = np.random.randn(N)

colors = np.random.randint(0,5,N)

plt.scatter(data1, data2, c=colors, cmap=cmap)

# Adding color bar
plt.colorbar()

plt.show()