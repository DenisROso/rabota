import sys

from routines import *

if __name__ == "__main__":
    if len(sys.argv) > 1:
        new_income = sys.argv[1]
    else:
        new_income = input('Введите сумму продаж: \n')
else:
    new_income = ''

if isfloat(new_income):
    with open(get_database_file(), mode='a+', encoding='UTF8') as f:
        f.writelines(normalize_write(new_income))
else:
    print('Введите корректное значение (сумму продаж).')