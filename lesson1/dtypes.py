a = 'Привет'
b = 'зашкварки'
c = 2
c = '{} {} {}!'.format(a, c, b)
print(c)

user = 'Python'
c = 'Привет {name}!'.format(name=user)
print(c)

#или

user = 'Python'
c = f'Привет {user}!'
print(c)

a = 'Привет'
b = 'Вася'
c = f'{a} {b}!'
d = len(c)
print(d)

#приведение к загласным и строчным

a = 'Привет'.upper()
b = 'МИР'.lower()
d = 'PyTHon'.capitalize()
c = f'{a} {b} {d}!'
print(c)


# удаление пробелов
a = ' Миша        '
b = a.strip()
print(len(a))  #подсчет длины строки после того как ибрали пробелы
print(len(b))  #подсчет длины строки после того как ибрали пробелы

# замена символов

a = 'Прив3т т363'
b = a.replace('3', 'e') #замена 3 на e
print(b)

# объединение методов
a = 'Привет приветЫ'.lower().replace('ы', '').capitalize()
print(a)

# замена в строке
a = 'Привет мир'
b = a.replace('мир','python')
print(b)

# разбиение строки на список

a = 'learn.python.ru'
print(a.split('.')) # указываем по какому символу разбивать 

a = 'Предложение из нескольких слов 123'
b = a.split()  #разбивка по пробелам, даже если 2 пробела в строке подряд, то () их найдет и разобъет по ним
print(len(b)) # подсчет количества слов в строке

# тип данных None

a = None
b = 0
print(a is None)
print(b is not None)

# типы переменных
a = 2
b = 2.0
c = 'Питон'
d = True
e = None
print(type(a), type(b), type(c), type(d), type(e))

# запрос ввода

#name = input('Введи свое имя: ')
#print(f'Привет {name}!')


#age = int(input('Сколько вам лет? '))  # введенный в input строку нельзя вычитать из числа , нужно привести к integer
#age = 2021 - age
#print(f'Вы родились {age}!')

# int превращает что может в целое число

print(bool('Привет'))
print(bool(''))
print(bool(1))
print(bool(0))
print(bool(0.1))
print(bool(-2))
print(bool(None))


# задание



