import os
import telebot
from analiz import image_analize


bot = telebot.TeleBot("Bot key")


chat_states = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    if chat_id not in chat_states:
        bot.reply_to(message, "Привет! Отправь мне изображение для анализа.")
        chat_states[chat_id] = "waiting_for_image"

@bot.message_handler(content_types=['photo'])
def handle_image(message):
    try:
        chat_id = message.chat.id
        if chat_id in chat_states and chat_states[chat_id] == "waiting_for_image":
            file_id = message.photo[-1].file_id
            file_info = bot.get_file(file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            file_extension = os.path.splitext(file_info.file_path)[1]
            file_name = f'image{file_extension}'
            with open(file_name, 'wb') as new_file:
                new_file.write(downloaded_file)
            result = image_analize(file_name)
            bot.reply_to(message, result)
            os.remove(file_name)
        else:
            bot.reply_to(message, "Пожалуйста, отправьте изображение в правильном контексте.")
    except Exception as e:
        print(e)
        bot.reply_to(message, "Произошла ошибка при обработке изображения")

bot.polling()

