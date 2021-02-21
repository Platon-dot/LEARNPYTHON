balance = -10
print(bool(balance < 0))

if balance < 0:
    print('Пожалуйста, пополните баланс!')


balance = 100
price = 200

print('Баланс < 0 or < price:',bool(balance < 0 or price > balance))

if balance < 0 or price > balance:
    print('Пожалуйста, пополните баланс!')


temperature = 26

if temperature < 0:
    print('It\'s so cold now')
elif 0 <= temperature <= 15:
    print('The temperature is normal')
elif 15 <= temperature <= 25:
    print('It\'s warm outside')
else:
    print('Man, it\'s so hot')
    
# в виде функции

temperature = 26

def weather(temperature):
    if temperature < 0:
        return 'It\'s so cold now'
    elif 0 <= temperature <= 15:
        return 'The temperature is normal'
    elif 15 <= temperature <= 25:
        return 'It\'s warm outside' 
    else:
        return 'Man, it\'s so hot'
    
print(weather(-2))
print(weather(30))
print(weather(-15))

# в сложных условиях

phone1 = {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1,'discount': 15}
phone2 = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0,'discount': 10}
phone3 = {'name': '', 'stock': 18, 'price': 10000.0,'discount': 10}


def discounted(price, discount, max_discount=20, name= ''):  
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount or 'iphone' in name.lower() or not name:
        return price
    else:
        return price - (price * discount / 100)
    
apple_desc = discounted(phone1['price'],phone1['discount'], name=phone1['name'])
print('Apple disc', apple_desc)


android_desc = discounted(phone2['price'],phone2['discount'], name=phone2['name'])
print('Android disc', android_desc)

noname_desc = discounted(phone3['price'],phone3['discount'], name=phone3['name'])
print('Noname disc', noname_desc)