import pandas as pd


'''
DataFrame - двумерная структура данных в pandas
DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
Может быть сделан из:
1. dict (в качестве которого могут выступать ndarray, list, Series и dict)
2. Series
3. двумерный ndarray
4. другой DataFrame
'''

d = {'price': pd.Series(data=[1, 2, 3], index=['a', 'b', 'c']), 'cnt': pd.Series(data=[5, 7, 8], index=['a', 'b', 'c'])}
df1 = pd.DataFrame(d)
print(df1, end='\n-----------------\n')

'''
При выводе можно отдельно указать вывод названий всех колонок и строк
'''

print(*df1.index, end='\n-----------------\n')

print(*df1.columns, end='\n-----------------\n')
