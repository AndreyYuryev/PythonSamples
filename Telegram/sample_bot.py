import telebot
from President_elections import calculate


TOKEN = r'1820999339:AAGTNpnvXO88WNmiVmO1whCpw84v_8uryWE'
# TOKEN = 'AAGTNpnvX088WNmiVm01whCpw84v_8uryWE'
bot = telebot.TeleBot(TOKEN)
# bot = telebot.TeleBot('1820999339:AAGTNpnvXO88WNmiVmO1whCpw84v_8uryWE')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    elif message.text.lower() == '123':
        calculate()
        bot.send_message(message.from_user.id, 'Вы ввели код.')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')

bot.polling(none_stop=True)