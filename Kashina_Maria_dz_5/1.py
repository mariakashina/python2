# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

numbers = [3, 1, 2, 3, 4, 6, 1, 7]


def up_list(spisok, num):
    for i in range(len(spisok) - num):
        count = 0
        for j in spisok[i:i + num - 1]:
            spisok2 = spisok[i:i + num - 1].copy()
            spisok2.append(spisok2[-1] - 1)
            if j < spisok2[spisok2.index(j) + 1]:
                count += 1
        if count == len(spisok[i:i + num - 1]) - 1:
            return spisok[i:i + num]
    return 'таких нет'


print(up_list(numbers, 2))
