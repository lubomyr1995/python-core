# # DECORATOR
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print(20 * '-')
#         func(*args, **kwargs)
#         print(20 * '-')
#
#     return wrapper
#
#
# @decorator
# def greeting(name):
#     print('Hello ' + name)
#     return name
#
#
# greeting('John')

# # Замикання
# def counter():
#     count = 0
#
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#
#     def reset():
#         nonlocal count
#         count = 0
#         return count
#
#     return increment, reset
#
#
# increment, reset = counter()
# print(increment())
# print(increment())
# print(increment())
# print(increment())
# print('reset =', reset())
# print(increment())


# # LAMBDA
# users = [
#     {'name': 'Max', 'age': 18},
#     {'name': 'Tom', 'age': 12},
#     {'name': 'Mark', 'age': 15},
# ]
# users_sorted_by_age = sorted(users, key=lambda user: user['age'])
# print(users_sorted_by_age)
#
# users.sort(key=lambda item: item['age'], reverse=True)
# print(users)


# Type hinting - типізація
from typing import TypedDict, Callable

User = TypedDict('User', {'name': str, 'age': int, 'status': bool}, total=False)
user: User = {
    'name': 'Ivan',
    'age': 23,
    'status': True
}


def counter() -> Callable[[int], int]:
    count = 0

    def inc(x: int = 1) -> int:
        nonlocal count
        count += x
        return count

    return inc


counter1 = counter()
print(counter1(1))
print(counter1(1))
print(counter1(-4))
