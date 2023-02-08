n = int(input("Введите количество элементов массива: "))
list_1 = list()
from random import randint
for i in range(n):
    list_1.append(randint(0, 10))
print(list_1)
x = int(input("Введите число Х: "))
count = 0
for i in range(n):
    if x == list_1[i]:
        count +=1
print(count)