# Вводим строчку и выводим разницу между количеством букв в верхнем и нижнем регистре.


def bigsmall(string):
    big = 0
    small = 0
    for i in range(len(string)):
        if string[i].isupper():
            big += 1
        elif string[i].islower():
            small += 1
    return big - small


print(bigsmall(input()))
