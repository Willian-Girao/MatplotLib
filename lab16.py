import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(size=(20, 6)) + np.arange(6) / 2

sns.set_style("whitegrid")
sns.boxplot(data=data)
plt.title("whitegrid")
plt.show()

sns.set_style("darkgrid")
sns.boxplot(data=data);
plt.title("darkgrid")
plt.show()

sns.set_style("white")
sns.boxplot(data=data);
plt.title("white")
plt.show()

sns.set_style("dark")
sns.boxplot(data=data);
plt.title("dark")
plt.show()

sns.set_style("ticks")
sns.boxplot(data=data);
plt.title("ticks")
plt.show()