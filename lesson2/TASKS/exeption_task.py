'''
Перепишите функцию hello_user() из задания про while, 
чтобы она перехватывала KeyboardInterrupt, 
писала пользователю "Пока!" и завершала работу при помощи оператора break
'''

def hello_user(): 
    try:     
        while True:
            kak_dela = input('Как дела? ')
            if kak_dela == 'Хорошо':
                print("Пока")
                break
    except KeyboardInterrupt:
        print("Был нажат Ctrl+C")
        
hello_user()

"""
Перепишите функцию discounted(price, discount, max_discount=20) из урока про функции так, 
чтобы она перехватывала исключения, когда переданы некорректные аргументы.

"""

def discounted(price, discount, max_discount = 50):
    try:
        price = abs(float(price))  
        discount = abs(float(discount))  
        max_discount = abs(int(max_discount))
        if max_discount > 99:
            raise ValueError('Максимальная скидка не может быть больше 99 %')
        if discount >= max_discount:
            price_with_discount = price
        else:
            price_with_discount = price - price * discount / 100
        return(price_with_discount)
    except (ValueError, IndentationError):
        print("Возникла ошибка при вводе данных")
        return "error"


print(discounted(500, 30, "35"))
print(discounted(500, 30, "lbd"))
