# Задача-1
# У вас есть список(list) IP адрессов. Вам необходимо создать
# класс который будет иметь методы:
# 1) Получить список IP адресов
# 2) Получить список IP адресов в развернутом виде
# (10.11.12.13 -> 13.12.11.10)
# 3) Получить список IP адресов без первых октетов
# (10.11.12.13 -> 11.12.13)
# 4) Получить список последних октетов IP адресов
# (10.11.12.13 -> 13)
#

class IpAdres:
    lis_ip = ['06.07.08.09', '10.11.12.13', '14.15.16.17']

    def __init__(self, lis_ip, reverse_lis_start, reverse_lis_end):
        self.l_ip = lis_ip
        self.reverse_lis_start = reverse_lis_start
        self.reverse_lis_end = reverse_lis_end

    def reverse_ip(self, lis_ip):
        """Takes in a list and uses two list to expand the content."""
        reverse_lis_start = []
        reverse_lis_end = []
        for ip in lis_ip:
            reverse_lis_start = ip.split('.')
            reverse_lis_start = reverse_lis_start[::-1]
            reverse_lis_end.append('.'.join(reverse_lis_start))

        return reverse_lis_end

    def non_first_oktet(self, lis_ip):
        """For some reason I fell in love with lists"""
        reverse_lis_start = []
        reverse_lis_end = []
        for ip in lis_ip:
            reverse_lis_start = ip.split('.')
            reverse_lis_start = reverse_lis_start[1:]
            reverse_lis_end.append('.'.join(reverse_lis_start))
        print(reverse_lis_end)

    def last_oktet(self, lis_ip):
        """Yes, yes, yes, again lists. I'm sure this can be done more beautifully"""
        reverse_lis_start = []
        reverse_lis_end = []
        for ip in lis_ip:
            reverse_lis_start = ip.split('.')
            reverse_lis_start = reverse_lis_start[-1:]
            reverse_lis_end.append('.'.join(reverse_lis_start))
        print(reverse_lis_end)


# lis_ip = ['06.07.08.09', '10.11.12.13', '14.15.16.17']

# def reverse_ip(primordial_lis):
#     reverse_lis_start = []
#     reverse_lis_end = []
#     for ip in primordial_lis:
#         reverse_lis_start = ip.split('.')
#         reverse_lis_start = reverse_lis_start[::-1]
#         reverse_lis_end.append('.'.join(reverse_lis_start))
#
#     return reverse_lis_end
# reverse_ip(lis_ip)

# def non_first_oktet(primordial_lis):
#     reverse_lis_start = []
#     reverse_lis_end = []
#     for ip in primordial_lis:
#         reverse_lis_start = ip.split('.')
#         reverse_lis_start = reverse_lis_start[1:]
#         reverse_lis_end.append('.'.join(reverse_lis_start))
#     print(reverse_lis_end)
# non_first_oktet(lis_ip)

# def last_oktet(primordial_lis):
#     reverse_lis_start = []
#     reverse_lis_end = []
#     for ip in primordial_lis:
#         reverse_lis_start = ip.split('.')
#         reverse_lis_start = reverse_lis_start[-1:]
#         reverse_lis_end.append('.'.join(reverse_lis_start))
#     print(reverse_lis_end)
# last_oktet(lis_ip)

# Задача-2
# У вас несколько JSON файлов. В каждом из этих файлов есть
# произвольная структура данных. Вам необходимо написать
# класс который будет описывать работу с этими файлами, а
# именно:
# 1) Запись в файл
# 2) Чтение из файла
# 3) Объединение данных из файлов в новый файл
# 4) Получить путь относительный путь к файлу
# 5) Получить абсолютный путь к файлу
#
import json
import pprint
from pathlib import Path


class Json:
    some_data = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]

    def __init__(self, name_json, first_name_json, second_name_json, write_name_json, file_name):
        self.name_json = name_json
        self.first_name_json = first_name_json
        self.second_name_json = second_name_json
        self.write_name_json = write_name_json
        self.file_name = file_name

    def write_json(self, name_json):
        """Throws an error if initialized some_data under a class."""
        some_data = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
        with open(name_json, 'w') as json_file:
            json.dump(some_data, json_file, indent=2)

    write_json('example_json_result.json')

    def read_json(self, name_json):
        with open(name_json) as json_file:
            data = json.load(json_file)
            pprint.pprint(data)

    def union_json_files(self, first_name_json, second_name_json, write_name_json):
        with open(first_name_json) as first_json_file:
            data_first = json.load(first_json_file)

        with open(second_name_json) as second_json_file:
            data_second = json.load(second_json_file)

        data_second.update(data_first)
        """If you need to combine with key update."""
        with open(write_name_json, 'w') as write_json_file:
            json.dump(data_second, write_json_file, indent=2)

        """If it is necessary to add"""
        with open(write_name_json, 'a') as write_json_file:
            json.dump(data_first, write_json_file, indent=2)
            json.dump(data_second, write_json_file, indent=2)

    def absolute_path(self, file_name):
        file_absolute = Path.home()
        print(file_absolute)


# some_data = [{'a': 1, 'b': 2},{'c': 3, 'd': 4},{'e': 5, 'f': 6}]
# def write_json(name_json):
#     with open(name_json, 'w') as json_file:
#         json.dump(some_data, json_file, indent=2)
# write_json('example_json_result.json')
#
# def read_json(name_json):
#     with open(name_json) as json_file:
#         data = json.load(json_file)
#         pprint.pprint(data)

#
# def union_json_files(first_name_json, second_name_json, write_name_json):
#     with open(first_name_json) as first_json_file:
#         data_first = json.load(first_json_file)
#
#     with open(second_name_json) as second_json_file:
#         data_second = json.load(second_json_file)
#
#     data_second.update(data_first)
#     """If you need to combine with key update."""
#     with open(write_name_json, 'w') as write_json_file:
#         json.dump(data_second, write_json_file, indent=2)
#
#     """If it is necessary to add"""
#     with open(write_name_json, 'a') as write_json_file:
#         json.dump(data_first, write_json_file, indent=2)
#         json.dump(data_second, write_json_file, indent=2)

# union_json_files('example_json_1.json', 'example_json_2.json', 'example_json_result.json')

# """I tried to read through pathlib, but did not fully understand how to work with it."""
# from pathlib import Path

# def absolute_path(file_name):
#     file_absolute = Path.home()
#     print(file_absolute)
# absolute_path('example_json_1.json')


# Задача-3
#
# Создайте класс который будет хранить параметры для
# подключения к физическому юниту(например switch). В своем
# списке атрибутов он должен иметь минимальный набор
# (unit_name, mac_address, ip_address, login, password).
# Вы должны описать каждый из этих атрибутов в виде гетеров и
# сеттеров(@property). У вас должна быть возможность
# получения и назначения этих атрибутов в классе.


class Switch:

    def __init__(self, unit_name, mac_address, ip_address, login, password):
        self.__unit_name = unit_name
        self.__mac_address = mac_address
        self.__ip_address = ip_address
        self.__login = login
        self.__password = password

    @property
    def unit_name(self):
        return self.__unit_name

    @unit_name.setter
    def unit_name(self, name):
        rus_letter = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        """When initialized under a class, it gave an error"""
        if rus_letter.isdisjoint(name.lower):
            self.__unit_name = name
        else:
            print('The name must be written in Latin')

    @property
    def mac_address(self):
        return self.__mac_address

    @mac_address.setter
    def mac_address(self, mac):
        unacceptable = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюяqwertyuiopasdfghjklzxcvbnm')
        if unacceptable.isdisjoint(mac.lower):
            self.__mac_address = mac
        else:
            print('Unacceptable, must be numbers')

    @property
    def ip_address(self):
        return self.__ip_address

    @ip_address.setter
    def ip_address(self, ip):
        unacceptable = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюяqwertyuiopasdfghjklzxcvbnm')
        if unacceptable.isdisjoint(ip.lower):
            self.__ip_address = ip
        else:
            print('Unacceptable, must be numbers')

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, new_login):
        if new_login.isalpha():
            self.__login = new_login
        else:
            print('Unacceptable, must be a letter')

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_pas):
        """I know that it would be possible, something more interesting to come up with"""
        if new_pas.isspace():
            self.__password = new_pas
        else:
            print('You shall not pass!')