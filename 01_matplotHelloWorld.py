import math
import matplotlib.pyplot as plt # importing module

X = range(100) # list with all integers from 0 to 99
Y = [value ** 2 for value in X] # idiom - list comprehension

plt.plot(X, Y) # ploting curve (x coor = X, y coor = Y)
plt.show() # renders the graph -  necessary for every matplot lib graph

T = range(100)
X = [(2 * math.pi * t) / len(T) for t in T]
Y = [math.sin(value) for value in X]

plt.plot(X, Y) # ploting curve (x coor = X, y coor = Y)
plt.show() # renders the graph -  necessary for every matplot lib graph