# # 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# input_str = input("Enter a string: ")
# res = ','.join([i for i in input_str if i.isnumeric()])
# print(res)


# # 2)написати прогу яка вибирає зі введеної строки числа і виводить їх так як вони написані
# # наприклад:
# # st = 'as 23 fdf33dg544 34 '
# input_str = input("Enter a string: ")
# print(', '.join(''.join([i if i.isdigit() else ' ' for i in input_str]).split()))


# # 1)есть строка:
# # записать каждый символ в лист поменяв его на верхний регистр
# # пример:
# # ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
# input_str = input("Enter a string: ")
# res = [i.upper() for i in input_str]
# print(res)


# # 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# # пример:
# # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
# print([i**2 for i in range(50) if i % 2 != 0])


# FUNCTION
# # - створити функцію яка виводить ліст
# def print_list(lst: list) -> None:
#     print(lst)
#
#
# print_list([1, 2, 3, 4, 5])

# # - створити функцію яка приймає три числа та виводить та повертає найменьше.
# def min_value_of_three(a: float, b: float, c: float) -> float:
#     print(min(a, b, c))
#     return min(a, b, c)
#
#
# min_value_of_three(1, 2, 3)


# # - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# def show_value(*args) -> float:
#     print(max(args))
#     return min(args)
#
#
# print(show_value(1, 2, 3, 5, 0, 10, 7))

# # - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# def sum_of_list(lst: list) -> float:
#     return sum(lst)
#
#
# print(sum_of_list([1, 2, 3, 4, 5]))


# #  - заменить каждое четвертое значение на "Х"
# def change_to(lst: list) -> list:
#     return ['X' if (i % 4 == 3) else x for i, x in enumerate(lst)]
#
#
# print(change_to([1, 2, 3, 4, 5, 's', 5, 'e', 6]))


# # 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
# def draw_square(n):
#     print(n * '* ')
#     for i in range(n - 2):
#         print('* ', end='')
#         print((n - 2) * '  ', end='')
#         print('*')
#     print(n * '* ')


# draw_square(10)


# # 3) вывести табличку умножения с помощью цикла while
# def multi(n):
#     i = j = 1
#     while i < n:
#         while j < n:
#             print(i * j, end='')
#             print('  ' if i * j // 10 else '   ', end='')
#             j += 1
#         print()
#         i += 1
#         j = 1
#
#
# multi(10)


# # 4) переделать первое задание под меню с помощью цикла
# # Дан лист:
# #   - найти min число в листе
# #   - удалить все дубликаты в листе
# #   - заменить каждое четвертое значение на "Х"
#
#
# def min_el(lst: list):
#     print('min_el: ', min(lst))
#
#
# def unique(lst: list):
#     print('unique numbers: ', set(lst))
#
#
# def replace_x(lst):
#     for i in range(3, len(lst), 4):
#         lst[i] = 'X'
#     print('modified list: ', lst)
#
#
# def make_decision(lst: list):
#     while True:
#         print(
#             '1. Знайти мін число.\n2. Видалити всі одинакові значення.\n3. Замінити кожне 4-е значення на Х:\n0. Вийти з програми \n')
#         k = int(input())
#         if k == 1:
#             min_el(lst)
#         elif k == 2:
#             unique(lst)
#         elif k == 3:
#             replace_x(lst)
#         elif k == 0:
#             break
#         print('Зробіть свій вибір')
#
#
# make_decision([1, 2, 3, 4, 5])