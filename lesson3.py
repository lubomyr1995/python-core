# class User:
#     __slots__ = ('name', 'age', 'house')
#
#     def __init__(self, name, age, house):
#         self.name = name
#         self.age = age
#         self.house = house
#
#     def __str__(self):
#         return f'User(name={self.name}, age={self.age}, house={self.house})'
#
#     def __repr__(self):
#         # це працює якщо є __slots__: return f'{self.__dict__}'
#         return self.__str__()
#
#
# user = User('John', 21, 'Smith')
# print(user)


# # Інкапсуляція
# class User:
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#
# user = User('Max')
# print(user.name)
# user2 = User('Ivan')
# print(user2.name)
# user2.name = 'Pavlo'
# print(user2.name)
# del user2.name


# # # Polymorphism, Abstractions
# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
# # # shape = Shape() - в абстрактному методі не можна створити екземпляр класу, абстрактний метод гарантує що
# # # наслідники мають імплементувати його методи які продекоровані @abstractmethod
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def area(self):
#         return self.a * self.b * self.c / 3
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return self.a * self.b
#
#     def perimeter(self):
#         return 2 * (self.a + self.b)
#
#
# shapes: list[Shape] = [Triangle(1, 2, 3), Rectangle(4, 5), Rectangle(6, 7)]
# for i in shapes:
#     print('perimetr: ', i.perimeter())
#     print('area: ', i.area())
#
#
#
# # # staticmethod- не залежить від self, тобто не залежить від екземпляру класа
# # # classmethod - cls це посилання на імя класу
# class User:
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     @staticmethod
#     def greeting():
#         print('Hello')
#
#     @classmethod
#     def inc_count(cls):
#         cls.count += 1
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
#
# User.inc_count()
# User.inc_count()
# User.greeting()
# print(User.get_count())

# # Прегрузка методів
# # singleTone
# class User:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not isinstance(cls.__instance, cls):
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     # це означає що даний клас може мати максимум один екземпляр, або перевизначений
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return str(self.__dict__)
#
#
# user = User('Kokos', 20)
# user2 = User('Kokos', 21)
# user3 = object.__new__(User)
# user3.name = 'Roko'
# user3.age = 10
# print(user)
# print(user2)
# print(user3)


# # CALL
# class A:
#     def __init__(self, value):
#         self.value = value
#
#     # call дозволяє нам зробити з екземпляра класу ф-ю яка може щось робити
#     def __call__(self, inc, *args, **kwargs):
#         print('prev value was increase to selected value')
#         self.value += inc
#
#
# a = A(5)
# print(a.value)
# a(7)
# print(a.value)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()


# mini-Реалізація Array
class Array:
    length = 0

    def __init__(self, *args):
        self.__arr = [*args]
        Array.length = len(self.__arr)

    def __str__(self):
        return str(self.__arr)

    def __setitem__(self, key, value):
        self.__arr[key] = value

    def __getitem__(self, item):
        return self.__arr[item]

    def push(self, item):
        self.__arr.append(item)

    def map(self, cb):
        return Array(*[cb(i) for i in self.__arr])

    def filter(self, cb):
        return Array(*[i for i in self.__arr if cb(i)])


array = Array(1, 2, 3, 4, 5, 6)
print(array)
print(array.length)
array[0] = 10
print(array)
print(array[3])
array.push(7)
print(array)
print(type(array))
print(array.map(lambda x: x ** 2))
print(array.filter(lambda x: x % 2 == 0))
