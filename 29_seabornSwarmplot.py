import matplotlib.pyplot as plt
import seaborn as sns

# Loading Iris dataset
iris = sns.load_dataset("iris")

# Constructing plot
sns.swarmplot(x="species", y="petal_length", data=iris)

plt.show()