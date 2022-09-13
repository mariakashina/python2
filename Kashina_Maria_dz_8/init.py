class Worker:

    def __init__(self):
        self.name = input('Введите имя работника:')
        self.surname = input('Введите фамилию работника:')
        self.position = input('Введите должность работника:')
        self.income = input('Введите оклад работника:')


class Position(Worker):

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_full_salary(self):
        return self.income

    def get_position(self):
        return self.position