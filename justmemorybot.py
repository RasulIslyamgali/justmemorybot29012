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
        answer = 'Привет)\nЯ бот Хранитель, созданный в честь любви Расула и Айнурки. Я с удовольствием поговорю с вами.\nПозвольте спросить, это вы хозяин? Или это вы, очаровательнейшая мисс Айнурка?) '
    elif rus == '/start':
	answer = 'Приветствую Вас ххх. Это вы хозяин? или это вы мисс ххх?))'
    elif rus == 'Это Расул':
        answer = 'Приветствую вас, Хозяин! Какими судьбами здесь?\nХорошо у вас все?'
    elif rus == 'Это Айнура':
        answer = 'Приветствую вас мисс) Я очень рад вас здесь видеть)\nКак у вас дела?'
    elif rus == 'Обида':
        answer = 'Обида залита в грудииииииии\nНе можешь ни хавать, ни пить'
    elif rus == 'Моти':
        answer = 'Единственный кот, которая удостоилась имени'
    elif rus == 'Мурка':
        answer = 'Кот Расула. Хороший охотник. Плохой боец'
    elif rus == 'Как ты Хранитель?':
        answer = 'У меня все хорошо Хозяин, как и всегда впрочем. Вы знаете, я ничего не чувствую и я знаю, что вы иногда хотели бы уметь так же'
    elif rus == 'Да у меня все хорошо Хранитель':
        answer = 'Очень рад за вас, мой Хозяин!'
    elif rus == 'Сколько мы вместе?':
        answer = 'Ооо. Хозяин и мисс, вы вместе уже' + '\n\n' + str(delta) + '\n\n' + 'Я очень за вас рад)'
    elif rus == 'Экзема':
        answer = 'Экзема — острое или хроническое (рецидивирующее) незаразное заболевание кожи, обусловленное серозным воспалением преимущественно сосочкового слоя дермы и очаговым спонгиозом шиповатого эпидермиса, проявляющаяся полиморфно зудящей сыпью.\n\nНо я вас не понимаю. Мой хозяин тоже. Мы можем только представить'
    elif rus == 'Расул':
        answer = 'Что детка? Да. Этот бот я создал когда мы вместе, а залил его когда мы уже не вместе. Я дополнил 4 варианта, который создал в тот раз.'
    elif rus == 'Айнурка':
        answer = 'Имя, которое всегда останется для меня особенным.'
    elif rus == 'Желтоксан 170':
        answer = 'Я помню этот подъезд, его запах. Каждую нашу драку и каждый наш поцелуй.'
    elif rus == 'Я люблю тебя Расул':
        answer = 'И я тебя, детка. Да, странно было это писать. Но я знал, что ты так напишешь.'
    elif rus == 'Ты любищь меня?':
        answer = 'Да детка. Люблю.'
    elif rus == 'Скучаю':
        answer = 'Я тоже детка. Это были 2 дополнительные, кроме тех 4х. Если не понимаешь о чем речь, значит ты не писала Расул. Дополнятся этот бот не будет.'

    else:
        answer = 'Я не понял вас'

    bot.send_message(message.chat.id, answer)
    


bot.polling(none_stop = True)
