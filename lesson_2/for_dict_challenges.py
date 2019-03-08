def most_name(list_name, key):
    name_list = {}
    for dict_name in list_name:
        name = dict_name[key]

        if name in name_list:
            name_list[name] += 1
        else:
            name_list[name] = 1
    return name


from collections import Counter

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

name_dict = {}
for item in students:
    name = item['first_name']
    if name in name_dict:
        cur_count = name_dict[name]
        name_dict[name] = cur_count + 1
    else:
        name_dict[name] = 1
for name in name_dict:
    print(f'{name}: {name_dict[name]}')

# Пример вывода:'''
# Вася: 1''
# Маша: 2'
# Петя: 2'
(print())

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
]
list_names = {}
cur_name = 0
search_name = None

for item in students:
    name = item['first_name']

    if name in list_names:
        list_names[name] += 1

    else:
        list_names[name] = 1

for name in list_names:

    if cur_name < list_names[name]:

        cur_name = list_names[name]
        often_name = cur_name
        search_name = name

    elif cur_name > list_names[name]:
        cur_name = cur_name

print(f'Самое частое имя среди учеников: {search_name}')

# Пример вывода:
# Самое частое имя среди учеников: Маша
print()

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Петя'},
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
        {'first_name': 'Вася'},
        {'first_name': 'Петя'},
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Петя'},
        {'first_name': 'Маша'},
    ],
    [
        {'first_name': 'Вася'},
        {'first_name': 'Петя'},
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
        {'first_name': 'Петя'},
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Петя'},
        {'first_name': 'Маша'},
        {'first_name': 'Петя'},
        {'first_name': 'Петя'},
        {'first_name': 'Петя'},
    ]
]
name_list = {}
name_list_current = []

i = 1
for list_group in school_students:
    x = 'first_name'
    text = 'Самое частое имя в классе'
    print(text, i, '-', most_name(list_group, x))
    i += 1

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '1b', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'},
                                 {'first_name': 'Маша'}, {'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '5b', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'},
                                 {'first_name': 'Миша'}, {'first_name': 'Миша'}, {'first_name': 'Оля'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???
print()
current_class = 0
list_students = 0

count_male = 0
count_fem = 0

for item_list in school:

    current_class = item_list['class']

    list_students = item_list['students']

    for item in list_students:
        name = item['first_name']
        if is_male[name] == False:
            count_fem += 1
        else:
            count_male += 1
    print(f'В классе {current_class} - {count_male} мальчка, {count_fem} девочки')
    count_fem = 0
    count_male = 0

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.'
# В классе 3c 0 девочки и 2 мальчика.
print()

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Оля'}]},
    {'class': '5b', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'},
                                 {'first_name': 'Миша'}, {'first_name': 'Миша'}, {'first_name': 'Оля'}]},

]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???

def maxClass(school_dict, sex_dict):
    max_male = 0
    max_fem = 0
    fem_max_sign = 0
    male_max_sign = 0
    for class_list in school_dict:
        cur_male_count = 0
        cur_fem_count = 0

        class_sign = class_list['class']
        name_list = class_list['students']
        for names in name_list:
            name = names['first_name']
            if sex_dict[name] is True:
                cur_male_count += 1
            else:
                cur_fem_count += 1

        if cur_male_count > max_male:
            max_male = cur_male_count
            male_max_sign = class_sign
        if cur_fem_count > max_fem:
            max_fem = cur_fem_count
            fem_max_sign = class_sign

    return male_max_sign, fem_max_sign


(male_sign, femal_sign) = maxClass(school, is_male)


print(f'Больше всего мальчиков в классе {male_sign}')
print(f'Больше всего девочек в классе {femal_sign}')

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

