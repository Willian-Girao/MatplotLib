import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")

sns.catplot(x="class", y="survived", hue="sex", data=titanic, kind="bar",
	palette="muted", legend=True)

plt.show()