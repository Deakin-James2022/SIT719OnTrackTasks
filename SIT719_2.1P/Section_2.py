# Colab Command
# summarizes some key concepts and usages of important python libraries like ‘pandas’,’numpy’, ‘matplotlib’ you have learned in this week

import pandas as pd
import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris = pd.read_csv(url)

iris.head()

iris.columns = ['sepal_length','sepal_width','petal_length','petal_width','class']

iris.columns

iris.isnull().values.any()

iris.loc[10:29, 'petal_length'] = np.nan

iris.isnull().sum()

iris = iris.fillna(10.0)

iris.isnull().sum()
