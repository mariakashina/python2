import csv


def worker_table_read():
    try:
        search = input('Какого/их работника/ов хотите найти? Введите искомый параметр: ')
    except ValueError:
        print('Некорректный ввод данных')
    with open('worker_data.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if search in row:
                print(row)