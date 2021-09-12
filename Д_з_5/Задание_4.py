#Задание №4

def int_filter(input_list=[]):
    for i in range(1, len(input_list)):
        if input_list[i - 1] < input_list[i]:
            yield input_list[i]

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = list(int_filter(src))
print(result)