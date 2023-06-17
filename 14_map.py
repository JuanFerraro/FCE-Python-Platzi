numbers = [1, 2, 3, 4, 5, 6]
number_v2 = []

for i in numbers:
    number_v2.append(i * 2)

print(numbers)
print(number_v2)

number_v3 = list(map(lambda i: i * 2, numbers))
print(number_v3)

numbers_1 = [1,2,3,4,5]
numbers_2 = [6,7,8] # Toma como limite la list mas pequeña

result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)