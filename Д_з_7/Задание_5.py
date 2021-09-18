#Задание №5

import json

import routines

folder_name = '..\\'
my_dict = {}
cached_list = routines.folder_stat(folder_name)

for i in cached_list:
    my_dict[i[2]] = sum(1 for x, y, z in cached_list if i[2] == z), list(
        set((x.split('.')[1] for x, y, z in cached_list if i[2] == z)))

with open('summary.json', 'w') as f:
    json.dump(my_dict, f)