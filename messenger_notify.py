import requests

class Notify:
    def __init__(self, message, recipient, page_token, url):
        self.message = message
        self.recipient = recipient
        self.page_token = page_token
        self.url = url
        self.respond()

    def respond(self):
        self.message = self.get_bot_response()
        self.send_message()

    def get_bot_response(self):
        return "ALERT: {}".format(self.message)

    def send_message(self):
        payload = {
            'message': {
                'text': self.message
            },
            'recipient': {
                'id': self.recipient
            },
            'notification_type': 'regular'
        }

        auth = {
            'access_token': self.page_token
        }

        requests.post(
            self.url,
            params=auth,
            json=payload
        )