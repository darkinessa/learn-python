# Попросить пользователя ввести возраст при помощи input  
# положить результат в переменную
# Написать функцию, которая по возрасту определит, 
# чем должен заниматься пользователь: 
# учиться в детском саду, школе, ВУЗе или работать
# Вызвать функцию, передав ей возраст пользователя и 
# положить результат работы функции в переменную
# Вывести содержимое переменной на экран

def isint(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False


def engaged_user(user_age):


    if isint(user_age):

        user_age = int(user_age)

        if user_age < 0:
            user_age = input('введите ваш возраст, целое число: ')
            return engaged_user(user_age)

        elif 0 <= user_age <= 6:
            return "Дошкольник"

        elif 6 < user_age <= 17:
            return "Школьник"

        elif 17 < user_age <= 22:
            return "Студент"

        elif 22 < user_age <= 65:
            return "Трудовой резерв"

        elif 65 < user_age < 101:
            return "Пенсионер"

        elif user_age >101:
            return 'MacLeod'


    else:
        user_age = input('введите ваш возраст, целое число: ')
        return engaged_user(user_age)

age_user = input('введите ваш возраст, целое число: ')

print(engaged_user(age_user))

