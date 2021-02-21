list = [1, 26, 13, 14, 165, 4546, 324, 6575, 932, 10]

for list_up in list:
    list_up_one = list_up + 1
    print(list_up_one)


line = input('Введи строку: ')
for letter in line:
    print(letter)

print('--------')

students = [{'school_class': '4a', 'scores': [6,4,4,5,2], 'student_name':'Сидоров'},
{'school_class': '4a', 'scores': [5,4,4,5,2], 'name' : 'Кашперов'},
{'school_class': '4a', 'scores': [3,4,3,5,2], 'name' : 'Майдеров'},
{'school_class': '5a', 'scores': [2,1,3,1,2], 'name' : 'Семенова'},
{'school_class': '6a', 'scores': [5,5,5,5,5], 'name' : 'Всехборцова'}]

avr__scholl = 0
avr__class = 0

for avr_scores in students:
    avr__scholl += sum(avr_scores['scores'])/len(avr_scores['scores']) 
    avr__class = sum(avr_scores['scores'])/len(avr_scores['scores']) 
    print(f'Средний балл класса {avr_scores["school_class"]} составит {avr__class}')

print(f'Средний балл по школе составляет {round(avr__scholl/len(students), 1)}')

