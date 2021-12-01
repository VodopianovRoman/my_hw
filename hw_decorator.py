# ЗАДАЧА-1
# Написать свой декоратор который будет проверять остаток от деления числа 100 на результат
# работы функции ниже.
# Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys,
# we got {}» остаток от деления.
import functools


# def decorator_remainder_of_division(func):
#     @functools.wraps(func)
#     def wraper(*args, **kwargs):
#         res = 1
#         for i in args:
#             res *= i
#         res_remainder = 100 % res
#         if res_remainder == 0:
#             print('We are OK!')
#         else:
#             print(f'Bad news guys,we got {res_remainder}')
#     return wraper
#
#
#
# @decorator_remainder_of_division
# def multiplication(int_one, int_two):
#     return int_one * int_two

# def decorator_remainder_of_division(func):
#     @functools.wraps(func)
#     def wraper(*args, **kwargs):
#         res = 100 % func(*args, **kwargs)
#         if not res:
#             print('We are OK!')
#         else:
#             print(f'Bad news guys,we got {res}')
#     return wraper
#
# @decorator_remainder_of_division
# def multiplication(int_one, int_two):
#     """the function takes two numbers (int) and multiplies them."""
#     return int_one * int_two
#
# multiplication(2, 5)


# ЗАДАЧА-2
# Написать декоратор который будет выполнять предпроверку типа аргумента который
# передается в вашу функцию.
# Если это int, тогда выполнить функцию и вывести результат, если это str(),
# тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))

# def decorator_check_for_number(func):
#     @functools.wraps(func)
#     def wraper(*args):
#         for i in args:
#             if isinstance(i, int):
#                 func(i)
#             elif isinstance(i, str):
#                 raise ValueError('string type is not supported')
#
#     return wraper
#
#
# @decorator_check_for_number
# def number_function(int_arg):
#     """The function accepts a number for mathematical operation. Just for example."""
#     print((int_arg * 100) / 20)
#
#
# number_function(20)

# ЗАДАЧА-3
# Написать декоратор который будет кешировать значения аргументов и результаты работы
# вашей функции и записывать
# его в переменную cache. Если аргумента нет в переменной cache и функция выполняется,
# вывести сообщение
# «Function executed with counter = {}, function result = {}» и количество раз сколько
# эта функция выполнялась.
# Если значение берется из переменной cache, вывести сообщение
# «Used cache with counter = {}» и
# количество раз обращений в cache.

# def decorator_multi(func):
#     cache = {}
#     @functools.wraps(func)
#     def wrap(*args):
#         if args in cache:
#             wrap.ccalls += 1
#             print(f'Used cache with counter = {wrap.ccalls}')
#             return cache[args]
#         else:
#             wrap.ncalls += 1
#             cache[args] = func(*args)
#             print(f'Function executed with counter = {wrap.ncalls}, function result = {cache[args]}')
#             return cache[args]
#
#     wrap.ccalls = 0
#     wrap.ncalls = 0
#     return wrap
#
#
# @decorator_multi
# def multi_bulti(int_n):
#     """The name of the function speaks for itself.
# Takes an argument as a number and raises it to the power of the accepted argument."""
#     print(f'this passed to func call {multi_bulti.ncalls}')
#     return int_n ** int_n
#
# multi_bulti(5)



# def decorator_fib(func):
#     cache = {}
#
#     @functools.wraps(func)
#     def wrap(*args):
#         if args in cache:
#             wrap.ccalls += 1
#             print(f'Used cache with counter = {wrap.ccalls}')
#             return cache[args]
#         else:
#             cache[args] = func(*args)
#             wrap.ncalls += 1
#             print(f'Function executed with counter = {wrap.ncalls}, function result = {cache[args]}')
#             return cache[args]
#
#     wrap.ccalls = 0
#     wrap.ncalls = 0
#     return wrap
#
#
# @decorator_fib
# def fib(n):
#     """Wacky example for finding the fibonacci number"""
#     if n < 2:
#         return n
#     return fib(n-2) + fib(n-1)
#
# print('fib(20) =', fib(20))



# ======================Практика=========================================================

# import time
#
# def decorator_time_name_result(func):
#     """The decorator shows the runtime and the name and result of the func being received and
#     writes the data to file log.txt"""
#     @functools.wraps(func)
#
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(f'Результат - {func(*args, **kwargs)}')
#         print(f'Имя функции - {func.__name__}')
#         print(f'Время работы - {end-start}')
#         all_res = f'Результат - {func(*args, **kwargs)} Имя функции - {func.__name__} Время работы - {end-start}'
#         with open('log.txt', 'w', encoding='utf-8') as file:
#             file.write(all_res)
#
#     return wrapper
#
# @decorator_time_name_result
# def my_func(a):
#     """Return 'a'. 'a' is int"""
#     return a
#
# my_func(10)

# def use_cache(func):
#     cache = {}
#
#     @functools.wraps(func)
#     def wrapper(*args):
#         if args in cache:
#             wrapper.cache_calls += 1
#             print(f"wrapper.cache_calls = {wrapper.cache_calls}")
#             return cache[args]
#         else:
#             wrapper.function_calls += 1
#             cache[args] = func(*args)
#             print(f"wrapper.function_calls = {wrapper.function_calls}, function_result = {cache[args]}")
#             return cache[args]
#
#     wrapper.function_calls = 0
#     wrapper.cache_calls = 0
#     return wrapper
#
# @use_cache
# def any_func(a ,b):
#     print(f'this passed to func call {any_func.function_calls}')
#     return a * b

# any_func(1,2)
# any_func(1,2)
# any_func(1,2)
# any_func(2,2)