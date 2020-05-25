import requests

class Notify:
    def __init__(self, url, app_token, user_key, message):
        self.message = message
        self.url = url
        self.app_token = app_token
        self.user_key = user_key
        self.send_message()

    def send_message(self):
        requests.post(self.url, data = {
            "token": self.app_token,
            "user": self.user_key,
            "message": self.message
        })