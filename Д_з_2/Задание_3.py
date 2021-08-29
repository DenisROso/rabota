#Задание №3

some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов', 'то', 'есть', 'выше',
             '-1', 'градуса']
some_list_as_text = ''
idx = 0

while idx < len(some_list):
    el = some_list[idx]
    if el.replace('+', '').replace('-', '').isdigit():
        some_list.insert(idx, '"')
        some_list[idx + 1] = some_list[idx + 1].replace(el, "%0.2d" % int(el))
        some_list_as_text = some_list_as_text + ' "' + some_list[idx + 1] + '"'
        some_list.insert(idx + 2, '"')
        idx += 3
    else:
        idx += 1
        some_list_as_text = some_list_as_text + ' ' + el

print(some_list_as_text)