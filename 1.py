# Вводим строчку и меняем все пробелы на знак подчеркивания

def underline(string):
    enter = ''
    for i in range(len(string)):
        if string[i] == ' ':
            enter += '_'
        else:
            enter += string[i]
    return enter


print(underline(input()))
