#Задание №3

class Worker():
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        if type(income) is dict:
            self.__income = income

    def full_income(self):
        try:
            return self.__income['wage'] + self.__income['bonus']
        except:
            return 0


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'Доход с учетом премии: {self.full_income()}'


p1 = Position('Сергей', 'Выхин', 'Электросварщик', {"wage": 60000, "bonus": 12000})
print(p1.get_full_name())
print(p1.get_total_income())