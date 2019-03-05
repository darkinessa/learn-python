# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

pupil_list = ['Оля', 'Петя', 'Вася', 'Маша']

for pupil_name in pupil_list:
    print(pupil_name)
print()

# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.

pupil_list = ['Оля', 'Петя', 'Вася', 'Маша']
for pupil_name in pupil_list:
    print(pupil_name, len(pupil_name))
print()

# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

pupil_dict = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}

for pupil_name in pupil_dict:
    if pupil_dict[pupil_name] == False:
        print(pupil_name, 'Ура, я женщина!')
    else:
        print(pupil_name, 'Мальчик' )
print()

# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
  ['Оля', 'Петя', 'Вася', 'Маша', 'Паша', ' Cаша'],
  ['Няша']
]
print('Всего', len(groups), 'группы.')

for pupil in groups:
    amount_pupil = len(pupil)
    text = {'1': 'a', '2': 'ов'}
    text_1 = 'Всего в группе'
    text_2 = 'ученик'
    if amount_pupil == 1:
        print(text_1, amount_pupil, text_2)
    elif 1 < amount_pupil < 5:
        print(text_1, amount_pupil, (text_2+ text['1']))
    elif amount_pupil >= 5:
        print(text_1, amount_pupil, (text_2 + text['2']))
#print(f'{text_1} {amount_pupil} {text_2}ов')
print()


# Задание 5
# Для каждой паы учеников нужно с новой строки перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
#text = 'Группа '
i = 1
for pupil in groups:
    amount_pupil = len(pupil)
    #names_pupil = ', '.join(pupil)
    print(f"Группа {i}: {', '.join(pupil)}")

#print(text, i, ': ', ', '.join(pupil), sep='')
    i += 1


# ???