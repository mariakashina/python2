import re


def get_name():
    name = input(f'Введите имя контакта: ')
    return name


def get_number():
    number = input(f'Введите номер в виде +7-XXX-XXX-XX-XX: ')
    try:
        if not re.fullmatch(r'(?:\+7|8)(?:-\d{2,3}){4}', number):
            raise ValueError('Номер не соответствует шаблону')
    except ValueError:
        print('Номер не соответствует шаблону. Лучше переписать')
    return number


def get_note():
    note = input(f'Введите примечание к этому контакту: ')
    return note


def data_collection():
    return get_name(), get_number(), get_note()
