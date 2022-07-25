import telebot, config

bot = telebot.TeleBot(config.BOT_TOKEN)
users = config.USER()


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    if users.get(userId = message.from_user.id):
        bot.reply_to(message, "Salom do'stim")
    else:
        user = users.create(
            userId = message.from_user.id,
            name = message.from_user.first_name,
            username = message.from_user.username
        )
        if user:
            bot.reply_to(message, "Salom yangi do'stim")
        else: print("err")

bot.infinity_polling()