from transliterate import to_cyrillic, to_latin
import telebot


TOKEN = '1560588494:AAG72gwCDvFXb_3VtsmFZLmqiX2ooaZU7ow'
bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or 

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Assalomu aleykum. Xush kelibsiz!\n\
							Kerakli matnni kiriting.")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "Agar muammoga duch kelsangiz @begbotov_shokir ga murojat qiling!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	msg = message.text
	if msg[0].isascii():
		javob = to_cyrillic(msg)
	else:
		javob = to_latin(msg)
	
	bot.reply_to(message, javob)


bot.polling()