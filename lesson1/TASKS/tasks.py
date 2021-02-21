#v = int(input('Введите число от 1 до 10: '))
#print(v + 10)


#name = input('Введите ваше имя: ')
#print(f'Привет, {name} Как дела?')

print(float('1'))
print(int(float('2.5')))
print(bool(1))
print(bool('')) 
print(bool(0))

number = [3, 5, 7, 9, 10.5]
print(number)
number.append('Python')
print(number)
print('Количество элементов:',len(number))
print('Начальный элемент:',number[0])
print('Последний элемент:',number[5])
print('Список с 2 по 4:',number[1:5])
number.remove('Python')
print(number)

town = {
    "city": "Москва", 
    "temperature": "20"
}
print(town['city'])
town['temperature'] = int (town['temperature'])
town['temperature'] -= 5
print(town)
print(town.get('country'))
town['country'] = 'Россия'
town['date'] = '27.05.2019'
print(town)
print('Размер словаря:', len(town), 'элемента')
