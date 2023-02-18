from sklearn.datasets import fetch_california_housing
from impyute.imputation.cs import fast_knn
from impyute.imputation.cs import mice
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
from math import sqrt
import pandas as pd
import numpy as np
import random
import sys


random.seed(0)
sys.setrecursionlimit(10000)


# Fetching the Dataset
dataset = fetch_california_housing()
train, target = pd.DataFrame(dataset.data), pd.DataFrame(dataset.target)
train.columns = [str(i) for i in range(8)]
train.insert(loc=len(train.columns), column='target', value=target)

# Randomly replace 40% of the first column with Nan values
column = train['0']
missing_pct = int(column.size * 0.4)
i = [random.choice(range(column.shape[0])) for _ in range(missing_pct)]
column[i] = np.NaN
print(train)

# Impute the values using scikit-learn SimpleImpute Class, mean strategy
imp_mean1 = SimpleImputer(strategy='mean')
imp_mean1.fit(train)
imputed_train_df1 = imp_mean1.transform(train)
print("Mean Strategy")
print(pd.DataFrame(imputed_train_df1))

# Impute the values using scikit-learn SimpleImpute Class, most-frequent strategy
imp_mean2 = SimpleImputer(strategy='most_frequent')
imp_mean2.fit(train)
imputed_train_df2 = imp_mean2.transform(train)
print("most_frequent Strategy")
print(pd.DataFrame(imputed_train_df2))

# Impute the values using kNN algorithms | works with numpy version < 1.24
# imputed_train_df3 = fast_knn(train.values, k=30)

# Impute the values using MICE algorithms | works with numpy version < 1.24
# imputed_train_df4 = mice(train.values)

