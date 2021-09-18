#Задание №3

from routines import *

process_path('config_clean_trash.yaml')
process_path('config_l2.yaml')
process_path('config_l3.yaml')
gen = ((dir_path, dir_names, file_names) for dir_path, dir_names, file_names in os.walk(".\my_project") if
       dir_path.split('\\')[-1] == 'templates')

task_list = list(gen)
action_list = []
target_dir = ''

for i in task_list:
    if len(i[1]) == 0:
        target_dir = i[0]

for i in task_list:
    if len(i[1]) > 0:
        action_list.append([target_dir + '\\' + ''.join(i[1]), i[0] + '\\' + ''.join(i[1])])

for i in action_list:
    shutil.copytree(i[1], i[0])