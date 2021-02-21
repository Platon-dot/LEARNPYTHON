# task 1

names = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша'] 
def find_person(names):  # вызываем список
    name = input('Введи имя: ') # ввести имя ручками
    for name_search in names: # 
        if name == name_search:
            print(f'Нашёл {name}')
        else: 
            print(f'Не нашёл {name}')
print(find_person(names))


# task 2

'''
Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
пользователя “Как дела?”, пока он не ответит “Хорошо
'''

while True:
    hello_user = input('Как дела? ')
    if hello_user == 'Хорошо':
        print('Молодцом!!!')
        break
    else:
        print('Я рад что у тебя {}'.format(hello_user))


# task 3

'''
Задание 2
Создайте словарь типа "вопрос": "ответ", например: {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее.
Напишите функцию ask_user() которая с помощью функции input() просит пользователя ввести вопрос, 
а затем, если вопрос есть в словаре, программа давала ему соотвествующий ответ. Например:
Пользователь: Что делаешь?
Программа: Программирую
'''

questions_list ={"Как дела?": "Хорошо!", 
                "Что делаешь?": "Программирую",
                }

def ask_user():
    while True:
        ask_example = input('Введите что-нибудь')
        if ask_example in questions_list:
            print(questions_list[ask_example])

print(ask_user())