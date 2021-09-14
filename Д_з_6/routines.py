import json
import os
import uuid

def my_dictionary_ext(users_file, hobbys_file, results_file='', keep_clean=True):
    result_dict = {}
    with open(users_file, encoding='UTF8') as f:
        users_len = sum(1 for _ in f.readlines())
    with open(hobbys_file, encoding='UTF8') as f:
        hobbys_len = sum(1 for _ in f.readlines())

    if users_len < hobbys_len:
        raise ValueError

    with open(users_file, encoding='UTF8') as f:
        users_data = (' '.join(i.split(',')).rstrip() for i in f.readlines())

    with open(hobbys_file, encoding='UTF8') as f:
        hobby_data = (i.rstrip() for i in f.readlines())

    for i in range(0, users_len):
        user_line = next(users_data)
        if i < hobbys_len:
            hobby_line = next(hobby_data)
        else:
            hobby_line = None
        uid = str(uuid.uuid1())
        result_dict[uid] = {}
        result_dict[uid]['fn'] = user_line.split()[0]
        result_dict[uid]['ln'] = user_line.split()[1]
        result_dict[uid]['mn'] = user_line.split()[2]
        result_dict[uid]['hh'] = hobby_line

    if len(result_dict) >= 1:
        with open(results_file, 'w+') as f:
            json.dump(result_dict, f)

    if os.path.isfile(results_file) and keep_clean:
        os.remove(results_file)

    return result_dict


def isfloat(value):
    try:
        float(value)
        if len(value) > 24:
            print('Такую космическую сумму в булочной заработать невозможно!')
            return False
        return True
    except ValueError:
        return False


def normalize_write(input_string):
    while len(input_string) < 30:
        input_string = input_string + chr(0)
    input_string = input_string + chr(13)
    return input_string


def get_database_file():
    database = os.getcwd()
    if database[-1] != '\\':
        database = database + '\\'
    database = database + 'bakery.csv'
    return database