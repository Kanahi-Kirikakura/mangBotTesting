import os
import telebot

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message, 
        "Привет! Я бот-пример.\n"
        "Доступные команды:\n"
        "/info - информация о боте"
    )

# Обработчик команды /info
@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, "Я создан на библиотеке pytelegrambotapi")

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()
