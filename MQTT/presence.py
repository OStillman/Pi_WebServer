import paho.mqtt.client as mqtt
from MQTT import db

class Presence():
    def __init__(self, member, status):
        self.member = member
        self.status = status

    def updateStatus(self):
        PresenceActions = db.PresenceActions()
        if PresenceActions.checkPresence(self.member, self.status) == False:
            client = mqtt.Client("pi")
            client.connect("192.168.68.116")
            client.publish("presence/" + self.member, self.status)