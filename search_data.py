# модуль поиска контакта
def search():
    data = open('Phonebook.csv', 'r', encoding = 'utf-8')
    flag = 1
    name = input('Введите данные для поиска: ')
    for line in data:
        if name in line:
            flag = 0
            print(line)
    if flag: print('Введенных данных нет в справочнике')