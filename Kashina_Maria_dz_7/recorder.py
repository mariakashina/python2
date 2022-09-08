import csv

import inputter as put


def phonebook_recorder():
    try:
        n = int(input('Сколько номеров хотите ввести? '))
    except ValueError:
        print('Неверное значение количества контактов')
    with open('phone.csv', 'a', newline='') as f:
        writer = csv.writer(f, dialect="excel", delimiter=',')
        f.write(f"sep=,\n")
        writer.writerow(('Имя', 'Номер', 'Примечание'))
    try:
        for i in range(0, n):
            with open('phone.csv', 'a', newline='') as f:
                writer = csv.writer(f, dialect="excel", delimiter=',')
                writer.writerows([put.data_collection()])
    except UnboundLocalError:
        print('')
