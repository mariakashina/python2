# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

operations = {
    '+': lambda x, y: float(x) + float(y),
    '-': lambda x, y: float(x) - float(y),
    '*': lambda x, y: float(x) * float(y),
    '/': lambda x, y: float(x) / float(y)
}


def calc(string):
    expression = list(string)
    for el in expression:
        if el == '.':
            i = expression.index(el)
            expression[i - 1] = expression[i - 1] + '.' + expression[i + 1]
            expression.pop(i)
            expression.pop(i)
    operators = list(filter(lambda x: x in '+-*/', expression))
    for el in operators:
        if el in '*/':
            i = expression.index(el)
            expression[i - 1] = operations[el](expression[i - 1], expression[i + 1])
            expression.pop(i)
            expression.pop(i)
        else:
            continue
    for el in operators:
        if el in '+-':
            i = expression.index(el)
            expression[i - 1] = operations[el](expression[i - 1], expression[i + 1])
            expression.pop(i)
            expression.pop(i)
        else:
            continue
    print(float(expression[0]))


calc(input())
