# Напишите функцию get_summ(num_one, num_two), которая принимает на вход два целых числа (int) и складывает их
# Оба аргумента нужно приводить к целому числу при помощи int() и
# перехватывать исключение ValueError если приведение типов не сработало


def get_summ(num_one, num_two):

    try:
        int(num_one) + int(num_two)
        return int(num_one) + int(num_two)
    except ValueError:
        return 'Числа не числа, проверьте правильность ввода'


x = input('введите число: ')
y = input('введите число: ')

print(get_summ(x,y))
