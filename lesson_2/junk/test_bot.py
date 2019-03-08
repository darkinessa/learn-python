# Установите модуль ephem
# Добавьте в бота команду /planet, которая будет принимать на вход название планеты на английском, например /planet Mars
# В функции-обработчике команды из update.message.text получите название планеты (подсказка: используйте .split())
# При помощи условного оператора if и ephem.constellation научите бота отвечать, в каком созвездии сегодня находится планета.


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings_bot
import ephem


PROXY = {'proxy_url': 'socks5å//t1.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def greet_user(bot, update):
    print('Вызван /start')
    print(update)
å

def talk_to_me(bot, update):
    # нам приходит текст "/planet Mars"
    # Мы разбиваем его на список используя метод .split(' ')
    # Мы берем второй элемент списка
    # Используя if мы выбираем какую планету просит пользователь и вызываем соответсвующий класс из ephem
    # Высчитываем созвездие и отправляем пользователю в виде строки.

    planet_list = [Mars, Mercury, Venus, Earth, Jupiter, Saturn, Uranus, Neptune, Pluto]
    if update.message.text.split('/planet') in planet_list:
        print(update.message.ephem.constellation.update.message.text.split('/planet'))
    else:
        print(user_text)
        update.message.reply_text(user_text)

def say_me_constellation(bot, update):
    planet_list = [Mars, Mercury, Venus, Earth, Jupiter, Saturn, Uranus, Neptune, Pluto]


def main():
    mybot = Updater(settings_bot.SECRET_BOT_KEY, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()
