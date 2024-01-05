import requests

from .config import TELEGRAM_TOKEN

TELEGRAM_API_URL = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/'
MESSAGE_TEXTS = {
    'creation': "Your invitation link has been created successfully",
    'agreement': "Someone agreed to go out with you"
}


def send_telegram_message(chat_id, text_type):
    response = requests.post(
        TELEGRAM_API_URL + "sendMessage",
        {'chat_id': chat_id, 'text': MESSAGE_TEXTS[text_type]}
    )
    return response.json()['ok']

