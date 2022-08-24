# Вводим строчку и выводим на экран:
# * общее количество символов в строке;
enter = input()


def length(string):
    return len(string)


print(length(enter))

# * каждый чётный символ,


def even(string):
    return string[1::2]


print(even(enter))

# * все символы в обратном порядке


def reverse(string):
    return string[::-1]


print(reverse(enter))
