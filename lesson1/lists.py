a = ('Вася','Маша','Петя','Саша')
print(a)

phones = ['Iphone Xs', 'Samsung 10 s', 'Xiaomi Mi8']

print(phones)

phones_count = len(phones)
print(phones_count)

phones.append('Iphone 6')
print(phones)
print(phones.count('Iphone Xs'))
print(phones.count('IPhone 9'))


# обращение к жлементам спискам
print(phones[-1])

# срезы

print(phones[1:3]) # от второго до 3 не включая его
print(phones[:]) #все значения списка
print(phones[:2]) # с 0 до 2 элемента не включая его 
 
print(phones.index('Iphone Xs'))  # вывод индекса элементов из списка


hobbits = ['Двалин', 'Завлин', 'Балин', '42', '1', '5'] #сортировка элементов по алфавиту
hobbits.sort()
print(hobbits)

# поиск элементов в списке
print('Двалин' in hobbits)   # поиск конкретных элементов в списке с логическим результатом True and False
print('345' in hobbits)

# удаление жлементов 
hobbits = ['Двалин', 'Завлин', 'Балин', '42', '1', '5']
print(hobbits)
print(len(hobbits))

del hobbits[0]  #обязательно квадратные списки
print(hobbits)
print(len(hobbits))

# удаление конкретного элемента через .remove()
hobbits.remove('42')
print(len(hobbits))
print(hobbits)








