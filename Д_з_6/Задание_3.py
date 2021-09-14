import json
import os

def my_dictionary(users, hobby):
    result_dict = {}
    user_list = list(users)
    hobby_list = list(hobby)
    if len(hobby_list) > len(user_list):
        raise ValueError
    while len(hobby_list) < len(user_list):
        hobby_list.append(None)
    for i, el in enumerate(user_list):
        result_dict[el] = hobby_list[i]
    return result_dict

with open('users.csv', encoding='UTF8') as f:
    users_data = (' '.join(i.split(',')).rstrip() for i in f.readlines())

with open('hobby.csv', encoding='UTF8') as f:
    hobby_data = (i.rstrip() for i in f.readlines())

my_dict = my_dictionary(users_data, hobby_data)

print(my_dict)

with open('saved_data.dat', 'w+') as f:
    json.dump(my_dict, f)

my_dict = {}
with open('saved_data.dat') as f:
    print(json.load(f))

if os.path.isfile('saved_data.dat'):
    os.remove('saved_data.dat')