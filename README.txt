PROGRAMMING AND SCRIPTING PROJECT

FISHER'S IRIS DATA SET


Data set online research:
The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper "The use of multiple measurements in taxonomic problems".
Based on Fisher's linear discriminant model, the data set became a typical test case for many statistical classification techniques in machine learning such as support vector machines.

The set consists of measurements, in centimetres, of 50 samples of each of three types of iris flowers (setosa, versicolor and virginica) – 150 in total. 
For each of the type four measurements were taken – sepal length, sepal width, petal length and petal width.

https://en.wikipedia.org/wiki/Iris_flower_data_set
https://wikimili.com/en/Iris_flower_data_set


The Iris Dataset is saved into a CSV file (Comma Separated Value file).
The following Python libraries are essential and are to be imported to be able to make the necessary program run (https://web.microsoftstream.com/video/025ef713-d7c8-492f-97f4-5590015da029?referrer=https:%2F%2Flearnonline.gmit.ie%2Fcourse%2Fview.php%3Fid%3D1598):

Pandas 
Matplotlib
Seaborn


Pandas is an open-source Python Library providing high-performance data manipulation and analysis tool using its powerful data structures. The name Pandas is derived from the word Panel Data – an Econometrics from Multidimensional data.
Python with Pandas is used in a wide range of fields including academic and commercial domains including finance, economics, Statistics, analytics, etc.

import pandas as pd                           #This first line imports the Pandas module
from pandas import DataFrame, read_csv        #The read_csv method loads the data in a Pandas dataframe that we will name df.
df = pd.read_csv(filename)                    ## Opens, analyzes, and reads the CSV file provided, and stores the data in a DataFrame.
References: https://pythonspot.com/pandas-read-csv/
	   https://realpython.com/python-csv/

Matplotlib
matplotlib.pyplot is a rich collection of command style functions. Certain pyplot functions will help us make some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, title, type of plot (for example, histogram or scatter) etc
plt.show() command displays all figures.

import matplotlib.pyplot as plt              #This first line imports Matplotlib library
Reference: https://matplotlib.org/3.2.0/tutorials/introductory/pyplot.html


Seaborn
Seaborn is a library for making statistical graphics in Python. It is built on top of matplotlib and closely integrated with pandas data structures.

Here is some of the functionality that seaborn offers:

A dataset-oriented API for examining relationships between multiple variables

Specialized support for using categorical variables to show observations or aggregate statistics

Options for visualizing univariate or bivariate distributions and for comparing them between subsets of data

Automatic estimation and plotting of linear regression models for different kinds dependent variables

Convenient views onto the overall structure of complex datasets

High-level abstractions for structuring multi-plot grids that let you easily build complex visualizations

Concise control over matplotlib figure styling with several built-in themes

Tools for choosing color palettes that faithfully reveal patterns in your data

Seaborn aims to make visualization a central part of exploring and understanding data. Its dataset-oriented plotting functions operate on dataframes and arrays containing whole datasets and internally perform the necessary semantic mapping and statistical aggregation to produce informative plots.
Reference: https://seaborn.pydata.org/introduction.html

Seaborn.pairplot function
seaborn.pairplot(data, hue=None, hue_order=None, palette=None, vars=None, x_vars=None, y_vars=None, kind='scatter', diag_kind='auto', markers=None, height=2.5, aspect=1, corner=False, dropna=True, plot_kws=None, diag_kws=None, grid_kws=None, size=None)
Plot pairwise relationships in a dataset.
https://seaborn.pydata.org/generated/seaborn.pairplot.html

CODE FOR SHOWING VARIABLES

import pandas as pd   #Import pandas library that allows to use its in-built functions, like max(), min(), mean() and describe()

df=pd.read_csv('Iris.csv')     # reads the csv file


#FINDING SEPAL LENGTH VALUES FOR ALL IRIS TYPES - MAX, MIN, MEAN AS WELL AS MORE DETAILED INFO WITH DESCRIBE FUNCTION
maximum = df['Sepal_length'].max()
minimum = df['Sepal_length'].min()
average = df['Sepal_length'].mean()
description = df['Sepal_length'].describe()

#FINDING SEPAL WIDTH VALUES FOR ALL IRIS TYPES - MAX, MIN, MEAN AS WELL AS MORE DETAILED INFO WITH DESCRIBE FUNCTION
maximum = df['Sepal_width'].max()
minimum = df['Sepal_width'].min()
average = df['Sepal_width'].mean()
description = df['Sepal_width'].describe()

#FINDING PETAL LENGTH VALUES FOR ALL IRIS TYPES - MAX, MIN, MEAN AS WELL AS MORE DETAILED INFO WITH DESCRIBE FUNCTION
maximum = df['Petal_length'].max()
minimum = df['Petal_length'].min()
average = df['Petal_length'].mean()
description = df['Petal_length'].describe()

#FINDING PETAL WIDTH VALUES FOR ALL IRIS TYPES - MAX, MIN, MEAN AS WELL AS MORE DETAILED INFO WITH DESCRIBE FUNCTION
maximum = df['Petal_width'].max()
minimum = df['Petal_width'].min()
average = df['Petal_width'].mean()
description = df['Petal_width'].describe()

#Iris Setosa only  - maximums for all four parameters
import pandas as pd

df=pd.read_csv('Iris.csv')                                                     
Setosa_maximum = df[df.Species=='setosa']                                   # df[df.Column_Name==''] function allows to narrow down only to the needed rows (reference: https://youtube.com/watch?V=xvpNA7bC8cs)

#Iris Versicolor only  - maximums for all four parameters
df=pd.read_csv('Iris.csv')                                                   
Versicolor_maximum = df[df.Species=='versicolor']        

#Iris Virginica only  - maximums for all four parameters
df=pd.read_csv('Iris.csv')                                                    
Virginica_maximum = df[df.Species=='virginica']        


#Iris Setosa only  - minimums for all four parameters
df=pd.read_csv('Iris.csv')                                                  
Setosa_minimum = df[df.Species=='setosa']       

#Iris Versicolor only  - minimums for all four parameters
df=pd.read_csv('Iris.csv')                    
Versicolor_minimum = df[df.Species=='versicolor']        

#Iris Virginica only  - minimums for all four parameters
df=pd.read_csv('Iris.csv')              
Virginica_minimum = df[df.Species=='virginica']        

#Iris Setosa only  - average values for all four parameters

df=pd.read_csv('Iris.csv')                  
Setosa_average = df[df.Species=='setosa']       

#Iris Versicolor only  - average values for all four parameters
Versicolor_average = df[df.Species=='versicolor']        
print('Average values for Iris Versicolor flowers are: ',Versicolor_average.mean())

#Iris Virginica only  - average values for all four parameters
df=pd.read_csv('Iris.csv')                
Virginica_average = df[df.Species=='virginica']    

---------------------------------------------------------------
EXAMPLE OF PRINTING VARIABLES INTO A TEXT FILE:

print('\nMaximum sepal length of all Iris species is ', maximum, file=open(output_textfile,"a"))          # \n - new line reference: https://wtmatter.com/python-new-line/  
print('Average sepal length of all Iris species is ', round(average,1), file=open(output_textfile,"a"))  # rounding to 1 decimal function - round(my_float,1)  reference:  https://tutorialdeep.com/knowhow/round-float-to-2-decimal-places-python/  


SCATTERPLOTS AND HISTOGRAMS 
Scatterplots and histograms can be best represented with Seaborn.
Seaborn is a library for making statistical graphics in Python. It is built on top of matplotlib and closely integrated with pandas data structures.
 It has options for visualizing univariate or bivariate distributions and for comparing them between subsets of data.
Scatterplots represent joint relationships, but histograms - univariate distributions.
Behind the scenes, seaborn uses matplotlib to draw plots. Many tasks can be accomplished with only seaborn functions, but further customization might require using matplotlib directly.

To run Seaborn and matplotlib in Python:
import matplotlib.pyplot as plt
import seaborn as sns

--------------------------------------------------------------

Scatterplot

# References https://www.youtube.com/watch?v=GcXcSZ0gQps, https://web.microsoftstream.com/video/025ef713-d7c8-492f-97f4-5590015da029?referrer=https:%2F%2Flearnonline.gmit.ie%2Fcourse%2Fview.php%3Fid%3D1598
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("Iris.csv")
sns.set(style = 'whitegrid')                                                         # color of the background grid
sns.scatterplot(x = 'Sepal_length', y = 'Sepal_width', data = df,hue = 'Species')
plt.title('Comparison of sepal length against sepal width')
plt.show()


df = pd.read_csv("Iris.csv")
sns.set(style = 'whitegrid')                                                         # color of the background grid
sns.scatterplot(x = 'Petal_length', y = 'Petal_width', data = df,hue = 'Species')
plt.title('Comparison of petal length against petal width')
plt.show()

df = pd.read_csv("Iris.csv")
sns.set(style = 'whitegrid')                                                         # color of the background grid
sns.scatterplot(x = 'Sepal_length', y = 'Petal_length', data = df,hue = 'Species')
plt.title('Comparison of sepal length against petal length')
plt.show()

df = pd.read_csv("Iris.csv")
sns.set(style = 'whitegrid')                                                         # color of the background grid
sns.scatterplot(x = 'Sepal_length', y = 'Petal_width', data = df,hue = 'Species')
plt.title('Comparison of sepal length against petal width')
plt.show()

df = pd.read_csv("Iris.csv")
sns.set(style = 'whitegrid')                                                         # color of the background grid
sns.scatterplot(x = 'Sepal_width', y = 'Petal_length', data = df,hue = 'Species')
plt.title('Comparison of sepal width against petal length')
plt.show()

df = pd.read_csv("Iris.csv")
sns.set(style = 'whitegrid')                                                         # color of the background grid
sns.scatterplot(x = 'Sepal_width', y = 'Petal_width', data = df,hue = 'Species')
plt.title('Comparison of sepal width against Petal width')
plt.show()

Pairplot

sns.pairplot(df, hue  ='Species')
plt.show()
