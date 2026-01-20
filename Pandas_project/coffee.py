import pandas as pd

Coffee=pd.read_csv(open('Coffee.csv'))
#print(Coffee.head())
#print(Coffee.sample(9))
#print(Coffee.loc[[0,1,5]])
#print(Coffee)



import numpy as np

arr_1 = np.array([2:11:2])
arr_2 = np.array([2:11:2])

print(arr_1+arr_2)