import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset("titanic")

sns.catplot("class", "survived", "sex", data=titanic, kind="bar", 
	height=7, aspect=2, palette="muted", legend=True)

plt.show()