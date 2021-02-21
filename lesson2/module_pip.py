from collections import Counter


phones = ["Iphone", "Samsung", "LG", "Ihone", "LG", "Samsung", "Samsung"]

count = Counter(phones)
print('LG в списке встречается: ', count["LG"], 'раза')
print('Samsung в списке встречается: ', count["Samsung"], 'раза')
print(count["Hello"])
print(count)



                # два вариант использования lower and replace Вариант 1
test = "ехал Грека через реку, видит Грека в реке рак"
count = Counter(test.lower().replace(' ', '')) # все приводим к нижнему регистру и заменяем пробел пустой строкой
print(count)
                # Вариант2
test = "ехал Грека через реку, видит Грека в реке рак".lower().replace(' ', '')
count = Counter(test) # все приводим к нижнему регистру и заменяем пробел пустой строкой
print(count)

