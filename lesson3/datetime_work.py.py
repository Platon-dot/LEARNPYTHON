# пример: 

from datetime import datetime, timedelta, date

dt_now = datetime.now() # datetime.now() берет текущее время
print(dt_now)
dt2 =  datetime(2015, 5, 16, 8, 3, 44)

# Разница между двумя датами

delta = dt_now - dt2
print(f"Разница составит: {delta}")

dt3 = dt2 + delta  # возможность создать иную дату из delta
print(dt3)

# импортирование temedelta
dt = date(2000, 1, 1)
print(dt)
delta = timedelta(days=1)  # создали дельту в которой лежит 1 день
print(delta)  # выводим на печать то что положили в delta
# теперь математические действия
print(dt - delta)
print(dt + delta)

# вывод даты на экран в формате strftime
dt_now.strftime("%d.%m.%Y %H:%m")
print(dt_now.strftime("%d.%m.%Y %H:%m"))

dt_now.strftime("%d-%m-%Y")
print(dt_now.strftime("%d-%m-%Y"))

dt_now.strftime("%A %d %B %Y")
print(dt_now.strftime("%A %d %B %Y"))

# вывод формата даты на локальных языках

import locale
locale.setlocale(locale.LC_TIME, "es_ES")
print(dt_now.strftime("%A %d %B %Y"))


# Получение даты из строки

date_string = '12/23/2010'  # получаем дату в виде строки
date_dt = datetime.strptime(date_string, '%m/%d/%Y') # кормим ему переменную со строкой и формат в ктором я хочу это увидеть
print(date_dt)
