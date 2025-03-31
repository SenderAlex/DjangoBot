#@freelancer23_bot
import telebot
from telebot.types import Message
import requests


API_URL = 'http://127.0.0.1:8000/api'
BOT_TOKEN = 'bot_token'
REGISTRATION_LINK = 'http://127.0.0.1:8000/api/user/'

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message: Message):
    data = {
        "user_id": message.from_user.id,
        "username": message.from_user.username
    }
    response = requests.post(API_URL + '/registration', json=data)
    if response.status_code == 200:
        if response.json().get('message'):
            bot.send_message(message.chat.id, f'Пользователь с таким ID уже зарегистрирован')
        else:
            bot.send_message(message.chat.id, f"Ваш телеграм ID: <b>{response.json()['user_id']}</b>,\n"
                              f"Ваше имя: <b>{response.json()['username']}</b>\n"
                     f"Время создания: <b>{response.json()['created_at']}</b>\n"
                              f"Ваша ссылка: <b>{API_URL}/user/{message.from_user.id}/</b>", parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, 'Произошла ошибка при регистрации!!!')


@bot.message_handler(commands=['info'])
def user_info(message: Message):
    response = requests.get(f"{API_URL}/user/{message.from_user.id}/")  # почему post???
    if response.status_code == 200:
        bot.reply_to(message, f"Ваш телеграм ID: <b>{response.json()['user_id']}</b>,\n"
                              f"Ваше имя: <b>{response.json()['username']}</b>\n"
                     f"Время создания: <b>{response.json()['created_at']}</b>\n"
                              f"Ваша ссылка: <b>{API_URL}/user/{message.from_user.id}/</b>", parse_mode='HTML')
    elif response.status_code == 404:
        bot.send_message(message.chat.id, 'Вы не зарегистрированы!!')
    else:
        bot.send_message(message.chat.id, 'Непредвиденная ошибка!!!')


if __name__ == '__main__':
    bot.polling(none_stop=True)