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
    for a in range(expression.count('(')):
        i = len(expression) - 1 - expression[::-1].index('(')
        j = expression[i:].index(')') + i
        operators = list(filter(lambda x: x in '+-*/', expression[i:j]))
        expression.pop(i)
        expression.pop(j - 1)
        for el in operators:
            if el in '*/':
                i = expression[i:j].index(el)
                expression[i - 1] = operations[el](expression[i - 1], expression[i + 1])
                expression.pop(i)
                expression.pop(i)
            else:
                continue
        for el in operators:
            if el in '+-':
                i = expression[i:j].index(el) + i
                expression[i - 1] = str(operations[el](expression[i - 1], expression[i + 1]))
                expression.pop(i)
                expression.pop(i)
            else:
                continue
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
