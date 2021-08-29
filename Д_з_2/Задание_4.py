#Задание №4

person_list = ['инженер-конструктор Игорь',
               'главный бухгалтер МАРИНА',
               'токарь высшего разряда нИКОЛАй',
               'директор аэлита']

person_name = ''

for element in person_list:
    person_name = element.split(' ')[-1].capitalize()
    print(f'Привет, {person_name}!')