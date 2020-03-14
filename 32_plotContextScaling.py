import seaborn as sns
import matplotlib.pyplot as plt

# Reset default parameters
sns.set()

# Set context - "paper", "notebook", "talk", "poster"
sns.set_context("poster")

iris = sns.load_dataset("iris")

sns.swarmplot(x="species", y="petal_length", data=iris)

plt.show()