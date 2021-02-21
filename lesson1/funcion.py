print(len('Hello World!')) # пример наиболее распространенных функций 

# price = 100
# discount = 5
# price_with_discount = price - price * discount / 100
# print(price_with_discount)

# создание функции

def discounted(price, discount):
    if discount >= 100:
        price_with_discount = print('Неа, твоя скидка теперь 0:', price) # если дискон больше 100, то мы выводим цену без скидки
    else:
        price_with_discount = price - price * discount / 100
        print(price_with_discount)

discounted(10, 50)  # воод данных в функцию 
discounted(200, 30)
discounted(500, 35)
discounted(500, 101)


# взятие по модулю abs() текущей скидки 

def discounted(price, discount):
    price = abs(float(price))  # приведение к числу без точки и взятие по модулю
    discount = abs(float(discount))  # приведение к числу без точки и взятие по модулю
    if discount >= 100:
        price_with_discount = print('Неа, твоя скидка теперь 0:', price) # если дискон больше 100, то мы выводим цену без скидки
    else:
        price_with_discount = price - price * discount / 100
        print(price_with_discount)

discounted(10, -50)  # воод данных в функцию 
discounted(200, 30)
discounted(-500, 35)
discounted(500, 101)

# делаем функцию полезной

def discounted(price, discount):
    price = abs(float(price))  
    discount = abs(float(discount))  
    if discount >= 100:
        price_with_discount = print('Неа, твоя скидка теперь 0:', price) # если дискон больше 100, то мы выводим цену без скидки
    else:
        price_with_discount = price - price * discount / 100
        return(price_with_discount)   

p = discounted(100, 50)
print(p)


product = {
    'name': 'Samsung Galaxy S10', 
    'stock': 8, 
    'price': 50000.0,
    'discount': 50
}
product['with_discount'] = discounted(product['price'], product['discount']) # передаем в функцию idscounted значения из словаря выше
print(product)

# именованные аргументы 

def discounted(price, discount, max_discount = 50):
    price = abs(float(price))  
    discount = abs(float(discount))  
    max_discount = abs(float(max_discount))
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return(price_with_discount)   

product = {
    'name': 'Samsung Galaxy S10', 
    'stock': 8, 
    'price': 50000.0,
    'discount': 70
}
product['with_discount'] = discounted(product['price'], product['discount'], max_discount=80) # передаем в функцию idscounted новое значение скидки
print(product)


# Выбрасывание исключения при вводе крайних значений 

def discounted(price, discount, max_discount = 50):
    price = abs(float(price))  
    discount = abs(float(discount))  
    max_discount = abs(float(max_discount))
    if max_discount > 99:    # здесь
        raise ValueError('Максимальная скидка не может быть больше 99 %')  # здесь
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return(price_with_discount)   


discounted(100, 50, max_discount=100) # здесь 
