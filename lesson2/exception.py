

# функция делящая пирог на количество людей


def cut_cake(people, cakes):
    z = round(cakes / people, 2)
    print(f'Каждый получит {z} пирога')

cut_cake(8, 3)


# переписываем с перехватом исключений

def cut_cake(people, cakes):
    try:
        z = round(cakes / people, 2)
        print(f'Каждый получит {z} пирога')
    except  ZeroDivisionError:
        print("Не может быть 0 человек")
    except TypeError:
        print('Программа принимает только числа')
cut_cake(8, 3)

# оптимизируем

def cut_cake(people, cakes):
    try:
        z = round(cakes / people, 2)
        print(f'Каждый получит {z} пирога')
    except  (ZeroDivisionError, TypeError):
        print("Не могу поделить")
cut_cake(8, 3)