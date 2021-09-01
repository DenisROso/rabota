#Задание №2

def num_translate_adv(in_number):
    data = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if in_number[0].islower():
        return data.get(in_number.lower(), 'None').lower()
    else:
        return data.get(in_number.lower(), 'None').capitalize()

print(num_translate_adv('Nine'))