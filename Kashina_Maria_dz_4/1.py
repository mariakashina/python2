# Создать список случайных чисел от -10, до 10 на num * 2 элементов. num вводим с клавиатуры.

import random

rand_list = []
num = int(input('Введите натуральное число: '))
for i in range(num * 2):
    rand_list.append(random.randint(-10, 10))
print(rand_list)

# Вывести все числа меньше 0 и делящиеся на 3

for el in rand_list:
    if el < 0 and el % 3 == 0:
        print(el)

# Сказать кол-во элементов 5 и 3

print(rand_list.count(5) + rand_list.count(3))

# Вывести разницу между кол-вом максимальных и минимальных значений

max_list = max(rand_list)
min_list = min(rand_list)
print(abs(rand_list.count(max_list)-rand_list.count(min_list)))

# Сделать копию списка. Развернуть и упорядочить список список
# Я так понимаю, что слово "список" второе написано случайно. И осортировала просто по возрастанию

rand_list_copy = rand_list
rand_list_copy.reverse()
print(rand_list_copy)
rand_list_copy.sort()
print(rand_list_copy)

# Удалить половину элементов списка

print(rand_list_copy[:num])

# Очистить список

rand_list_copy.clear()
print(rand_list_copy)
