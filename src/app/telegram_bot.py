import telebot

from app.config import BOT_ID
from app.core.users.models import get_user, create_user, update_city
from app.weather import WeatherForecast

bot = telebot.TeleBot(BOT_ID)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi! Im weather bot! \nSend me "weather" to get current weather!')


@bot.message_handler(commands=['current_weather'])
def get_current_weather(message):
    user = get_user(message.chat.username)
    if user:
        current_weather = WeatherForecast(city=user.city).get_current_weather()
        if not current_weather:
            bot.send_message(message.chat.id, 'Send me your city')
        bot.send_message(message.chat.id, current_weather)
    else:
        new_user = create_user(message.chat.username, message.chat.name)
        if new_user:
            bot.send_message(message.chat.id, 'Send me your city')


@bot.message_handler(commands=['weather_forecast'])
def get_weather_forecast(message):
    pass


@bot.message_handler(content_types=['text'])
def update_user(message):
    user = get_user(message.chat.username)
    if user:
        update_city(user, message.text)
    else:
        user = create_user(message.chat.username, message.chat.name, message.text)
    current_weather = WeatherForecast(city=user.city).get_current_weather()
    if not current_weather:
        bot.send_message(message.chat.id, 'Send me your city')


bot.polling()
