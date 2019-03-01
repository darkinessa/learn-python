# Создать список из словарей с оценками учеников разных классов школы вида
# [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

def listsum(list_content):
    list_sum = 0
    for i in list_content:
        list_sum = list_sum + i
    return list_sum


def listmerge(list_list):
    one_list = []
    for lst in list_list:
        one_list.extend(lst)
    return one_list


list_pupils = (
    [{'school_class': '1a', 'scores': [5, 4, 4, 5, 5, 5]}, {'school_class': '1b', 'scores': [3, 4, 4, 3, 2]},
     {'school_class': '2a', 'scores': [3, 5, 4, 5, 3]}, {'school_class': '2b', 'scores': [3, 3, 4, 4, 4, 5, 5]},
     {'school_class': '2v', 'scores': [3, 4, 3, 3, 5, 5, 2]}, {'school_class': '3a', 'scores': [4, 5, 4, 4, 5, 4]},
     {'school_class': '3b', 'scores': [3, 3, 2, 5, 3, 4]}, {'school_class': '4a', 'scores': [5, 5, 4, 5, 4]},
     {'school_class': '4b', 'scores': [3, 4, 4, 4, 5, 4]}, {'school_class': '4с', 'scores': [3, 4, 3, 3, 3]}])


all_school_score = []
all_class_scores = []

sum_score = 0
mid_class_score = 0
mid_school_score = 0

for i in list_pupils:
    all_class_scores = all_class_scores + i['scores']
    sum_score = listsum(all_class_scores)
    i['sum_score'] = sum_score

    mid_class_score = round(sum_score / len(i['scores']))
    i['mid_score'] = mid_class_score

    new_element = i['scores']
    all_school_score.append(new_element)

all_school_score = listmerge(all_school_score)
mid_school_score = listsum(all_school_score) / len(all_school_score)


print('Средняяя темпeратура по больничке: ', round(mid_school_score))
print()
print('Средняя темпeратура по каждому классу:')

for i in list_pupils:
    print(i['school_class'], '-', i['mid_score'])
