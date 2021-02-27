def format_price(price):
    price = abs(int(price))
    return f'Цена: {price} руб.'

result = format_price(56.24)
print(result)