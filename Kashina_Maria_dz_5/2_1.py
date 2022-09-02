# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

# игра человека с человеком

candy = 2021
order = 1
while candy > 0:
    grab = int(input('Введите число от 1 до 28 (При первом ходе желательно взять 20 конфет, '
                     'а затем 29 - количество конфет, взятое вторым игроком): '))
    if 0 < grab < 29:
        candy -= grab
        print(f'Конфет осталось: {candy}')
    else:
        break
    if order == 1:
        order = 2
    else:
        order = 1
    print(f'Ходит игрок номер {order}')
if order == 1:
    order = 2
else:
    order = 1
print(f'Победил игрок номер {order}')
