from dateutil.parser import parse
import ephem


def is_date(string):
    if len(string) == 10:
        try:
            parse(string)
            return True
        except ValueError:
            return False
    else:
        return False


def is_planet(planet):
    planet_list = ['Mars', 'Mercury', 'Venus', 'Moon', 'Sun', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

    if planet.capitalize() in planet_list:
        return True
    else:
        return False


def planet_answer(text):

    user_text = text.split(' ')
    user_planet = user_text[1]
    user_date = user_text[2]

    if is_date(user_date) and is_planet(user_planet) is True:
        build_attribute = getattr(ephem, user_planet.capitalize())
        constellation = ephem.constellation(build_attribute(user_date))[1]
        return_date = parse(user_date).strftime("%d %B %Y ")
        return f'В заданный день {return_date} планета {user_planet} находилась в созвездии {constellation}'
    else:
        if is_date(user_date) is True:
            return 'Данная планета не найдена, возможно вы ошиблись при написании, попробуйте еще'
        else:
            return 'Неверный формат даты, введите дату в формате гггг.мм.дд'
