# Сгенерировать список на num элементов от 150 до 200. num вводим с клавиатуры.

import random

rand_list = []
num = int(input('Введите натуральное число: '))
for i in range(num):
    rand_list.append(random.randint(150, 200))
print(rand_list)

# Мы вводим с клавиатуры какое-то число в этом диапазоне ( от 150 до 200).
# Это построение по росту в строю. Необходимо поставить в строй введеный лемент
# Например: сгенерировались 163, 175, 169 , 200
# Вбили с клавиатуры 180
# Вы второй в строю. И вывести список.

height = int(input('Введите число от 150 до 200: '))
if height > 200 or height < 150:
    print('Ошибка')
else:
    rand_list.append(height)
    rand_list.sort(reverse=True)
print(rand_list)
