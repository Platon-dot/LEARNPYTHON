from faker import Faker
import csv
from datetime import date
import random

fake = Faker('ru_RU')

def fake_companies(num_rows=10):
    companies = []
    for _ in range(num_rows):
        companies.append(
            [fake.large_company(), fake.city_name(),
            fake.street_address(), fake.phone_number()]
        )
    return companies


def fake_enployees(companies, num_rows=10):
    employees = []
    for company in companies:
        for _ in range(num_rows):
            employee = [fake.name(), fake.job(), fake.phone_number(),
                fake.free_email(), fake.date_of_birth(minimum_age=18, maximum_age=70)]
            employees.append(company + employee)
    return employees


def fake_payments(employees):
    payments = []
    for employee in employees:
        for month in range(1, 13):
            payment_date = date(2020, month, random.randint(10, 28))
            ammount = random.randint(10000, 200000)
            payment = [payment_date, ammount]
            payments.append(employee + payment)
    return payments


# выводим фейковые данные
# print(fake.name(), fake.city_name(), fake.large_company())

# нужное количество строчек в csv файле
#def get_fake_row():#
#    return [fake.name(), fake.city_name(), fake.street_address(),
#            fake.large_company(),
#            fake.job(), fake.phone_number(), fake.free_email(),
#            fake.date_of_birth(minimum_age=18, maximum_age=70),
#            random.randint(20000, 200000)]

# функция записи в csv файл

def generate_data(payments):
    with open('salary.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        for payment in payments:
            # передаю сюда список из предыдущей функции для записи значений в таблицу
            writer.writerow(payment)

if __name__ == '__main__':
    companies = fake_companies()
    employees = fake_enployees(companies)
    payments = fake_payments(employees)
    generate_data(payments)