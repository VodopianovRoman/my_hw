import time
from functools import wraps

# Задача-1
# У вас есть файл из нескольких строк. Нужно создать генератор который будет построчно выводить строки из вашего файла.
# При вызове итерировании по генератору необходимо проверять строки на уникальность.
# Если строка уникальна, тогда ее выводим на экран, если нет - скипаем

def uniq_line(file_name, uniq = None):
    uniq = set(uniq or [])
    with open(file_name, 'r') as file:
        for line in file:
            line = line.replace('\n', '')
            if line not in uniq:
                uniq.add(line)
                print(line)
                yield line
        print(uniq)

# file1 = uniq_line('demo.txt')
# next(file1)
# next(file1)
# next(file1)
# next(file1)
# next(file1)
# print(list(file1))

# Задача-2 (оригинальный вариант и его делать не обязательно):
# представим есть файл с логами, его нужно бессконечно контролировать
# на предмет возникнования заданных сигнатур.
#
# Необходимо реализовать пайплайн из корутин, который подключается к существующему файлу
# по принципу команды tail, переключается в самый конец файла и с этого момента начинает следить
# за его наполнением, и в случае возникнования запиcей, сигнатуры которых мы отслеживаем -
# печатать результат
#
# Архитектура пайплайна

#                    --------
#                   /- grep -\
# dispenser(file) <- - grep - -> pprint
#                   \- grep -/
#                    --------

# Структура пайплайна:
# ```
def coroutine(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        cor = func(*args, **kwargs)
        # cor.send(None)
        next(cor)
        return cor

    return wrap


@coroutine
def grep(pattern, target):
    while True:
        line = yield
        if pattern in line:
            target.send(line)


@coroutine
def printer():
    while True:
        line = yield
        print(line)


@coroutine
def dispenser(*args):
    line = yield
    for target in args:
        target.send(line)




def follow(file, target):
    file.seek(0, 2)  # Go to the end of the file
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)  # Sleep briefly
            continue
        target.send(line)
# ```
#
# Каждый grep следит за определенной сигнатурой
#
# Как это будет работать:
#
# ```
# f_open = open('log.txt') # подключаемся к файлу
# follow(f_open,
#        # делегируем ивенты
#        dispenser([
#            grep('python', printer()), # отслеживаем
#            grep('is', printer()),     # заданные
#            grep('great', printer()),  # сигнатуры
#        ])
#        )
# ```
# Как только в файл запишется что-то содержащее ('python', 'is', 'great') мы сможем это увидеть
#
# Итоговая реализация фактически будет асинхронным ивент хендлером, с отсутствием блокирующих операций.
#
# Если все плохо - план Б лекция Дэвида Бизли
# [warning] решение там тоже есть :)
# https://www.dabeaz.com/coroutines/Coroutines.pdf


#Задача-3 (упрощенный вариант делаете его если задача 2 показалась сложной)
# Вам нужно создать pipeline (конвеер, подобие pipeline в unix https://en.wikipedia.org/wiki/Pipeline_(Unix)).
#
# Схема пайплайна :
# source ---send()--->coroutine1------send()---->coroutine2----send()------>sink
#
# Все что вам нужно сделать это выводить сообщение о том что было получено на каждом шаге и обработку ошибки GeneratorExit.
#
# Например: Ваш source (это не корутина, не генератор и прочее, это просто функция ) в ней опеделите цикл из 10 элементов
# которые будут по цепочке отправлены в каждый из корутин и в каждом из корутин вызвано сообщение о полученном элементе.
# После вызова .close() вы должны в каждом из корутин вывести сообщение что работа завершена.

@coroutine
def source():
    cr = coroutine1(target=coroutine2(target=sink()))
    for elem in range(3):
        cr.send(elem)
        yield elem

@coroutine
def coroutine1(target):
    try:
        while True:
            elem = yield
            print(f'Received value: {elem}')
            target.send(elem)
    except GeneratorExit:
        print('Coroutine is close')

@coroutine
def coroutine2(target):
    try:
        while True:
            elem = yield
            print(f'Received value: {elem}')
            target.send(elem)
    except GeneratorExit:
        print('Coroutine is close')

@coroutine
def sink():
    elem_lis = []
    try:
        while True:
            elem = yield
            elem_lis.append(elem)
    except GeneratorExit:
        print(f'Result {elem_lis}')
        print('Coroutine is close')

# sor = source()
# next(sor)
# next(sor)

#======================================Pracrice=========================================

# class FibonacciIter:
#
#     def __init__(self):
#         self.prev, self.cur = 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.res = self.prev
#         self.prev, self.cur = self.cur, self.prev + self.cur
#         return self.res

# for i in FibonacciIter():
#     print(i)
#     if i > 100:
#         break

# def fibonaci_iter():
#     prev, cur = 0, 1
#     while True:
#         yield prev
#         prev, cur = cur, cur + prev

# for i in fibonaci_iter():
#     print(i)
#     if i > 100:
#         break

# def gen_counter():
#     start_val = 0
#     step_val = 1
#     while True:
#         new_start = yield start_val
#         if new_start is None:
#             start_val += step_val
#             print(start_val)
#         else:
#             start_val = new_start
#
#
# count = gen_counter()
# next(count)
# count.send(200)
# next(count)
# next(count)
# next(count)
# next(count)


# def count(firstval=0, step=1):
#     counter = firstval
#     while True:
#         new_counter_val = yield counter
#         if new_counter_val is None:
#             counter += step
#         else:
#             counter = new_counter_val


# start_value = 2.1
# step_value = 0.3
# counter = count(start_value, step_value)
# for i in range(10):
#     new_value = next(counter)
#     print(f"{new_value:2.2f}", end=", ")
#
# print("set current count value to another value:")
# counter.send(100.5)
# for i in range(10):
#     new_value = next(counter)
#     print(f"{new_value:2.2f}", end=", ")