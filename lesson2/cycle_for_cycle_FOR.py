
stock = [
	{'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0,'discount': 10},
    {'name': 'IpHoNe', 'stock': 18, 'price': 10000.0, 'discount': 19},
    {'name': 'D', 'stock': 18, 'price': 10000.0, 'discount': 15}
]

def discounted(price, discount, max_discount=20, name=''): # принимаем значение функции
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Ошибка по проценту скидки')
    if discount >= max_discount or 'iphone' in name.lower() or not name:
        return(price)
    else:
        return price - (price * discount / 100)


for phone in stock:
    print(phone)
    phone['final_price'] = discounted(phone['price'],phone['discount'], name=phone['name'])
    print(phone)