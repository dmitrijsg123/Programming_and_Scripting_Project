#Import pandas library that allows to use its in-built functions, like max(), mnin(), mean() and describe()

import pandas as pd

df=pd.read_csv('Iris.csv')     # reads the csv file

output_textfile = "Variables_Summary.txt"                                                                       # writing to a text file in Python reference:  https://www.geeksforgeeks.org/writing-to-file-in-python/
file = open(output_textfile, "w")
file.close()

#FINDING SEPAL LENGTH VALUES FOR ALL IRIS TYPES - MAX, MIN, MEAN AS WELL AS MORE DETAILED INFO WITH DESCRIBE FUNCTION
maximum = df['Sepal_length'].max()
minimum = df['Sepal_length'].min()
average = df['Sepal_length'].mean()
description = df['Sepal_length'].describe()


print('\nMaximum sepal length of all Iris species is ', maximum, file=open(output_textfile,"a"))                    # \n - new line reference: https://wtmatter.com/python-new-line/
print('Minimum sepal length of all Iris species is ', minimum, file=open(output_textfile,"a"))
print('Average sepal length of all Iris species is ', round(average,1), file=open(output_textfile,"a"))                 # rounding to 1 decimal function - round(my_float,1)  reference:  https://tutorialdeep.com/knowhow/round-float-to-2-decimal-places-python/
print('Some more detailed summarized information:', file=open(output_textfile,"a"))
print(round(description,1), file=open(output_textfile,"a"))

#FINDING SEPAL WIDTH VALUES FOR ALL IRIS TYPES - MAX, MIN, MEAN AS WELL AS MORE DETAILED INFO WITH DESCRIBE FUNCTION
maximum = df['Sepal_width'].max()
minimum = df['Sepal_width'].min()
average = df['Sepal_width'].mean()
description = df['Sepal_width'].describe()


print('\nMaximum sepal width of all Iris species is ', maximum, file=open(output_textfile,"a"))
print('Minimum sepal width of all Iris species is ', minimum, file=open(output_textfile,"a"))
print('Average sepal width of all Iris species is ', round(average,1), file=open(output_textfile,"a"))
print('Some more detailed summarized information:', file=open(output_textfile,"a"))
print(round(description,1), file=open(output_textfile,"a"))

#FINDING PETAL LENGTH VALUES FOR ALL IRIS TYPES - MAX, MIN, MEAN AS WELL AS MORE DETAILED INFO WITH DESCRIBE FUNCTION
maximum = df['Petal_length'].max()
minimum = df['Petal_length'].min()
average = df['Petal_length'].mean()
description = df['Petal_length'].describe()


print('\nMaximum petal length of all Iris species is ', maximum, file=open(output_textfile,"a"))
print('Minimum petal length of all Iris species is ', minimum, file=open(output_textfile,"a"))
print('Average petal length of all Iris species is ', round(average,1), file=open(output_textfile,"a"))
print('Some more detailed summarized information:', file=open(output_textfile,"a"))
print(round(description,1), file=open(output_textfile,"a"))

#FINDING PETAL WIDTH VALUES FOR ALL IRIS TYPES - MAX, MIN, MEAN AS WELL AS MORE DETAILED INFO WITH DESCRIBE FUNCTION
maximum = df['Petal_width'].max()
minimum = df['Petal_width'].min()
average = df['Petal_width'].mean()
description = df['Petal_width'].describe()

print('\nMaximum petal width of all Iris species is ', maximum, file=open(output_textfile,"a"))
print('Minimum petal width of all Iris species is ', minimum, file=open(output_textfile,"a"))
print('Average petal width of all Iris species is ', round(average,1), file=open(output_textfile,"a"))
print('Some more detailed summarized information:', file=open(output_textfile,"a"))
print(round(description,1), file=open(output_textfile,"a"))

#....................................................................................................................

#Iris Setosa only  - maximums for all four parameters
df=pd.read_csv('Iris.csv')                       # reads the csv file
Setosa_maximum = df[df.Species=='setosa']        # df[df.Column_Name==''] function allows to narrow down only to the needed rows (reference: https://youtube.com/watch?V=xvpNA7bC8cs)
print('\nMaximum values for Iris Setosa flowers are: ', file=open(output_textfile,"a"))
print(Setosa_maximum.max(), file=open(output_textfile,"a"))

#Iris Versicolor only  - maximums for all four parameters
df=pd.read_csv('Iris.csv')                       # reads the csv file
Versicolor_maximum = df[df.Species=='versicolor']        
print('\nMaximum values for Iris Versicolor flowers are: ', file=open(output_textfile,"a"))
print(Versicolor_maximum.max(), file=open(output_textfile,"a"))

#Iris Virginica only  - maximums for all four parameters
df=pd.read_csv('Iris.csv')                       # reads the csv file
Virginica_maximum = df[df.Species=='virginica']        
print('\nMaximum values for Iris Virginica flowers are: ', file=open(output_textfile,"a"))
print(Virginica_maximum.max(), file=open(output_textfile,"a"))

#...................................................................................................

#Iris Setosa only  - minimums for all four parameters
df=pd.read_csv('Iris.csv')                       # reads the csv file
Setosa_minimum = df[df.Species=='setosa']       
print('\nMinimum values for Iris Setosa flowers are: ', file=open(output_textfile,"a"))
print(Setosa_minimum.min(), file=open(output_textfile,"a"))

#Iris Versicolor only  - minimums for all four parameters
df=pd.read_csv('Iris.csv')                       # reads the csv file
Versicolor_minimum = df[df.Species=='versicolor']        
print('\nMinimum values for Iris Versicolor flowers are: ', file=open(output_textfile,"a"))
print(Versicolor_minimum.min(), file=open(output_textfile,"a"))

#Iris Virginica only  - minimums for all four parameters
df=pd.read_csv('Iris.csv')                       # reads the csv file
Virginica_minimum = df[df.Species=='virginica']        
print('\nMinimum values for Iris Virginica flowers are: ', file=open(output_textfile,"a"))
print(Virginica_minimum.min(), file=open(output_textfile,"a"))

#...................................................................................................

#Iris Setosa only  - average values for all four parameters
df=pd.read_csv('Iris.csv')                       # reads the csv file
Setosa_average = df[df.Species=='setosa']       
print('\nAverage values for Iris Setosa flowers are: ', file=open(output_textfile,"a"))
print(round(Setosa_average.mean(),2), file=open(output_textfile,"a"))          # will round to 2 decimals here

#Iris Versicolor only  - average values for all four parameters
df=pd.read_csv('Iris.csv')                       # reads the csv file
Versicolor_average = df[df.Species=='versicolor']        
print('\nAverage values for Iris Versicolor flowers are: ', file=open(output_textfile,"a"))
print(round(Versicolor_average.mean(),2), file=open(output_textfile,"a"))

#Iris Virginica only  - average values for all four parameters
df=pd.read_csv('Iris.csv')                       # reads the csv file
Virginica_average = df[df.Species=='virginica']        
print('\nAverage values for Iris Virginica flowers are: ', file=open(output_textfile,"a"))
print(round(Virginica_average.mean(),2), file=open(output_textfile,"a"))


# SCATTERPLOTS
# References https://www.youtube.com/watch?v=GcXcSZ0gQps
# https://matplotlib.org/3.1.1/tutorials/text/text_intro.html
# https://web.microsoftstream.com/video/025ef713-d7c8-492f-97f4-5590015da029?referrer=https:%2F%2Flearnonline.gmit.ie%2Fcourse%2Fview.php%3Fid%3D1598
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("Iris.csv")
sns.set(style = 'whitegrid')                                                         # colour of the background grid
sns.set_palette(None)                                                                # option of changing colour palette (default one left here)
sns.scatterplot(x = 'Sepal_length',y = 'Sepal_width', data = df,hue = 'Species')
plt.title('Comparison of sepal length against sepal width',fontsize=15, fontweight='bold',color='red',fontstyle='italic')              # option of adjusting font size, weight, colour and style
plt.legend(loc='lower right')                                                                                                          # legend positioning
plt.show()


df = pd.read_csv("Iris.csv")
sns.set(style = 'whitegrid')                                                       
sns.scatterplot(x = 'Petal_length', y = 'Petal_width', data = df,hue = 'Species')
plt.title('Comparison of petal length against petal width',fontsize=15, fontweight='bold',color='red',fontstyle='italic') 
plt.legend(loc='lower right')
plt.show()

df = pd.read_csv("Iris.csv")
sns.set(style = 'whitegrid')                                                      
sns.scatterplot(x = 'Sepal_length', y = 'Petal_length', data = df,hue = 'Species')
plt.title('Comparison of sepal length against petal length',fontsize=15, fontweight='bold',color='red',fontstyle='italic')  
plt.legend(loc='lower right')
plt.show()

df = pd.read_csv("Iris.csv")
sns.set(style = 'whitegrid')                                                        
sns.scatterplot(x = 'Sepal_length', y = 'Petal_width', data = df,hue = 'Species')
plt.title('Comparison of sepal length against petal width',fontsize=15, fontweight='bold',color='red',fontstyle='italic')  
plt.legend(loc='lower right')
plt.show()

df = pd.read_csv("Iris.csv")
sns.set(style = 'whitegrid')                                                    
sns.scatterplot(x = 'Sepal_width', y = 'Petal_length', data = df,hue = 'Species')
plt.title('Comparison of sepal width against petal length',fontsize=15, fontweight='bold',color='red',fontstyle='italic')  
plt.legend(loc='upper right')
plt.show()

df = pd.read_csv("Iris.csv")
sns.set(style = 'whitegrid')                                                       
sns.scatterplot(x = 'Sepal_width', y = 'Petal_width', data = df,hue = 'Species')
plt.title('Comparison of sepal width against petal width',fontsize=15, fontweight='bold',color='red',fontstyle='italic') 
plt.legend(loc='upper right')              
plt.show()

sns.pairplot(df, hue='Species')
plt.show()

