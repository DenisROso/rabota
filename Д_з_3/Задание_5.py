#Задание №5

import random


def get_jokes_random_matrix(arr, one_per_joke):
    i = round(random.random() * 100) // 10 + 1
    if i > len(arr) - 1:
        i = len(arr) - 1
    out_str = arr[i]
    if one_per_joke:
        arr.remove(out_str)
    return out_str


def get_jokes(jokes_number=1, one_per_joke=True):
    result_arr = []
    nouns = ["арбуз", "пистолет", "валет", "камин", "кот", "конверт", "хомяк"]
    adverbs = ["зимой", "до обеда", "в два часа", "5го июня", "утром", "в полнолуние", "после дождичка в четверг"]
    verbs = ["был", "проснулся", "бултыхнётся", "стал", "может и будет", "появился", "бежит"]
    adjectives = ["неуклюжим", "милым", "мощным", "невиновным", "щекастым", "умелым", "заскорузлым"]
    while jokes_number > 0:
        result_arr.append(
            f'{get_jokes_random_matrix(nouns, one_per_joke)} '
            f'{get_jokes_random_matrix(adverbs, one_per_joke)} '
            f'{get_jokes_random_matrix(verbs, one_per_joke)} '
            f'{get_jokes_random_matrix(adjectives, one_per_joke)}')

        jokes_number = jokes_number - 1
        if len(nouns) == 0 or len(adverbs) == 0 or len(verbs) == 0 or len(adjectives) == 0:
            jokes_number = 0
    return result_arr

print(get_jokes(7, one_per_joke=True))
print(get_jokes())
print(get_jokes(2, False))