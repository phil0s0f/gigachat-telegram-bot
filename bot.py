import telebot
import pprint
from config import TELEGRAM_TOKEN
from gigachat_client import send_request_to_gigachat
from history_manager import user_histories, Messages, MessagesRole

bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    user_histories[message.chat.id] = user_histories.default_factory()
    bot.send_message(message.chat.id, "Привет! Я бот-посредник для Гигачата. Задавай вопросы!")


@bot.message_handler(content_types=['text'])
def chat(message):
    user_id = message.chat.id
    user_history = user_histories[user_id]

    print(f'Пользователь {user_id} отправил запрос: {message.text}')
    pprint.pprint(user_history)

    user_history.messages.append(Messages(role=MessagesRole.USER, content=message.text))
    response_text = send_request_to_gigachat(user_history)
    user_history.messages.append(Messages(role=MessagesRole.ASSISTANT, content=response_text))

    pprint.pprint(vars(user_history))
    bot.reply_to(message, response_text)
    print(f'Пользователь {user_id} получил ответ: {response_text}')


if __name__ == "__main__":
    bot.polling()
