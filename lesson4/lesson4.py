# class MyException(Exception):
#     print('my exception')
#
#
# try:
#     print(10 / 0)
#     raise MyException
# except ZeroDivisionError:
#     print('division by zero')
# except Exception as e:
#     print(e)
# finally:
#     print('finally')


# generator
# def gen(n):
#     for i in range(n):
#         yield i
#
#
# g = gen(5)
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def gen(n: int, team_name: str) -> None:
#     for i in range(n):
#         yield f'Person {i + 1} from {team_name} team.'
#
#
# def schedule(teams: list) -> None:
#     while teams:
#         team_generator = teams.pop(0)
#         try:
#             print(next(team_generator))
#             teams.append(team_generator)
#         except StopIteration:
#             pass
#
#
# teams = [gen(5, 'Erudite'), gen(7, 'Zoro')]
# schedule(teams)


# # generator name of file
# import uuid
# from typing import Generator
#
# '''
# Generator[str, None, None] вказує, що цей генератор повертає значення типу str,
# не приймає жодних значень для send() і не повертає жодних значень (тобто повертає None) при завершенні.'''
#
#
# def generator_name_of_file(ext: str) -> Generator[str, None, None]:
#     __counter = 0
#     while True:
#         __counter += 1
#         yield f'{uuid.uuid4()}-{__counter}.{ext}'
#
#
# gen_name_images = generator_name_of_file('jepg')
# print(next(gen_name_images))
# print(next(gen_name_images))
# print(next(gen_name_images))

# # context_manager
# try:
#     with open('lesson4.txt', 'r') as file:
#         print(file.read())
# except Exception as error:
#     print(error)

# # відкриття та запис бінарних данних: в даному випадку робим копію
# try:
#     with open('lw4.png', 'rb') as file:
#         with open('lesson4a.png', 'wb') as file2:
#             file2.write(file.read())
#
# except Exception as err:
#     print(err)

import json
import pickle

# user = {'name': 'Max', 'age': 25}


# try:
#     with open('my_user.data', 'wb') as file:
#         pickle.dump(user, file)
# except Exception as err:
#     print(err)
# try:
#     with open('my_user.data', 'rb') as file:
#         user = pickle.load(file)
#         print(user)
# except Exception as err:
#     print(err)

# try:
#     with open('my_user.json', 'w') as file:
#         json.dump(user, file)
# except Exception as err:
#     print(err)
#
# try:
#     with open('my_user.json', 'r') as file:
#         user = json.load(file)
#         print(user)
# except Exception as err:
#     print(err)

################################################
# # match
# action1 = ['left', 200]
#
# match action1:
#     case 'left' | 'top' as action, value:
#         print(action, value)
#     case _:
#         print('not found')
#
# u1 = ['Ivan', 26, True]
# match u1:
#     case 'Ivan' | 'Stepan' as name, a, True as s:
#         print(name, a, s)
#     case _:
#         print('NTF')
#
# action2 = ['rightt', 200]
# match action2:
#     case ['right' | 'left', value]:
#         print(action2)
#     case _:
#         print('not found')
#
# user0 = {'name': 'Max', 'age': 25}
# match user0:
#     case {'name': str(name), 'age': int(age)}:
#         print(f'name = {name}, age = {age}')
#     case _:
#         print('NF')
#
# user2 = {'name': 'Maxx', 'age': 25}
# match user2:
#     case {'name': 'Max' as name, 'age': int(age)}:
#         print(f'name = {name}, age = {age}')
#     case _:
#         print('NF')

# match into class
from typing import TypedDict

UserType = TypedDict('UserType', {'name': str, 'age': int})


class User:
    __match_args__ = 'name', 'age'

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Maxx', 25)
user2: UserType = {'name': 'Ivan', 'age': 27}


def matcher(data: User | dict):
    match data:
        case User('Max' as name):
            print(name)
        case {'name': str(name)}:
            print(name)
        case _:
            print('Nf')


matcher(user)
matcher(user2)
