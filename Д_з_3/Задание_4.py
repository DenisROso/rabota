#Задание №4

def arr_data(*args):
    return list(args)


def thesaurus_adv(*args, key_sort=False):
    names_dict = {}
    if key_sort:
        sorted_list = list(args)
        sorted_list.sort(key=lambda x: str(x).split(' ')[1])
        args = sorted_list
    for i in args:
        for name, surname in arr_data(str(i).split()):
            if surname[0] not in names_dict.keys():
                names_dict[surname[0]] = {}
                if names_dict[surname[0]].keys() not in (surname[0], name[0]):
                    names_dict[surname[0]][name[0]] = []
                    names_dict[surname[0]][name[0]] = list(filter(lambda x:
                                                                  str(x).split()[0][0].lower() == str(
                                                                      name[0]).lower() and
                                                                  str(x).split()[1][0].lower() == str(
                                                                      surname[0]).lower(),
                                                                  args)
                                                           )
            else:
                names_dict[surname[0]][name[0]] = []
                names_dict[surname[0]][name[0]] = list(filter(lambda x:
                                                              str(x).split()[0][0].lower() == str(name[0]).lower() and
                                                              str(x).split()[1][0].lower() == str(surname[0]).lower(),
                                                              args)
                                                       )
    return names_dict

print(thesaurus_adv("Игорь Петренко", "Арина Старцева", "Владимир Ильин", "Пётр Фёдоров", "Николай Валетов", "Александра Петрова",
                    "Юрий Борисов", "Виктория Суханова", key_sort=True))