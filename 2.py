# Вводим с клавиатуры целое число X
# Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.

number = []
X = int(input('X = '))
for i in range(0, X):
    number.append(int(input()))
max1 = number[0]
max2 = number[0]
for el in number:
    if el > max1:
        max1 = el
for el in number:
    if max2 < el < max1:
        max2 = el
print(max1, max2)
