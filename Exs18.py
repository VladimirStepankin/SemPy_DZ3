n = int(input("Введите количество элементов массива: "))
list_1 = list()
from random import randint
for i in range(n):
    list_1.append(randint(0, 10))
print(list_1)
x = int(input("Введите число Х: "))
result = list_1[0]
for i in list_1:
    if abs(i - x) < abs(result - x):
        result = i
print(result)