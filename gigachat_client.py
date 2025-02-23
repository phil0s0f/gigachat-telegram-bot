from gigachat import GigaChat
from config import GIGA_KEY

giga = GigaChat(credentials=GIGA_KEY, verify_ssl_certs=False)


def send_request_to_gigachat(chat_history):
    response = giga.chat(payload=chat_history)
    return response.choices[0].message.content
