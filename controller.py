from import_data import import_data
from change import rewrite_change
from delete import rewrite_delete
from input_data import input_data
from search_data import search
def greeting():
    print("Добро пожаловать в телефонный справочник!")


def choice_sep():
     sep = input("Введите разделитель: ")
     if sep == "":
         sep = None
     return sep

def choice_todo():
    print("Доступные операции с телефонной книгой:\n\
    1 - Запись контакта;\n\
    2 - Просмотр контактов;\n\
    3 - Поиск контакта;\n\
    4 - Изменение контакта;\n\
    5 - Удаление контакта;\n\
    6 - Выход из справочника.")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = choice_sep()
        import_data(input_data(), sep)
        user_entry = input("Нажмите Enter, чтобы вернуться в главное меню ...")
        choice_todo()
    elif ch == '2':
        pbfile = open('Phonebook.csv', 'r', encoding = 'utf-8')
        file_contents = pbfile.read()
        if len(file_contents) == 0:
            print("данных еще не сохранено!")
        else:
            print (file_contents)
        pbfile.close
        user_entry = input("Нажмите Enter, чтобы вернуться в главное меню ...")
        choice_todo()
    elif ch == '3':
        search()
        user_entry = input("Нажмите Enter, чтобы вернуться в главное меню ...")
        choice_todo()
    elif ch == '4':
        rewrite_change()
        user_entry = input("Нажмите Enter, чтобы вернуться в главное меню ...")
        choice_todo()
    elif ch == '5':
        rewrite_delete()
        user_entry = input("Нажмите Enter, чтобы вернуться в главное меню ...")
        choice_todo()
    elif ch == '6':
        print("Спасибо, что воспользовались нашим справочником")