# A screenshot of the output you obtained by executing the python program
import pandas as pd
import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(url)
print("Original Iris dataset:")
iris.head()

iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
print("\nColumn names:")
print(iris.columns)

print("\nMissing values in each column:")
print(iris.isnull().sum())
print("\nAre there any missing values?")
print(iris.isnull().values.any())

iris.loc[10:29, 'petal_length'] = np.nan
# iris.iloc[10:30, 2] = np.nan

print("\nMissing values after inserting NaN:")
print(iris.isnull().sum())
# iris.isnull().sum().sum()

iris.fillna(10.0, inplace=True)
print("\nMissing values after fillna:")
print(iris.isnull().sum())

print("\nUpdated Iris dataset:")
print(iris.head(35))

