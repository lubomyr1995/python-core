##########################
# """
#     Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# з функціонала:
#  * вивід всіх покупок
#  * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь-якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)
# """
import uuid
from typing import TypedDict, List
import json

PurchaseTypy = TypedDict('PurchaseTypy', {'id': int, 'name': str, 'price': int})


class ShoppingBook:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__shopping_list: List[PurchaseTypy] = []
        self.__read_file()

    def __write_shopping_list(self):
        try:
            with open(self.__file_name, 'w') as file:
                json.dump(self.__shopping_list, file)
        except Exception as e:
            print(e)
            return e

    def __read_file(self):
        try:
            with open(self.__file_name, 'r') as file:
                self.__shopping_list = json.load(file)
        except (Exception,):
            self.__write_shopping_list()

    def __id(self):
        return self.__shopping_list[-1]['id'] + 1 if self.__shopping_list else 1

    def __get_all_purposes(self):
        print('All purposes: ')
        if len(self.__shopping_list) == 0:
            print('You dont have shopping list yet, please add sth...')
        else:
            for p in self.__shopping_list:
                print(f'{p["id"]}. {p["name"]}: {p["price"]}$')
            print(' ')

    def __add_purpose(self):
        name = input('Please enter purpose name: ')
        while True:
            try:
                price = int(input('Please enter purpose price: '))
                break
            except (Exception,):
                pass
        self.__shopping_list.append({'id': self.__id(), 'name': name, 'price': price})
        self.__write_shopping_list()
        print('Purpose added!')

    def __search_purpose(self):
        print('Searching purposes...')
        keys = ['id', 'name', 'price']
        for i, v in enumerate(keys):
            print(f'{i}) {v}')
        choice = int(input('Please choose number: '))
        try:
            find = input(f'Please enter search {keys[choice]}: ')
            purposes: List[PurchaseTypy] = [p for p in self.__shopping_list if str(p[keys[choice]]) == find]
            if len(purposes) == 0:
                print('No purposes found.')
            else:
                for purpose in purposes:
                    print(f'{purpose["name"]}: {purpose["price"]}$')
        except (Exception,):
            print("You selected wrong option, please try again.")
            self.__search_purpose()

    def __most_expensive(self):
        print('Most expensive:')
        if not self.__shopping_list:
            print('No purchases yet. You can add using the add() method.')
        else:
            print(max(self.__shopping_list, key=lambda i: i['price']))

    def __delete_purpose_by_id(self):
        print('Deleting purpose by id...')
        _id = input('Please enter purpose id: ')
        index = next((i for i, v in enumerate(self.__shopping_list) if str(v['id']) == _id), None)
        if index:
            self.__shopping_list.pop(index)
            self.__write_shopping_list()
            print('Purpose deleted.')
            return

    def menu(self):
        while True:
            print(50 * '-')
            print("1) Show all purposes: ")
            print("2) Add purpose: ")
            print("3) Search: ")
            print("4) Show the most expensive purpose: ")
            print("5) Remove purpose by id: ")
            print("9) Exit: ")
            choice = input("Enter your choice: ")
            print("*" * 50)
            match choice:
                case '1':
                    self.__get_all_purposes()
                case '2':
                    self.__add_purpose()
                case '3':
                    self.__search_purpose()
                case '4':
                    self.__most_expensive()
                case '5':
                    self.__delete_purpose_by_id()
                case '9':
                    break


FILENAME = 'purchases.txt'
purchases = ShoppingBook(FILENAME)
purchases.menu()
