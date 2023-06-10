import telebot
from telebot import types


TOKEN = "2029450215:AAFMWMrJTjkz_wGfRAUcyiGIjvyxYTCi0TY"
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Це калькулятор двох одноцифрових чисел. Введіть приклад у форматі 3*8")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text[1] == '+':
        bot.reply_to(message, int(message.text[0]) + int(message.text[2]))
    
    elif message.text[1] == '-':
        bot.reply_to(message, int(message.text[0]) - int(message.text[2]))
    elif message.text[1] == '/':
        if int(message.text[2]) != 0:
            bot.reply_to(message, int(message.text[0]) / int(message.text[2]))
        else:
            bot.reply_to(message, "Не можна ділити на нуль!!")
    elif message.text[1] == '-':
	    bot.reply_to(message, int(message.text[0]) - int(message.text[2]))

def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)



bot.polling(none_stop=True, timeout=300)
