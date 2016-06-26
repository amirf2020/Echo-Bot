# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

print "Python Bot By amir @alfroshotak [196560568]{sik}"
print "Kosgu Bot has been started."

import telebot

API_TOKEN = '<221733608:AAGRoU0BjSvLVOdtNd3KKJ8UKguO4bqOZvU>'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am Kos Goo Bot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!
Created By @alfroshotak\
""")

@bot.message_handler(commands=['credits', 'about'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am KosGu BOT
An Multi Purpose Telegram Bot Written In Python By @ArashEmp
Licenced Under Gnu General v.3 License!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.polling()
#ArashEmp
