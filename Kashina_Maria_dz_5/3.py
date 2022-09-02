# Создайте программу для игры в "Крестики-нолики".

player = input('Выберите X или O: ')

def field(cage):
    print('\n')
    print('\t     |     |')
    print(f'\t  {cage[0]}  |  {cage[1]}  |  {cage[2]}')
    print('\t_____|_____|_____')
    print('\t     |     |')
    print(f'\t  {cage[3]}  |  {cage[4]}  |  {cage[5]}')
    print('\t_____|_____|_____')
    print('\t     |     |')
    print(f'\t  {cage[6]}  |  {cage[7]}  |  {cage[8]}')
    print('\t     |     |')
    print('\n')


cage = [' ' for i in range(9)]
pos = {'X': [], 'O': []}
field(cage)


def check_victory(pos, player):
    win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for i in win:
        if all(el in pos[player] for el in i):
            return True
    return False


def check_tie(pos):
    if len(pos['X']) + len(pos['O']) == 9:
        return True
    return False


while not check_victory(pos, player):
    num = int(input(f'Игрок {player}, выберите номер клетки от 1 до 9: '))
    if 1 > num > 9:
        print("Некорректный ввод, введите снова")
        continue
    if cage[num - 1] != ' ':
        print("Поле занято,введите снова")
        continue
    cage[num - 1] = player
    pos[player].append(num)
    field(cage)
    if check_victory(pos, player):
        print(f'Игрок {player} победил!')
        print("\n")
        break
    if check_tie(pos):
        print("Ничья")
        print("\n")
        break
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
