# print('hw4')
# # EX1 Є файл email, записати в новий файл пошти в кого gmail.com

def create_file_with_selected_address(file_name: str, find_email: str):
    try:
        with open(file_name, 'r') as file, open(f'{file_name.split('.')[0]}@{find_email}.txt', 'w') as new_file:
            for line in file:
                email = line.split()[-1]
                if email.endswith(find_email):
                    # print(email, file=new_file)
                    # new_file.write(f'{line}')
                    new_file.write(f'{email}\n')
    except Exception as e:
        return e


create_file_with_selected_address('emails.txt', 'gmail.com')
