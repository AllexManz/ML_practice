import pandas as pd
import numpy as np


np_array = np.array(list(range(10)))
s = pd.Series(data=np_array, index=list('abcdefghij'))
print(s, end='\n-----------------\n')

'''
Со структурой данных Series работают все методы списков:
1. Можно обращаться по номеру
2. Можно обращаться по ключу
3. Работают срезы
4. Работают условные выражения
5. Работают lambda функции
'''

print(s['a'], end='\n-----------------\n')

print(s[0], end='\n-----------------\n')

print(s[:5], end='\n-----------------\n')

print(s[s <= 5], end='\n-----------------\n')

print(s[lambda x: x <= 5], end='\n-----------------\n')

'''
Элементы внутри Series модно умножить на одно число
Также можно сложить их с другим экземпляром Series
'''
s1 = pd.Series(data=range(10))
s2 = pd.Series(data=range(35, 45))

print(s1 * 4, end='\n-----------------\n')

print(s1 + s2, end='\n-----------------\n')

'''
Существует возможность обращаться к данным через атрибуты Series
'''

s3 = pd.Series(data=list(range(10)), index=list('abcdefghij'))

print(s3, end='\n-----------------\n')

print(s3.b, end='\n-----------------\n')

'''
Существует возможность получить случайный набор данных из уже существующего экземпляра Series
Параметры:
1. n количество объектов получаемых из Series
2. frac отвечает за возможность выбрать часть от общего числа
3. weights массив отвечает за вероятность выпадения каждого элемента
'''

print(s3.sample(n=4), end='\n-----------------\n')

print(s3.sample(frac=0.3), end='\n-----------------\n')

w = list(np.arange(0.1, 1.1, 0.1))
print(s3.sample(n=3, weights=w), end='\n-----------------\n')

