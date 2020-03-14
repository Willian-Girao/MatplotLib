import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
import pandas as pd

x = 10 ** np.arange(1, 10)
y = x * 2

data = pd.DataFrame(data={'x': x, 'y': y})

grid = sns.lmplot('x', 'y', data, height=7, truncate=True, scatter_kws={"s": 100})

grid.set_xticklabels(rotation=60)

plt.show()