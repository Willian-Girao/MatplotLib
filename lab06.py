import matplotlib.pyplot as plt
import numpy as np

label_set = (b'Iris-setosa', b'Iris-versicolor', b'Iris-virginica')

def read_label(label):
    return label_set.index(label)

data = np.loadtxt('iris.txt', delimiter = ',', converters = { 4 : read_label })

color_set = ('.20', '.55', '.90') 
color_list = [color_set[int(label)] for label in data[:,4]]

plt.scatter(data[:,0], data[:,1], color = color_list)
plt.show()