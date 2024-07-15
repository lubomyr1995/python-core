# # 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# # - перший записує в список нову справу
# # - другий повертає всі записи
# def list_of_things():
#     lst = []
#
#     def add(action):
#         nonlocal lst
#         lst.append(action)
#
#     def get_list():
#         return lst
#
#     return add, get_list
#
#
# add, get_list = list_of_things()
# add('do1')
# add('do2')
# add('do3')
# print(get_list())


# # 2) протипізувати перше завдання
# from typing import Callable, Tuple
#
#
# # def list_of_things() -> Tuple[Callable[[str], None], Callable[[], list[str]]]:
# def list_of_things():
#     lst: list[str] = []
#
#     def add(action: str):
#         nonlocal lst
#         lst.append(action)
#
#     def get_list():
#         nonlocal lst
#         return lst.copy()
#
#     return add, get_list
#
#
# add1, list1 = list_of_things()
# add2, list2 = list_of_things()
# add1('do1')
# add1('do2')
# add1('do3')
# add2('do4')
# add2('do5')
# print(list1())
# print(list2())

# # 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
# # Приклад:
# # expanded_form(12) # return '10 + 2'
# # expanded_form(42) # return '40 + 2'
# # expanded_form(70304) # return '70000 + 300 + 4'
# def expanded_form(n: int) -> str:
#     st = str(n)
#     lst = []
#     for i, j in enumerate(st):
#         if j != '0':
#             lst.append(f'{j}{("0" * (len(st) - i - 1))}')
#     return '+'.join(lst)
#
#
# print(expanded_form(42))
# print(expanded_form(142))
# print(expanded_form(70304))
# print(expanded_form(1))


# # 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# # та буде виводити це значення після виконання функцій
# from typing import Callable
#
#
# def decorator_counter(func: Callable) -> Callable:
#     count = 0
#
#     def wrapper(*args, **kwargs) -> None:
#         nonlocal count
#         func(*args, **kwargs)
#         count += 1
#         print(f'This function was called {count}.')
#
#     return wrapper
#
#
# @decorator_counter
# def say_hello() -> None:
#     print('Hello')
#
#
# @decorator_counter
# def say_goodbye() -> None:
#     print('Goodbye')
#
#
# say_hello()
# say_hello()
# say_goodbye()
# say_hello()
# say_goodbye()


