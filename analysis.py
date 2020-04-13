#Import pandas library that allows to use its in-built functions, like max(), mnin(), mean() and describe()

import pandas as pd

df=pd.read_csv('Iris.csv')     # reads the csv file


#FINDING SEPAL LENGTH VALUES FOR ALL IRIS TYPES - MAX, MIN, MEAN AS WELL AS MORE DETAILED INFO WITH DESCRIBE FUNCTION
maximum = df['Sepal_length'].max()
minimum = df['Sepal_length'].min()
average = df['Sepal_length'].mean()
description = df['Sepal_length'].describe()


print('Maximum sepal length of all Iris species is ', maximum)
print('Minimum sepal length of all Iris species is ', minimum)
print('Average sepal length of all Iris species is ', average)
print('Here is some more detailed summarized information:', description)

#FINDING SEPAL WIDTH VALUES FOR ALL IRIS TYPES - MAX, MIN, MEAN AS WELL AS MORE DETAILED INFO WITH DESCRIBE FUNCTION
maximum = df['Sepal_width'].max()
minimum = df['Sepal_width'].min()
average = df['Sepal_width'].mean()
description = df['Sepal_width'].describe()

print('Maximum sepal width of all Iris species is ', maximum)
print('Minimum sepal width of all Iris species is ', minimum)
print('Average sepal width of all Iris species is ', average)
print('Here is some more detailed summarized information:', description)

#FINDING PETAL LENGTH VALUES FOR ALL IRIS TYPES - MAX, MIN, MEAN AS WELL AS MORE DETAILED INFO WITH DESCRIBE FUNCTION
maximum = df['Petal_length'].max()
minimum = df['Petal_length'].min()
average = df['Petal_length'].mean()
description = df['Petal_length'].describe()

print('Maximum petal length of all Iris species is ', maximum)
print('Minimum petal length of all Iris species is ', minimum)
print('Average petal length of all Iris species is ', average)
print('Here is some more detailed summarized information:', description)

#FINDING PETAL WIDTH VALUES FOR ALL IRIS TYPES - MAX, MIN, MEAN AS WELL AS MORE DETAILED INFO WITH DESCRIBE FUNCTION
maximum = df['Petal_width'].max()
minimum = df['Petal_width'].min()
average = df['Petal_width'].mean()
description = df['Petal_width'].describe()

print('Maximum petal width of all Iris species is ', maximum)
print('Minimum petal width of all Iris species is ', minimum)
print('Average petal width of all Iris species is ', average)
print('Here is some more detailed summarized information:', description)

#Iris Setosa only  - maximums for all four parameters
import pandas as pd

df=pd.read_csv('Iris.csv')                                                     
Setosa_maximum = df[df.Species=='setosa']                                             # df[df.Column_Name==''] function allows to narrow down only to the needed rows (reference: https://youtube.com/watch?V=xvpNA7bC8cs)
print('Maximum values for Iris Setosa flowers are: ',Setosa_maximum.max())

#Iris Versicolor only  - maximums for all four parameters
df=pd.read_csv('Iris.csv')                                                   
Versicolor_maximum = df[df.Species=='versicolor']        
print('Maximum values for Iris Versicolor flowers are: ',Versicolor_maximum.max())

#Iris Virginica only  - maximums for all four parameters
df=pd.read_csv('Iris.csv')                                                    
Virginica_maximum = df[df.Species=='virginica']        
print('Maximum values for Iris Virginica flowers are: ',Virginica_maximum.max())

#Iris Setosa only  - minimums for all four parameters
df=pd.read_csv('Iris.csv')                                                  
Setosa_minimum = df[df.Species=='setosa']       
print('Minimum values for Iris Setosa flowers are: ',Setosa_minimum.min())

#Iris Versicolor only  - minimums for all four parameters
df=pd.read_csv('Iris.csv')                    
Versicolor_minimum = df[df.Species=='versicolor']        
print('Minimum values for Iris Versicolor flowers are: ',Versicolor_minimum.min())

#Iris Virginica only  - minimums for all four parameters
df=pd.read_csv('Iris.csv')              
Virginica_minimum = df[df.Species=='virginica']        
print('Minimum values for Iris Virginica flowers are: ',Virginica_minimum.min())

#Iris Setosa only  - average values for all four parameters
df=pd.read_csv('Iris.csv')                  
Setosa_average = df[df.Species=='setosa']       
print('Average values for Iris Setosa flowers are: ',Setosa_average.mean())

#Iris Versicolor only  - average values for all four parameters
Versicolor_average = df[df.Species=='versicolor']        
print('Average values for Iris Versicolor flowers are: ',Versicolor_average.mean())

#Iris Virginica only  - average values for all four parameters
df=pd.read_csv('Iris.csv')                
Virginica_average = df[df.Species=='virginica']        
print('Average values for Iris Virginica flowers are: ',Virginica_average.mean())
