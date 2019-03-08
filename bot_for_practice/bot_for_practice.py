import ephem
import settings_bot
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text()
    print(text)
    print(update)


def help_me(bot, update):
    text = 'Вызван /help_me'
    logging.info(text)
    text_help_planet = 'Что бы узнать в каком созвездии была выбранная планета, набери команду /planet, введи название' \
                       ' планеты на английском языке и дату в формете ГГГГ/ММ/ДД.\nНапример /planet Mars 2020/12/31'

    update.message.reply_text(text_help_planet)


def planet(bot, update):
    text = 'Вызван /planet'

    text_planet = 'веди название планеты на английском языке и дату в формете ГГГГ/ММ/ДД.\n' \
                  'Например /planet Mars 2020/12/31'

    logging.info(text)

    logging.info(update.message.text)

    text_answer = planet_answer(update.message.text)
    # logging.info(text_answer)

    print(text)
    print(update)

    update.message.reply_text(text_answer)


def planet_answer(text):
    user_text = text.split(' ')
    user_planet = user_text[1]
    user_date = user_text[2]

    logging.info(user_planet)
    logging.info(user_date)

    return finding_constellation(user_planet, user_date)[1]


def finding_constellation(planet, date):
    planet_list = ['Mars', 'Mercury', 'Venus', 'Moon', 'Sun', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

    if planet.capitalize() in planet_list:
        build_attribute = getattr(ephem, planet.capitalize())
        return ephem.constellation(build_attribute(date))
    else:
        return 'Данная планета не найдена, возможно вы ошиблись при написании, попробуйте еще'


def talk_to_me(bot, update):
    user_text = update.message.text

    text_hello = 'Привет, я Астробот!\nЯ могу рассказать когда будет ближайшее новолоние или каком созвездии ' \
                 'находится интересующая тебя планета. \nНажми /help что бы узнать что я могу.'

    print(user_text)
    text = 'Привет'
    update.message.reply_text(text_hello)


def main():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                        level=logging.INFO,
                        filename='bot.log')

    astro_bot = Updater(settings_bot.BOT_KEY, request_kwargs=settings_bot.PROXY)

    logging.info('Запуск прошел успешно')

    dispatcher = astro_bot.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_me))
    dispatcher.add_handler(CommandHandler("planet", planet))
    dispatcher.add_handler(MessageHandler(Filters.text, talk_to_me))

    astro_bot.start_polling()
    astro_bot.idle()


if __name__ == '__main__':
    main()
