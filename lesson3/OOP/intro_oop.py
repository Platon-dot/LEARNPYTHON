class Point:  # задаем точку в классе на координатной плоскости 
    x = 0
    y = 0

my_point = Point()
print('Положение x: ', my_point.x)

my_point.x = 10 # меняем положение x

print('Положение х: ', my_point.x)



class Point:  # задаем точку в классе на координатной плоскости 
    x = 0
    y = 0
    z = 0
    
    def coordinates(self):  # метод класса 
        print(f'coordinates are: {self.x}, {self.y}, {self.z}')

my_point = Point()  
my_point.x = 10
my_point.z = 25
my_point.y = -5
my_point.coordinates()

# конструктор класса. Для создания точки с конкретными координатами

class Point:  
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def coordinates(self):  # метод класса 
        print(f'coordinates are: {self.x}, {self.y}')
            
my_point = Point(1, 3)

my_point.coordinates()

my_point.x = 10
my_point.y = -5


# конструктор класса __repr__

class Point:  
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def coordinates(self):  # метод класса 
        print(f'coordinates are: {self.x}, {self.y}')
    
    def __repr__(self):
        return f'Point x: {self.x}, y: {self.y}'
            
my_point = Point(1, 3)

print(my_point)




