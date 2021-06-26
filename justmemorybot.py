#justmemorybot

import telebot
import datetime


bot = telebot.TeleBot("1635598859:AAHYNzlUCM6AG2JLfDQieaMFyjNXqPzvpGQ")

today = datetime.date.today() 
last_year = datetime.date(2018, 9, 21)
delta = today - last_year 

@bot.message_handler(content_types=['photo'])
def text_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Да, Хозяин. Это красиво. Завидую вам белой завистью))')

@bot.message_handler(content_types=['text'])
def echo_all(message):
	#bot.reply_to(message, message.text)
    #bot.send_message(message.chat.id, message.text)

    rus = message.text

    if rus == 'Привет':
        answer = 'some answer'
    elif rus == 'Ты кто?':
	answer = 'some answer'
    else:
        answer = 'Я не понял вас'

    bot.send_message(message.chat.id, answer)
    


bot.polling(none_stop = True)
