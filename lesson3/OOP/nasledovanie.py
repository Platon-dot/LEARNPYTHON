# безем класс Products из инкапсуляции и наследуем ниже 

class Product:
    def __init__(self, name, price, discount=0, stock=0, max_discount=20.0):
        self.name = name.strip() # удалили из названия пробелы в начале и в конце
        if len(self.name) < 2: # проверили что длина названия не менее 2 символов
            raise ValueError('Название товара должно быть 2 символа и более') # вывод исключения
        self.price = abs(float(price))
        self.discount = abs(float(discount))
        self.stock = abs(int(stock))
        self.max_discount = abs(float(max_discount))
        
        if self.max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if self.discount > max_discount:
            self.discount = self.max_discount
            
    def discount(self):
        return self.price - self.price * self.discount / 100


# дополненительные плюшки
    # проверка на наличие на складе 
    def sell(self, items_count=1):   # если продаваемое количество товаров больше чем на складе 
        if items_count > self.stock:
            raise ValueError('Недостаточно товара на складе') 
        # здесь мы можем начинать взаимодействовать с учетной/бух. базой
        self.stock -= items_count
        
    def __repr__(self): # в удобном виде посмотреть что представляет из себя конкретный объект
        return f'Product name: {self.name}, price: {self.price}, stock: {self.stock}'

# создаем наследника продукта Телефон

class Phone(Product): # далее внизу нужно описывать то, что отличает этот, к примеру, товар от текущих правил
    def __init__(self, name, price, color, stock=0, discount=0, max_discount=20):
        super().__init__(name, price, stock, discount, max_discount) # передаем в __init__ конкретные переменные за исключением новой
        self.color = color
    def __repr__(self):
        return f'Phone name: {self.name}, price: {self.price}, stock: {self.stock}'

my_phone = Phone('Iphone', 60000, 'Черный')
print(my_phone)
print(my_phone.color)

# создаем наследника продукта Диван

class Sofa(Product): # далее внизу нужно описывать то, что отличает этот, к примеру, товар от текущих правил
    def __init__(self, name, price, color, texture, stock=0, discount=0, max_discount=20):
        super().__init__(name, price, stock, discount, max_discount) # передаем в __init__ конкретные переменные за исключением новой
        self.color = color
        self.texture = texture
        
    def __repr__(self):
        return f'Sofa name: {self.name}, price: {self.price}, stock: {self.stock}'

my_sofa = Sofa('Большой диван', 25312, 'Зеленый', 'Велюр')
print(my_sofa)
print(my_sofa.color)
print(my_sofa.texture)