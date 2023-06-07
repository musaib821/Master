import telebot 

#bot=telebot.TeleBot(token)

#@bot.message_handler(import telebot

API_TOKEN = '5699136129:AAE_Cd0DlRUHlGExGFpJJ_pxhvcFpS5q_6Q'

bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(func=lambda message: True)

def echo_message(message):

    bot.reply_to(message, "This bot has been changed to @buttonize_bot. Please use that bot instead")

bot.infinity_polling()
