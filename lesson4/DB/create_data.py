from faker import Faker
import csv
import random

fake = Faker('ru_RU')

# выводим фейковые данные
# print(fake.name(), fake.city_name(), fake.large_company())

# нужное количество строчек в csv файле
def get_fake_row():
    return [fake.name(), fake.city_name(), fake.street_address(),
            fake.large_company(),
            fake.job(), fake.phone_number(), fake.free_email(),
            fake.date_of_birth(minimum_age=18, maximum_age=70),
            random.randint(20000, 200000)]

# функция записи в csv файл

def generate_data(num_rows=100):
    with open('salary.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        for _ in range(num_rows):
            # передаю сюда список из предыдущей функции для записи значений в таблицу
            writer.writerow(get_fake_row())

if __name__ == '__main__':
    generate_data()