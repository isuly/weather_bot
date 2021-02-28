import telebot

bot = telebot.TeleBot('1689836173:AAEHmhMvTbRLslLvXVYh0WRJZD57q4L_2RE')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


bot.polling()
