import requests


class Telegram:

    def __init__(self, token:str='', chat_id:str=''):
        self.token = token
        self.chat_id = chat_id
        return

    def __call__(self, text:str):
        requests.get(f'{self.url}={text}')
        return

    @property
    def url(self) -> str:
        return f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.chat_id}&text"
