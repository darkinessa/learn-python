# Написать функцию, которая принимает на вход две строки
# Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
# Если строки одинаковые, вернуть 1
# Если строки разные и первая длиннее, вернуть 2
# Если строки разные и вторая строка 'learn', возвращает 3
# Вызвать функцию несколько раз, передавая ей разные праметры и выводя на экран ршазультаты.


def string_compare(string_1, string_2):

    if isinstance(string_1, str) and isinstance(string_2, str):

        if string_1 == string_2:
            return 1

        elif len(string_1) > len(string_2):
            return 2

        elif string_2 == 'learn':
            return 3

        else:
            return "Смешная третья опция"

    else:
        return 0


input_string_1 = input("enter something: ")
input_string_2 = input("enter something: ")

print(string_compare(input_string_1, input_string_2))
print()

input_string_1 = input("enter something: ")
input_string_2 = float(input("enter number: "))

print(string_compare(input_string_1, input_string_2))
print()

input_string_1 = (1, 2, 3)
input_string_2 = input("enter something: ")

print(string_compare(input_string_1, input_string_2))
print()

input_string_1 = 'sss'
input_string_2 = 'learn'

print(string_compare(input_string_1, input_string_2))

