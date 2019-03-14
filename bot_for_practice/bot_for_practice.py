import bot_planet
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
                       ' планеты на английском языке и дату в формете ГГГГ-ММ-ДД.\nНапример /planet Mars 2020-12-31'

    update.message.reply_text(text_help_planet)


def planet(bot, update):
    text = 'Вызван /planet'

    logging.info(text)

    logging.info(update.message.text)

    text_answer = bot_planet.planet_answer(update.message.text)

    print(text)
    print(update)

    update.message.reply_text(text_answer)


def talk_to_me(bot, update):
    user_text = update.message.text

    text_hello = 'Привет, я Астробот!\nЯ могу рассказать когда будет ближайшее новолоние или каком созвездии ' \
                 'находится интересующая тебя планета. \nНажми /help что бы узнать что я могу.'

    print(user_text)

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
