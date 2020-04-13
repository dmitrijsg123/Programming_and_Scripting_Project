#Import pandas library that allows to use its in-built functions, like max(), mnin(), mean() and describe()

import pandas as pd

df=pd.read_csv('Iris.csv')     # reads the csv file


#FINDING MAX, MIN, MEAN AS WELL AS MORE DETAILED INFO WITH DESCRIBE FUNCTION
p=df['Sepal_length'].max()
q=df['Sepal_length'].min()
r = df['Sepal_length'].mean()
s = df['Sepal_length'].describe()


print('Maximum sepal length of all Iris species is ', p)
print('Minimum sepal length of all Iris species is ', q)
print('Average sepal length of all Iris species is ', r)
print(s)