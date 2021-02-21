for number in range(3): # range - количество раз с указанием
    print(f'Привет мир {number}!')


# перебор строки побуквенно

for letter in 'python':
    print(letter.upper())


# разобъем на пробелы

example_string = 'I\'m learn Python'
for word in example_string.split():
    print(f'Длина слова "{word}": {len(word)}')
    
# пример цикла по списку и его обход. Вычисление среднего арифместического

students_scores = [1, 21, 19, 6, 5]

print(f'Средняя оценка: {sum(students_scores)/len(students_scores)}')

for score in students_scores:
    print(f'Оценка: {score}')

# второй вариант оформления

students_scores = [1, 21, 19, 6, 5]

scores_sum = 0
for score in students_scores:
    scores_sum += score
    print(scores_sum)

print(f'Средняя оценка: {sum(students_scores)/len(students_scores)}')


# работа со списком словарей

from cycle_for_cycle_FOR import discounted

stock = [
	{'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1,
            'discount': 25},
#	{'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0,
#            'discount': 10},
#	{'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}
]

for phone in stock:

    phone['final_price'] = discounted(phone['price'], phone['discount'], name = phone['name'])

print(stock)