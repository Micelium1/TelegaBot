import telebot
from telebot import types
import cfg
import geo_api_use
import weather_api_use

bot = telebot.TeleBot(cfg.bot_key)
global text_reading_flag
text_reading_flag = False

@bot.message_handler(commands=['help','start'])
def commands(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/weather")
    markup.add(btn1)
    bot.send_message(message.from_user.id,"<b>Список команд</b>\n"
                                          "<i>/help</i> или <i>/start</i> - Вывод этого сообщения.\n"
                                          "<i>/weather</i> - работа с погодой\n"                                      
                                          "<i>/credits</i> - автор + ссылка на git", parse_mode='html',reply_markup=markup)
@bot.message_handler(commands=['credits'])
def credits(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Git', url='https://habr.com/ru/all/')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Работа выполнена Артовским Максимом", reply_markup=markup)
@bot.message_handler(commands=['weather'])
def weather(message):
    bot.send_message(message.from_user.id, "Введите название города на английском")
    global text_reading_flag
    text_reading_flag = True
@bot.message_handler(content_types=['text'])
def Get_weather(message):
    global text_reading_flag
    if text_reading_flag:
        try:
            coords = geo_api_use.get_coords(message.text)
            weather = weather_api_use.get_weather(coords)
            bot.send_message(message.from_user.id, f"Погода в городе {message.text}: \n{weather.weather}\nТемпература: {weather.temperature} градусов Цельсия\nНаправление ветра {weather.wind} м/c")
            text_reading_flag = False
        except Exception:
            bot.send_message(message.from_user.id, "Город либо введен неверно, либо его нету в базе данных")


bot.polling(none_stop=True)
