import os
import telebot
from telebot import types
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message, 
        "Привет! Я бот-пример.\n"
        "Доступные команды:\n"
        "/help - помощь\n"
        "/info - информация о боте"
    )

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(
        message,
        "Вот что я умею:\n"
        "- Отвечать на текстовые сообщения\n"
        "- Обрабатывать кнопки\n"
        "Просто напиши мне что-нибудь!"
    )

# Обработчик команды /info
@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, "Я создан на библиотеке pytelegrambotapi")

# Обработчик обычных текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user_text = message.text
    user_name = message.from_user.first_name
    
    response = f"{user_name}, ты написал: {user_text}"
    bot.reply_to(message, response)

# Пример с кнопками
@bot.message_handler(commands=['menu'])
def show_menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('Кнопка 1')
    btn2 = types.KeyboardButton('Кнопка 2')
    btn3 = types.KeyboardButton('Кнопка 3')
    markup.add(btn1, btn2, btn3)
    
    bot.send_message(
        message.chat.id,
        "Выберите опцию:",
        reply_markup=markup
    )

# Обработка нажатий на кнопки
@bot.message_handler(func=lambda message: message.text in ['Кнопка 1', 'Кнопка 2', 'Кнопка 3'])
def handle_buttons(message):
    if message.text == 'Кнопка 1':
        bot.reply_to(message, "Вы нажали Кнопку 1!")
    elif message.text == 'Кнопка 2':
        bot.reply_to(message, "Вы нажали Кнопку 2!")
    elif message.text == 'Кнопка 3':
        bot.reply_to(message, "Вы нажали Кнопку 3!")

# Инлайн-кнопки (под сообщением)
@bot.message_handler(commands=['inline'])
def inline_buttons(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Да", callback_data="yes")
    btn2 = types.InlineKeyboardButton("Нет", callback_data="no")
    markup.add(btn1, btn2)
    
    bot.send_message(
        message.chat.id,
        "Вы согласны?",
        reply_markup=markup
    )

# Обработчик нажатий на инлайн-кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "yes":
        bot.answer_callback_query(call.id, "Вы выбрали Да!")
        bot.edit_message_text(
            "✅ Вы согласились!",
            call.message.chat.id,
            call.message.message_id
        )
    elif call.data == "no":
        bot.answer_callback_query(call.id, "Вы выбрали Нет!")
        bot.edit_message_text(
            "❌ Вы отказались!",
            call.message.chat.id,
            call.message.message_id
        )

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()
