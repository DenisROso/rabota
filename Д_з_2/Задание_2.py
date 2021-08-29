#Задание №2

some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов', 'то', 'есть', 'выше',
             '-1']
digit_indices = []
some_list_as_text = ''

for idx, el in enumerate(some_list):
    el = el.replace('+', '').replace('-', '')
    if el.isdigit():
        digit_indices.append(idx)
        some_list[idx] = some_list[idx].replace(el, "%0.2d" % int(el))

for idx, el in enumerate(digit_indices):
    el = el + 2 * idx
    some_list.insert(el, '"')
    some_list.insert(el + 2, '"')
    digit_indices[idx] = el + 1

for i, txt in enumerate(some_list):
    if i - 1 in digit_indices or i in digit_indices:
        some_list_as_text = some_list_as_text + txt
    else:
        some_list_as_text = some_list_as_text + ' ' + txt

print(some_list_as_text)