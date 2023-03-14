import requests
from .models import TeleSettings


def send_telegram(tg_name, tg_phone):
    if TeleSettings.objects.get(pk=1):
        tg_settings = TeleSettings.objects.get(pk=1)
        token = str(tg_settings.tg_token)
        chat = str(tg_settings.tg_chat)
        message = str(tg_settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        if message.find('{') and message.find('}') and message.rfind('{') + message.rfind('}'):
            part_1 = message[0:message.find('{')]
            part_2 = message[message.find('}') + 1:message.rfind('{')]
            part_3 = message[message.rfind('}'):-1]

            message_slice = part_1 + tg_name + part_2 + tg_phone + part_3
        else:
            message_slice = message
        try:
            r = requests.post(method, data={
                'chat_id': chat,
                'text': message_slice,
            })
        except:
            pass
        finally:
            if r.status_code != 200:
                print('Ошибка отправки')
            elif r.status_code == 500:
                print('Ошибка сервера - 500')
            else:
                print('Все ОК сообщение отправлено')
    else:
        pass
