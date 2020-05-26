import requests
import yaml

class Notify:
    def __init__(self, title, message):
        self.message = message
        self.title = title
        self.getConfig()
        self.applyConfig()
        self.send_message()

    def send_message(self):
        r = requests.post(self.url, data = {
            "token": self.app_token,
            "user": self.user_key,
            "title": self.title,
            "message": self.message,
        })
        print(r.content)

    def getConfig(self):
        config_file = open(file='constants.yaml', mode='r')
        self.config = yaml.load(config_file, Loader=yaml.FullLoader)["PushoverSettings"]
        config_file.close()

    def applyConfig(self):
        self.url = self.config["general"]["url"]
        self.app_token = self.config["tokens"]["app_token"]
        self.user_key = self.config["tokens"]["user_key"]
        print(self.url)
