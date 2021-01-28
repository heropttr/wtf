from logging import basicConfig
from os import W_OK
from pyowm.utils.config import get_default_config
from pyowm.utils import config
from pyowm.utils import config
import telebot
import pyowm
from telebot.apihelper import edit_message_text

config_dict = get_default_config()
config_dict['language'] = 'ru' 

owm = pyowm.OWM('bda3802e104b459f78de2c31711bf6b1')

bot = telebot.TeleBot("1507015068:AAELFQbesXGjTcp9IzZKMaH3-uPMP1r821w", parse_mode=None) 

@bot.message_handler(content_types=['text'])
def send_echo(message):
    
    mgr = owm.weather_manager()   
    observation = mgr.weather_at_place( message.text )
    w = observation.weather
    temp = w.temperature('celsius') ["temp"]
    
    answer = "В городе " + message.text + " сейчас " + w.detailed_status 
    answer += "\n" "Температура в городе: " + str(temp) + "\n"  
    
    bot.send_message(message.chat.id, answer)
bot.polling(none_stop = True )