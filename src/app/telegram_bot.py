import telebot

from app.config import BOT_ID
from app.weather import WeatherForecast
from app.core.users.models import get_user

bot = telebot.TeleBot(BOT_ID)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi! Im weather bot! \nSend me "weather" to get current weather!')


@bot.message_handler(content_types=['text'])
def get_current_weather(message):
    user = get_user(message.chat.username)
    if message.text.lower() == 'weather':
        if user:
            current_weather = WeatherForecast(city=user.city).get_current_weather()
            if not current_weather:
                bot.send_message(message.chat.id, 'Send me your city')
            bot.send_message(message.chat.id, current_weather)
        else:
            bot.send_message(message.chat.id, 'Send me your city')
    else:
        pass
        # user sends city
        # update users city in db


bot.polling()
