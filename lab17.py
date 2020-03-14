import matplotlib.pyplot as plt
import seaborn as sns

sns.set_context("paper", font_scale=6, rc={"font.size":6,"axes.labelsize":1})

iris = sns.load_dataset("iris")

sns.swarmplot(x="species", y="petal_length", data=iris)

plt.show()