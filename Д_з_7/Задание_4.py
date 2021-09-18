#Задание №4

import routines

my_dict = {}
cached_list = routines.folder_stat('..\\')

for i in cached_list:
    my_dict[i[2]] = sum(1 for x, y, z in routines.folder_stat('..\\') if i[2] == z)

print(my_dict)