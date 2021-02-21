def get_summ(one, two, delimiter = '&'):
    one = str.upper(one)
    two = str.upper(two)
    delimiter = str.upper(delimiter)
    summ = f'{one}{delimiter}{two}'
    print(summ)

get_summ('Learn', 'Python')