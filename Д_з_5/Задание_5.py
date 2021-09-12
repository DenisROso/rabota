#Задание №5

names = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_dict = {}

for el in names:
    if names.count(el) == 1:
        my_dict[el] = el

print(list(my_dict.keys()))