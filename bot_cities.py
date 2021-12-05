import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import keys_and_directories
import cities

logging.basicConfig(filename='bot.log', level=logging.INFO)
PROXY = {'proxy_url': keys_and_directories.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': keys_and_directories.PROXY_USERNAME, 'password': keys_and_directories.PROXY_PASSWORD}}

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def cities_game(update, context):
    cities_list = cities.file_read()
    user_text = update.message.text
    


def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)












def main():
    mybot = Updater(keys_and_directories.API_KEY, use_context=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()