from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    updater = Updater("500759412:AAEP5H411ssukLTTahklXqYq6tt2hj2r5gI")


    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))



    updater.start_polling()
    updater.idle()


#def greet_user(bot, update):
#    print('Вызван /start')


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    logging.info(user_text)
    update.message.reply_text(user_text)


main()



















