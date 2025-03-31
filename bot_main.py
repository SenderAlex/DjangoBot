#@freelancer23_bot
import telebot
from telebot.types import Message
import requests


API_URL = 'http://127.0.0.1:8000/api'
BOT_TOKEN = 'BOT TOKEN'

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message: Message):
    data = {
        "user_id": message.from_user.id,
        "username": message.from_user.username
    }
    response = requests.post(API_URL + '/registration', json=data)  # почему post???
    if response.status_code == 200:
        if response.json().get('message'):
            bot.send_message(message.chat.id, 'Пользователь с таким именем уже зарегистрирован')
        else:
            bot.send_message(message.chat.id, f'Вы успешно зарегистрированы!! Ваш уникальный номер '
                                              f'{response.json()['id']}')
    else:
        bot.send_message(message.chat.id, 'Произошла ошибка при регистрации!!!')
        print(response.json())
        print(response.status_code)
        print(response.text)


@bot.message_handler(commands=['info'])
def user_info(message: Message):
    response = requests.get(f"{API_URL}/user/{message.from_user.id}/")  # почему post???
    if response.status_code == 200:
        bot.reply_to(message, f"Ваша регистрация: \n Ваш телеграм ID {response.json()['user_id']} \n "
                              f"Ваше имя {response.json()['username']}")
    elif response.status_code == 404:
        bot.send_message(message.chat.id, 'Вы не зарегистрированы!!')
    else:
        bot.send_message(message.chat.id, 'Непредвиденная ошибка!!!')


if __name__ == '__main__':
    bot.polling(none_stop=True)