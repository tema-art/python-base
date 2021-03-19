# Задание 3. Генератор объединения двух списков
# Есть два списка:
#
# ```
# tutors = [
#         'Иван', 'Анастасия', 'Петр', 'Сергей',
#         'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#         '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
# ```
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
#
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
#
# Количество генерируемых кортежей должно быть равно длине списка tutors. Если в списке klasses меньше элементов, чем в
# списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
# ```('Станислав', None)```
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких ситуациях
# генератор даст эффект. НЕ ОЧЕНЬ ПОНЯТНА СУТЬ ВОПРОСА

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

klass_list = tuple(zip(tutors, klasses))

print(klass_list)
print(type(klass_list))


def klass_stud():
    for i in klass_list:
        yield i


student = klass_stud()

print(type(student))
print(next(student))
print(next(student))
print(next(student))
print(next(student))
print(next(student))
print(next(student))
print(next(student))
print(next(student))
print(next(student))
print(next(student))
print(next(student))
print(next(student))
# def join(tutors, klasses):
#     yield [tuple(x) for x in join(tutors, klasses)]
#
#
# print(tutors, klasses)
