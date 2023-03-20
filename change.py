def ind_search():
    data = open('Phonebook.csv', 'r', encoding = 'utf-8')
    count = 0
    name = input('Введите данные для поиска: ')
    flag = 1
    for line in data:
        if name in line:
            flag = 0
    if flag: print(f'\n Введенных данных нет в справочнике. Повторите команду.')
    data = open('Phonebook.csv', 'r', encoding = 'utf-8')
    for line in data:
        count += 1
        if name in line:
            count -= 1
            return count

    

def filling_list():
    data = open('Phonebook.csv', 'r', encoding = 'utf-8')
    list1 = []
    for line in data:
        list1.append(line)
    return list1

def change():
    list1 = filling_list()
    res = ind_search()
    list2 = []
    for i in range(len(list1)):
        if i != res:
            list2.append(list1[i])
        else:
            new = ''.join(get_change_info())
            list2.append(f'{new}\n')
    return list2


# def get_change_info ():
#     info = []
#     last_name = input("Введите фамилию: ")
#     info.append(f'{last_name} ')
#     first_name = input("Введите имя: ")
#     info.append(f'{first_name} ')
#     middle_name = input("Введите отчество: ")
#     info.append(f'{middle_name} ')
#     brith_name = input("Введите дату рождения: ")
#     info.append(f'{brith_name} ')
#     phone_number = input("Введите номер контакта: ")
#     info.append(f'{phone_number} ')
#     note = input("Введите категорию контакта: ")
#     info.append(f'{note} ')
    
#     return info
def get_change_info ():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(f' {last_name} ')
    first_name = input('Введите имя: ')
    info.append(f' {first_name} ')
    middle_name = input('Введите отчество: ')
    info.append(f' {middle_name} ')
    brith_name = input("Введите дату рождения: ")
    info.append(f'{brith_name} ')
    phone_number = input('Введите номер контакта: ')
    info.append(f' {phone_number} ')
    description = input('Введите категорию контакта: ')
    info.append(f' {description}  ')
    return info









def rewrite_change():
    list2 = change()
    with open ('Phonebook.csv', 'w', encoding = 'utf-8') as data:
        for i in range(len(list2)):
            data.write(list2[i])
        data.close()