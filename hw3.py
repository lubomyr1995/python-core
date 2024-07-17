# # Створити клас Rectangle:
# # -він має приймати дві сторони x,y
# # -описати поведінку на арифметични методи:
# #   + сумма площин двох екземплярів ксласу
# #   - різниця площин двох екземплярів ксласу
# #   == площин на рівність
# #   != площин на не рівність
# #   >, < меньше більше
# #   при виклику метода len() підраховувати сумму сторін
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.area = width * height
#
#     def __add__(self, other):
#         return self.area + other.area
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def __add__(self, other):
#         if isinstance(other, Rectangle):
#             return self.area() + other.area()
#
#     def __sub__(self, other):
#         if isinstance(other, Rectangle):
#             return self.area() - other.area()
#
#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             return self.area() == other.area()
#
#     def __ne__(self, other):
#         if isinstance(other, Rectangle):
#             return self.area() != other.area()
#
#     def __gt__(self, other):
#         if isinstance(other, Rectangle):
#             return self.area() > other.area()
#
#     def __lt__(self, other):
#         if isinstance(other, Rectangle):
#             return self.area() < other.area()
#
#     def __len__(self):
#         return 2 * (self.width + self.height)
#
#
# rec1 = Rectangle(4, 10)
# rec2 = Rectangle(8, 5)
# res_add = rec1 + rec2
# res_sub = rec1 - rec2
# print(res_add)
# print(res_sub)
# print('equality:', rec1 == rec2)
# print('not equality:', rec1 == rec2)
# print(len(rec1))
# print(len(rec2))

# ###############################################################################
# # створити класс Human (name, age)
# # створити два класси Prince и Cinderella які наслідуються від Human:
# # у попелюшки мае бути ім'я, вік, розмір нонги
# # у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде
# # приймати список попелюшок, та шукати ту саму
# #
# # в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# # також має бути метод классу який буде виводити це значення
# class Human:
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age
#
#     def __str__(self) -> str:
#         return f'{self.name} is {self.age} years old'
#
#     def __repr__(self) -> str:
#         return str(self.__dict__)
#
#
# class Cinderella(Human):
#     __count = 0
#
#     def __init__(self, name: str, age: int, foot_size: int) -> None:
#         super().__init__(name, age)
#         self.foot_size = foot_size
#         Cinderella.__count += 1
#
#     @classmethod
#     def get_count(cls) -> int:
#         return cls.__count
#
#
# class Prince(Human):
#     def __init__(self, name: str, age: int, cinderellas_size: int) -> None:
#         super().__init__(name, age)
#         self.cinderellas_size = cinderellas_size
#
#     def find_cinderellas(self, cds: list[Cinderella]) -> Cinderella | None:
#         for cinderella in cds:
#             if self.cinderellas_size == cinderella.foot_size:
#                 return cinderella
#         return None
#
#
# prince = Prince('Ivan', 30, 36)
# cinderellas = [
#     Cinderella('Kira', 22, 39),
#     Cinderella('Vika', 22, 37),
#     Cinderella('Ira', 22, 36),
#     Cinderella('Yulia', 22, 35)
# ]
# print('prince: ', prince)
# print('cinderellas: ', cinderellas)
# print('count_cinderellas: ', Cinderella.get_count())
# founded_cinderella = prince.find_cinderellas(cinderellas)
# print('Founded cinderella is: ', founded_cinderella.name if founded_cinderella else 'Not found cinderella')


# ###############################################################################
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку
#   чи то що передають є класом Book або Magazine інакше ігрнорувати додавання.
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        print(self)


class Book(Printable):
    def __init__(self, name):
        self.__name = name

    def print(self):
        print(self.__class__.__name__, self.__name)


class Magazine(Printable):
    def __init__(self, name):
        self.__name = name

    def print(self):
        print(self.__class__.__name__, self.__name)


class Main:
    __printable_list: list[Magazine | Book] = []

    @classmethod
    def add(cls, item: Magazine | Book):
        if isinstance(item, Magazine | Book):
            cls.__printable_list.append(item)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.__printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.__printable_list:
            if isinstance(item, Book):
                item.print()


Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))
Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()
