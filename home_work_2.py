# 1) Сгенерировать dict() из списка ключей ниже по формуле (key : key* key).
# keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  ожидаемый результат: {1: 1, 2: 4, 3: 9 …} 

# a = {i:i*i for i in keys}
# print(a)

# ========================================================================================
# 2) Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий
# массив только четные числа. 

# a = {i for i in range(1,100) if i%2 == 0}
# print(a)

# =============================================================================================
# 3)Заменить в произвольной строке согласные буквы на гласные.  
# import random
#
# a = ['a', 'e', 'i', 'o', 'u', 'y', 'а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ё', 'е']
#
#
# def noConsonant(st):
#     st.lower()
#     for i in st:
#         if i in 'bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ':
#             st = st.replace(i, random.choice(a))
#     return st
#
#
# print(noConsonant('qwertyаран'))


# =============================================================================================
# 4)Дан массив чисел. 
# a = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
# 4.1) убрать из него повторяющиеся элементы
# b = list(set(a[:]))
# print(b)
# 4.2) вывести 3 наибольших числа из исходного массива
# def maxDigit(a):
#     b=a[:3]
#     for i in a:
#         if i > b[0]:
#             b.pop(0)
#             b.append(i)
#             b.sort()
#     return b
#
# print(*maxDigit(a))

# 4.3) вывести индекс минимального элемента массива
# b = min(a)
# print(a.index(b))

# 4.4) вывести исходный массив в обратном порядке 
# print(a[::-1])

# 5) Найти общие ключи в двух словарях: 
# dict_one = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }
# dict_two = { 'a': 6, 'b': 7, 'z': 20, 'x': 40 }
#
# def coincidence(dict1, dict2):
#     _coincidence=[]
#     for key in dict1.keys():
#         if key in dict2:
#             _coincidence.append(key)
#     return _coincidence
#
# print(coincidence(dict_one,dict_two))


# 6)Дан массив из словарей 
# data = [
#     {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
#     {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
#     {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
#     {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
#     {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
#     {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

# 6.1) отсортировать массив из словарей по значению ключа ‘age' 

# from operator import itemgetter
# newlist = sorted(data, key=itemgetter('age'))
#
# print(newlist)

# 6.2) сгруппировать данные по значению ключа 'city' 
# вывод должен быть такого вида :

# result = {}
# for record in data:
#     city = record.pop('city')
#     if city in result:
#         result[city].append(record)
#     else:
#         result[city] = [record]
#
# print(result)

# result = {
#    'Kiev': [
#       {'name': 'Viktor', 'age': 30 },
#       {'name': 'Andrey', 'age': 34}],
#
#    'Dnepr': [ {'name': 'Maksim', 'age': 20 },
#               {'name': 'Artem', 'age': 50}],
#    'Lviv': [ {'name': 'Vladimir', 'age': 32 },
#              {'name': 'Dmitriy', 'age': 21}]
# }
# =======================================================
# 7) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку
# в последовательности.
# Например:

# def most_frequent(list_var):
#     a=''
#     count=1
#     for i in range(len(list_var)):
#         if list_var.count(list_var[i]) > count:
#             count = list_var.count(list_var[i])
#             a = list_var[i]
#     return a
#
# print(most_frequent(['a', 'a', 'bi', 'bi', 'bi', 'di', 'di', 'fa', 'fa', 'fa', 'fa']))
# =======================================================
# 8) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе,
# за исключением нулей.
# Например:
# Дано число 123405. Результат будет: 1*2*3*4*5=120.

# def sumOfnum(n):
#     n = str(n)
#     mult = 1
#     for i in n:
#         i = int(i)
#         if i>0:
#             mult*=i
#     print(mult)

# def sumOfnum(n):
#     mult = 1
#     while n > 0:
#         a = n % 10
#         if a > 0:
#             mult *= a
#         n = n // 10
#     print(mult)
#
#
# sumOfnum(123405)

# =======================================================
# 9) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива,
# тогда вернуть -1.
# def some_function(array, n):
#     if len(array) - 1< n:
#         return -1
#     power = array[n]**n
#     return power
#
# print(some_function([2,3,4,5],5))
# =======================================================
# 10) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или
# числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три
# слова подряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.

# def threeWords(st):
#     count=0
#     st = st.split()
#     for i in st:
#         if i.isalpha():
#             count+=1
#         elif i.isdigit():
#             count-=1
#     if count == 3:
#         print('Yes')
#     else:
#         print('No')
#
# threeWords('hello 1 one two three 15 world')
