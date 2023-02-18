import pandas as pd
import numpy as np

'''
Series - одномерная структура данных, список
Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
Может быть сделан из:
1. dict
2. list
3. ndarray (из библиотеки numpy array)
4. скалярная величина
'''

s1 = pd.Series(data=list(range(10)))
# print(s1)

s2 = pd.Series(data=list(range(10)), index=list('abcdefghij'))
# print(s2)

numpy_arr = np.array(list(range(10)))
s3 = pd.Series(data=numpy_arr, index=list('abcdefghij'))
# print(s3)

d = {'a': 1, 'b': 2, 'c': 3}
s4 = pd.Series(d)
# print(s4)

n = 3
s5 = pd.Series(data=n, index=range(10))
# print(s5)



