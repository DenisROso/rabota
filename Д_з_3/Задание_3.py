#Задание №3

def thesaurus(*args):

    names_dict = {}
    for i in sorted(args):
        if names_dict.keys() != i[0]:
            names_dict[i[0]] = list(sorted(filter(lambda x: str(x[0]).lower() == str(i[0]).lower(), args)))
    return names_dict


print(thesaurus("Катерина", "Анатолий", "Степан", "Игорь", "Василиса", "Константин", "Захар"))