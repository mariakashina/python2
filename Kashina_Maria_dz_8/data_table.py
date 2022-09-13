import csv

import init


def worker_table_rec():
    try:
        n = int(input('Сколько сотрудников хотите ввести? '))
    except ValueError:
        print('Неверное значение количества записей')
    with open('worker_data.csv', 'a', newline='') as f:
        writer = csv.writer(f, dialect="excel", delimiter=',')
        f.write(f"sep=,\n")
        writer.writerow(('Имя', 'Фамилия', 'Должность', 'Оклад'))
    try:
        for i in range(0, n):
            worker = init.Position()
            with open('worker_data.csv', 'a', newline='') as f:
                writer = csv.writer(f, dialect="excel", delimiter=',')
                writer.writerow((worker.get_name(), worker.get_surname(),
                                 worker.get_position(), worker.get_full_salary()))
    except UnboundLocalError:
        print('')
