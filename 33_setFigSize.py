import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

ax = sns.boxplot(x="total_bill", data=tips)
ax.set(xlim=(0, 100))

plt.show()