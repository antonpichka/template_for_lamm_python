import telebot
from library_architecture_mvvm_modify_python import BaseModelRepository, EnumRWTMode

BaseModelRepository.enum_rwt_mode = EnumRWTMode.TEST
bot = telebot.TeleBot("YOUR_BOT_TOKEN")

@bot.message_handler(commands=["start"])
def send_welcome(message: telebot.types.Message) -> None:
	bot.reply_to(message, "Howdy, how are you doing?")

bot.infinity_polling()