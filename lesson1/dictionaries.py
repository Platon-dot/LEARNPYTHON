lords_of_the_rings = ['Балин', 'Бифур', 'Бомбур', 'Бодруит', 'Борин', 'Бофур', 'Гамил']
products = {
    'name': 'Iphone Xs', 
    'stock': 5, 
    'price': 650,
    'recomend': lords_of_the_rings
}
print(products)
print(len(products))

# добавление элементов в словарь. Старое значение не меняется

products['stock'] = 15 
# print(products)
# a = products['stock']
# b = 15 + a
# print('Текущее количество телефонов:', b) 

products['stock'] += 15 # добавить число к значению в словаре по ключу: products[‘stock’]  += 15
products['memory'] = 64
print(products)

# получение значения элемента

print(products['stock'], products['name'])

# "Безопасное" обращение к словарю

print(products.get('name'))
print('Размер скидки примера:', products.get('discount', 10), '%') # задание значения по умолчению если такого значения не найдено None

del products['memory']
print(products)

# объединение списка и словаря

# products['recomend'] = lords_of_the_rings

print(products['recomend'][1]) # получение первоего элемента списка

# добавление в список новго элемента

products['recomend'].append('Фродо')
print(products)

print('')
print('Списки словарей')
print('')

# список словарей
stock = [
    {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 
    'recomended': ['Samsung Galaxy S10', 'iPhone Xs']},
    {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 5000},
    {'name': 'Xiaomi Mi8', 'stock': 42, 'price': 38000.5}
]
print(type(stock))  # проверка типа stock
print(type(stock[0]))   # проверка типа stock
print(stock[0]) #вывод первого словаря
print(stock[0]['name']) 
stock[0]['price'] = stock[0]['price'] + 10000 # добавили к текущей цене +10000 
print(stock[0]) 
stock[0]['price'] += 10000 # еще один вариант дополнения
print(stock[0])

print(stock[0]['recomended'][1])