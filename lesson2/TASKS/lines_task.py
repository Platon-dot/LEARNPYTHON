

def lines(x, y):
    if  type(x) == str and type(y) == str:
        if x == y:
            return('1')
        elif x != y and len(x) > len(y):
            return('2')
        elif x != y and y == 'Learn':
            return('3')
    else:
        return('0')

print(lines('Hello', 1))
print(lines('Hello', 'Hello'))
print(lines('Hello', 'Hell'))
print(lines('Hello', 'Learn'))
print('Yes, now I understood the funcions')