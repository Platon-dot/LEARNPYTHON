import csv # импорт модуля [[csv]]

with open('users.csv', 'r', encoding='utf-8') as f: #импортирование
    friends = ['first_name', 'last_name', 'email', 'gender', 'balance'] # создание словарь]] для перечисления
    reader = csv.DictReader(f, friends, delimiter=';')  # начало использования модуля csv. Укладываем по лючам
    money_total = 0
    for row in reader:
        money_total += float(row('balance'))
        
        

with open('users.csv', 'r', encoding='utf-8') as f:
    friends = ['first_name', 'last_name', 'email', 'gender', 'balance'] 
    writer = csv.DictWriter(f, friends, delimiter=';')
    writer.writeheader()
    for user user_list:
        writer.writerow(user)