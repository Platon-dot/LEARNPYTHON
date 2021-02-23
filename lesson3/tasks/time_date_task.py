'''
Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
Превратите строку "01/01/25 12:10:03.234567" в объект datetime
'''
from datetime import datetime, timedelta, date

dt_now = datetime.now()

delta = timedelta(days=-1)
yesterday = dt_now - delta
toomorrow = dt_now + delta
            print(yesterday)
print(dt_now)
        print(toomorrow)

# превращение в объект

user_line_date = '01/01/25 12:10:03.234567'
# user_line_date = user_line_date.replace(" ", "")
print(user_line_date)
user_date = datetime.strptime(user_line_date, "%d/%m/%y %H:%M:%S.%f")
print(user_date)