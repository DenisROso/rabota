#Задание №5

import random

result_string = ''
awesome_result_string = ''

number_list = []

for i in range(0, 20, 1):
    value = (round(random.random() * 100, 2));
    number_list.append(value)
    element = number_list[len(number_list) - 1]
    result_string = result_string + f'{int(str(element).split(".")[0])} руб. {int(str(element).split(".")[1]):02d} коп., '
    awesome_result_string = awesome_result_string + f'{int(str(element).split(".")[0]):02d} руб. {int(str(element).split(".")[1]):02d} коп., '

print(f'Сортировка по возрастанию ({id(number_list)}):  {awesome_result_string}')

reverse_number_list = list(reversed(number_list))
print(f'Сортировка по убыванию ({id(reverse_number_list)}): {reverse_number_list}')

print(f'Цены пяти самых дорогих товаров {(reverse_number_list[4::-1])}')