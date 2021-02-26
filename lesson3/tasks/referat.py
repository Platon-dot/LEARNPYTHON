"""
Скачайте файл по ссылке
Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
Подсчитайте количество слов в тексте
Замените точки в тексте на восклицательные знаки
Сохраните результат в файл referat2.txt

"""

from collections import Counter


with open('referat.txt', 'r', encoding='utf-8') as my_file:
    user_text = my_file.read()
    word_sum = len(user_text)
    print(word_sum)
    word_count = Counter(user_text.split())
    d = word_count   # вводим новую переменную для расчетов
    for k, v in d.items(): # цикл вывода словаря и записи в фрмате ключ - значение на каждой строчке
        print(k, v)
    
    user_text1 = user_text.replace('.', "!")
    print(user_text1)
    
    
    with open('referat2.txt', 'w', encoding='utf-8') as my_file2:
        my_file2.write(f'{word_sum}\n{word_count}{user_text1}')
        
    