# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

from random import randint


def create_list(numbers, min, max):
    return [randint(min, max) for i in range(numbers)]


def unique_values(some_list):
    return [i for i in set(some_list)]


list_test = create_list(15, 0, 4)
print(list_test)
print(unique_values(list_test))
