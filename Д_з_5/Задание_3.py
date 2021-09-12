#Задание №3

def create_students_generator(list_of_students=[], list_of_classrooms=[]):
    while len(list_of_classrooms) < len(list_of_students):
        list_of_classrooms.append(None)
    for i, el in enumerate(list_of_students):
        yield list_of_students[i], list_of_classrooms[i]


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classrooms_list = ['9А', '7В', '9Б', '9В', '8Б', '10А']

test_gen = create_students_generator(tutors, classrooms_list)
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))
print(next(test_gen))