import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

raw_data = {'first_name': ['Mike', 'Brad', 'Chan', 'Dee', 'Stan'], 
        'last_name': ['Miller', 'Smith', 'Man', 'Milner', 'Chin'], 
        'female': [0, 1, 1, 0, 1],
        'age': [42, 52, 36, 24, 73], 
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}

df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'female', 'preTestScore', 'postTestScore'])

print(df)

plt.scatter(df.preTestScore, df.postTestScore, s=[value * 2 for value in df.age], c =df.female)
plt.show()