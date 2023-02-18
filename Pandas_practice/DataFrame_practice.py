import pandas as pd
import numpy as np

d = {'price': np.array([1, 2, 3]), 'cnt': np.array([4, 5, 6])}
df1 = pd.DataFrame(d, index=['v1', 'v2', 'v3'])
# print(df1, end='\n-----------------\n')

'''
Существует функция info, которая позволяет получить информацию об отдельном экземпляре DataFrame:
1. Название колонок и рядов
2. Количество записей
3. Количество non-null элементов
4. Типы и количество хранимых элементов
5. Общий объём занятой памяти
'''

d = [{'price': 1, 'cnt': 4}, {'price': 2, 'cnt': 5}, {'price': 3, 'cnt': 6}]
df2 = pd.DataFrame(data=d, index=['v1', 'v2', 'v3'])
# print(df2, end='\n-----------------\n')
# print(df2.info())

d = np.array([[1, 2, 3], [4, 5, 6]])
df3 = pd.DataFrame(d)
# print(df3, end='\n-----------------\n')

'''
Операция                               Синтаксис           Возвращаемый результат
Выбор столбца                          df[col]             Series
Выбор строки по метке                  df.loc[label]       Series
Выбор строки по индексу                df.iloc[loc]        Series
Срез по строкам                        df[0:4]             DataFrame
Выбор строк, отвечающих условию        df[bool_vec]        DataFrame
Выбор строк lambda функцией            df[lambda x: ]      DataFrame
'''

d = {'price': np.array([1, 2, 3]), 'list': np.array([4, 5, 6])}
df4 = pd.DataFrame(d, index=['a', 'b', 'c'])

# print(df4, end='\n-----------------\n')

# print(df4['price'], end='\n-----------------\n')

# print(df4.loc['a'], end='\n-----------------\n')

# print(df4.loc['a']['price'], end='\n-----------------\n')

# print(df4.iloc[1], end='\n-----------------\n')

# print(df4[0:2], end='\n-----------------\n')

# print(df4[df4['list'] <= 5], end='\n-----------------\n')

# print(df4[lambda x: x["price"] <= 2], end='\n-----------------\n')

'''
Существует возможность обращаться к данным через атрибуты DataFrame
'''

d = {'price': [10, 20, 30], 'discount': [15, 25, 50]}
df5 = pd.DataFrame(data=d, index=['a', 'b', 'c'])

print(df5, end='\n-----------------\n')

print(df5.price, end='\n-----------------\n')

'''
Существует возможность получить случайный набор данных из уже существующего экземпляра DataFrame
Параметры:
1. n количество объектов получаемых из DataFrame
2. frac отвечает за возможность выбрать часть от общего числа
3. weights массив отвечает за вероятность выпадения каждого элемента
4. axis позволяет выбрать ось
'''

# print(df5.sample(n=2), end='\n-----------------\n')

# print(df5.sample(frac=0.5), end='\n-----------------\n')

w = list(np.arange(0.3, 1, 0.3))
# print(df5.sample(n=2, weights=w), end='\n-----------------\n')

# print(df5.sample(axis=1), end='\n-----------------\n')

# print(df5.sample(n=2, axis=1), end='\n-----------------\n')

# print(df5.sample(axis=1, n=1, weights=[0.1, 0.7]), end='\n-----------------\n')
