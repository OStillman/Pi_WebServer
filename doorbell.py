import os
import notify

class Doorbell():
    def __init__(self, data):
        self.doorbell = data["which"]
        self.ringBell()
        self.notify()

    def ringBell(self):
        os.system("aplay -D bluealsa /home/pi/Documents/Dev/Dingdong.wav")

    def notify(self):
        notify.Notify(title="DING DONG", message="{} is ringing!".format(self.doorbell))