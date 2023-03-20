def ind_search():
    data = open('Phonebook.csv', 'r', encoding = 'utf-8')
    count = 0
    name = input('Введите данные строки для удаления: ')
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

def delete():
    list1 = filling_list()
    res = ind_search()
    list2 = []
    for i in range(len(list1)):
        if i != res:
            list2.append(list1[i])
    return list2

def rewrite_delete():
    list2 = delete()
    with open ('Phonebook.csv', 'w', encoding = 'utf-8') as data:
        for i in range(len(list2)):
            data.write(list2[i])
        data.close()