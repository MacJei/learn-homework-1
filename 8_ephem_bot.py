"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import settings
from datetime import datetime, date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context): 
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planet_position(update, context):
    current_dt = date.today()
    user_text = update.message.text
    text = user_text.split()[1]
    planets = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn','Uran','Neptune', 'Pluto']

    if text.lower().strip().capitalize() == 'Earth':
      update.message.reply_text("Информации о Земле нет")
    elif text.lower().strip().capitalize() in planets:
      planet_cls = getattr(ephem, text)
      planet = planet_cls(current_dt)
      constellation = ephem.constellation(planet)[-1]
      update.message.reply_text(f'Планета *{text.title()}* сегодня в созвездии *{constellation}*.', parse_mode='MARKDOWN')
    else:
      update.message.reply_text(f'Планета *{text.title()}* не нашлась, просьба проверить корректность ввода.')


def main():
  # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    #mybot = Updater(settings.API_KEY, use_context=True)
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

  # Процессинг
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler('planet', planet_position))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Started bot')
  # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
  # Запускаем бота, он будет работать, пока мы его не остановим принудительно  
    mybot.idle()

# Вызываем функцию main() - именно эта строчка запускает бота
if __name__ == "__main__":
    main()
