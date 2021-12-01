# Задача-1
# Создать объект менеджера контекста который будет переходить в
# папку которую он принимает на вход. Так же ваш объект должен принимать
# исключение которое он будет подавлять Если флаг об исключении
# отсутствует, исключение должно быть поднято.
import os
import sys
import contextlib
import time
from contextlib import suppress


class OpenFolder:
    """This context manager takes the path to the folder and the name of the error.
    In the __init__ block, we save our current file location.
    The folder is opened in the __enter__ blocks, here the error is suppressed using the construction
try except, if an error occurs, we enter the message and remain at the current location.
    In the __exit__ block, the saved location is closed."""

    def __init__(self, path, *exception):
        self.path = path
        self.exception = exception
        """We save the current path so that we can close it later."""
        self.saved_cwd = os.getcwd()

    def __enter__(self):
        try:
            time.sleep(5)  # To test 3 tasks
            os.chdir(self.path)  # Trying to take a new path.
        except self.exception:
            print('Ooops, something went wrong')

        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.saved_cwd)  # Closing the old path


#
# with OpenFolder(r'C:\users', FileNotFoundError):
#     print(os.getcwd())

# Задача -2
# Описать задачу выше но уже с использованием @contexmanager

@contextlib.contextmanager
def open_folder(path):
    """With the help of this decorator of the context manager, we get the path to the folder and
    go to it using the construction try/except.
        We keep our current location.
        In the final implementation, when invoked using visas, we use the suppres tool
    from the contextLib.
        Since without it, when specifying a non-existent path, the yield is swearing."""
    now_cwd = os.getcwd()
    try:
        os.chdir(path)
        yield
    except:
        print('Exception caught: ', sys.exc_info()[0])
    finally:
        os.chdir(path)


# with suppress(FileNotFoundError):
# with open_folder(r'C:\Users'):
#     print(os.getcwd())

# Задача -3
# Создать менеджер контекста который будет подсчитывать время выполнения вашей функции

class CountOfFunc:
    """With the help of this context manager, we can calculate the execution time of the
    required function or context manager.
        In the variable time.start, we will remember the current time.
        In the __enter__ block, in try we start the countdown.
        In the __exit__ block, we display the time that was spent."""

    def __enter__(self):
        try:
            # self.context_manager
            self.time_start = time.time()
            # time.sleep(15)
        except:
            print('Ooops, something went wrong')

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.context_manager
        self.time_stop = time.time()
        print(f'Time spent on the function: {self.time_stop - self.time_start}')


# with CountOfFunc():
#     with OpenFolder(r'C:\Users',FileNotFoundError):
#         print(os.getcwd())

@contextlib.contextmanager
def open_new_folder(path, *exception):
    now_cwd = os.getcwd()

    try:
        os.chdir(path)
    except exception:
        os.chdir(now_cwd)
        print('exception catch')
    yield


# with open_new_folder(r'C:\asd', FileNotFoundError):
#     print(os.getcwd())


def open_new_folder1(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print('exception catch')


# f = open_new_folder1(r'C:\weq')
# print(os.getcwd())


# ===========ПРАКТИКА==============
# import requests

# class UrlOpen():
#
#     def __init__(self, url, exception=None):
#         self.url = url
#         self.exception = exception or Exception
#
#     def __enter__(self):
#         try:
#             self.req = requests.get(self.url, timeout=2)
#         except self.exception:
#             raise self.exception('Exception catch')
#         return self.req.text
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass
#
#
# with UrlOpen(r'https:\\www.google.com',requests.exceptions.ConnectionError) as page_text:
#     with open('page.html', 'w') as file:
#         file.write(page_text)


# ==================Classes=======================

class Player:
    instance_count = 0


    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        Player.instance_count += 1
        self.team = None

    def get_name(self):
        return self.name

    def get_age(self):
        print(f'{self.name} age is {self.age}')

    def get_height(self):
        print(f'{self.name} height is {self.height}')

    def get_weight(self):
        print(f'{self.name} weight is {self.weight}')

    def get_instance_count(self):
        print(f'instance_count - {Player.instance_count}')

    def get_player_team(self, name):
        if name == self.name:
            print(self.team)


class Team:

    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_players(self, player):
        if isinstance(player, Player):
            self.players.append(player)
            player.team = self.team_name #в классе Player записываем наименование команды для данного игрока
            print(f'Player - {player.name}, was added to team - "{self.team_name}"  ')
        else:
            raise NameError

    def get_team_players(self):
        print(f'Team: "{self.team_name}"; Players: {[player.name for player in self.players]}')



player1 = Player('Vasya', 18, 180, 75)
player1.get_height()
player1.get_name()
player2 = Player('Gnom', 22, 190, 95)
player2.get_height()
player2.get_instance_count()


team1 = Team('Chyhani')
team1.add_players(player1)
team1.add_players(player2)
player1.get_player_team('Vasya')
team1.get_team_players()