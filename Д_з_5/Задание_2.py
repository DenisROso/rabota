#Задание №2

def odd_nums(max_numbers=15):
    return (el for el in range(1, max_numbers + 1, 2))

odd_number_15 = odd_nums(15)
print(next(odd_number_15))
print(next(odd_number_15))
print(next(odd_number_15))
print(next(odd_number_15))
print(next(odd_number_15))
print(next(odd_number_15))
print(next(odd_number_15))
print(next(odd_number_15))
print(next(odd_number_15))