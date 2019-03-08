# нам приходит текст "/planet Mars"
# Мы разбиваем его на список используя метод .split(' ')
# Мы берем второй элемент списка
# Используя if мы выбираем какую планету просит пользователь и вызываем соответсвующий класс из ephem
# Высчитываем созвездие и отправляем пользователю в виде строки.

# Установите модуль ephem
# Добавьте в бота команду /planet, которая будет принимать на вход название планеты на английском, например /planet Mars
# В функции-обработчике команды из update.message.text получите название планеты (подсказка: используйте .split())
# При помощи условного оператора if и ephem.constellation научите бота отвечать, в каком созвездии сегодня находится планета.

#Реализуйте в боте команду, которая отвечает на вопрос “Когда ближайшее полнолуние?”
#Например /next_full_moon 2019-01-01. Чтобы узнать, когда ближайшее полнолуние, используйте ephem.next_full_moon(ДАТА)

import ephem

#func = getattr(ephem, planet_list)
#ephem.constellation(func())
print(ephem.constellation(ephem.Sun(2020-10-10)))

user_ask_planet = input('Введите название планеты (пример: /planet Mars): ').split(' ')
searching_date = input('Введите интересующую Вас дату в формате 2019/02/28: ')

requested_planet = user_ask_planet[1]

#planet_list = ({'Mars': 'ephem.Mars', 'Mercury': 'ephem.Mercury', 'Venus': 'ephem.Venus',
 #               'Earth': 'ephem.Earth', 'Jupiter': 'ephem.Jupiter', 'Saturn': 'ephem.Saturn',
     #           'Uranus': 'ephem.Uranus', 'Neptune': 'ephem.Neptune', 'Pluto': 'ephem.Pluto'})

planet_list = ['Mars', 'Mercury', 'Venus', 'Moon', 'Sun', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

def finding_constellation(planet, date):
    planet_list = ['Mars', 'Mercury', 'Venus', 'Moon', 'Sun', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
    if planet.capitalize() in planet_list:
        build_attribute = getattr(ephem, planet.capitalize())
        return ephem.constellation(build_attribute(date))
    else:
        return Данная планета не найдена, возможно вы ошиблись при написании


print(ephem.next_full_moon(searching_date))
print(finding_constellation(requested_planet, searching_date))
mars = ephem.Mars

#print(ephem.constellation(build_attribute(searching_date)))

