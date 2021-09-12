#Задание №1

def odd_nums(max_number=15):
    for i in range(1, max_number + 1, 2):
        yield i

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