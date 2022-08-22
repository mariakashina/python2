# Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 5 рублевых и 1 рублевых

salary = int(input())
one_ruble = salary % 5
twenty_five_rubles = (salary - salary % 5) // 25
ten_rubles = ((salary - salary % 5) - 25 * twenty_five_rubles) // 10
five_rubles = (((salary - salary % 5) - 25 * twenty_five_rubles) - ten_rubles * 10) // 5
print(f'Количество купюр: {one_ruble + ten_rubles + twenty_five_rubles + five_rubles}')
print(f'Количество 1 рублевых: {one_ruble} купюр(а/ы)')
print(f'Количество 5 рублевых: {five_rubles} купюр(а/ы)')
print(f'Количество 10 рублевых: {ten_rubles} купюр(а/ы)')
print(f'Количество 25 рублевых: {twenty_five_rubles} купюр(а/ы)')
