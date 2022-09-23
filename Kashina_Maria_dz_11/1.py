import numpy as np

N = int(input('N = '))
M = int(input('M = '))

array = np.empty(N * M, dtype=int)
for i in range(N * M):
    array[i] = int(input('Введите элемент матрицы: '))
matrix1 = array.reshape((N, M))
print(matrix1)

matrix2 = np.random.randint(10, size=(N, M))
print(matrix2)

sum = np.sum(matrix1) + np.sum(matrix2)
print(sum)

max1 = np.max(matrix1)
max2 = np.max(matrix2)
print(max(max1, max2))

min1 = np.min(matrix1)
min2 = np.min(matrix2)
print(min(min1, min2))
