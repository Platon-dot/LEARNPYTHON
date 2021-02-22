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
print(delta)
# теперь математические действия
print(dt - delta)
print(dt + delta)

# вывод даты на экран
dt.now.strflime("%d.%m.%Y %H:%m")
dt.now.strflime("%d-%m-%Y")
