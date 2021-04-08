import csv

from db import db_session
from models import Company, Employee, Payment

def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['company',  'city', 'address', 'phone_company', 'name', 'job',
                'phone_person', 'email', 'date_of_birth', 'payment_date', 'ammount']
        reader = csv.DictReader(f, fields, delimiter=';')
        payments_data = []
        for row in reader:
            payments_data.append(row)
        return payments_data

def save_companies(all_data):
    processed = []
    companies_unique = []
    for row in all_data:
        if row['company'] not in processed:
            company = {'name': row['company'], 'city': row['city'],
                        'address': row['address'], 'phone': row['phone_company'],
            }
            companies_unique.append(company)
            processed.append(company['name'])
    db_session.bulk_insert_mappings(Company, companies_unique, return_defaults=True)
    db_session.commit()
    return companies_unique

def save_employees(data, companies):
    processed = []
    unique_employees = []
    for row in data:
        if row['phone_person'] not in processed:
            employee = {'name': row['name'], 'job': row['job'], 'phone': row['phone_person'], 
                    'email': row['email'], 'date_of_birth': row['date_of_birth']}
            


if __name__ == '__main__':
    all_data = read_csv('salary.csv')
    companies = save_companies(all_data)
