#Задание №1

one_minute = 60
one_hour = 3600
one_day = 86400
one_week = 604800
one_month = 2630016
one_year = 31536000

duration = int (input('Укажите продолжительность в секундах: '))

if duration < one_minute:
    print('{} сек'.format(duration))
elif one_minute <= duration and one_hour > duration:
    my_minute = duration // one_minute
    my_second = duration % one_minute
    print('{} мин {} сек'.format(my_minute, my_second));
elif duration >= one_hour and duration < one_day:
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_minute = duration // one_minute
    my_second = duration % one_minute
    print('{} час {} мин {} сек'.format(my_hour, my_minute, my_second));
elif duration >= one_day and duration < one_week:
    my_day = duration // one_day
    duration = duration % one_day
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_minute = duration // one_minute
    my_second = duration % one_minute
    print('{} дн {} час {} мин {} сек'.format(my_day, my_hour, my_minute, my_second));
elif duration >= one_week and duration < one_month:
    my_week = duration // one_week
    duration = duration % one_week
    my_day = duration // one_day
    duration = duration % one_day
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_minute = duration // one_minute
    my_second = duration % one_minute
    print('{} нед {} дн {} час {} мин {} сек'.format(my_week, my_day, my_hour, my_minute, my_second));
elif duration >= one_month and duration < one_year:
    my_month = duration // one_month
    duration = duration % one_month
    my_week = duration // one_week
    duration = duration % one_week
    my_day = duration // one_day
    duration = duration % one_day
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_minute = duration // one_minute
    my_second = duration % one_minute
    print('{} мес {} нед {} дн {} час {} мин {} сек'.format(my_month, my_week, my_day, my_hour, my_minute, my_second));
elif duration >= one_year:
    my_year = duration // one_year
    duration = duration % one_year
    my_month = duration//one_month
    duration = duration % one_month
    my_week = duration // one_week
    duration = duration % one_week
    my_day = duration // one_day
    duration = duration % one_day
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_minute = duration // one_minute
    my_second = duration % one_minute
    print('{} год {} мес {} нед {} дн {} час {} мин {} сек'.format(my_year, my_month, my_week, my_day, my_hour, my_minute, my_second));
