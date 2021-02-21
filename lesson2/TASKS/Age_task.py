age = int(input('Введи свой возраст: '))

def age_stage(age):
    if age < 7:
        return 'Kindergarten'
    elif 18 >= age >= 7:
        return 'School'
    elif 23 >= age > 18:
        return 'University'
    else:
        return 'Work! The sun is still high'

if age_stage(age) == 'Work! The sun is still high':
    print(f'Тебе уже пора: {age_stage(age)}')
else:   
    print(f'Тебе нужно идти в: {age_stage(age)}')