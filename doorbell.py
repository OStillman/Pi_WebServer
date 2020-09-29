import os
import notify
import paho.mqtt.client as mqtt

class Doorbell():
    def __init__(self, data):
        self.doorbell = data["which"]
        self.ringBell()
        self.notify()

    def ringBell(self):
        #os.system("aplay -D bluealsa /home/pi/Documents/Dev/Dingdong.wav")
        broker_address="192.168.68.116"
        client = mqtt.Client("doorbell") #create new instance
        client.connect(broker_address) #connect to broker
        client.publish("doorbell/back","Pressed")#publish


    def notify(self):
        notify.Notify(title="DING DONG", message="{} is ringing!".format(self.doorbell))