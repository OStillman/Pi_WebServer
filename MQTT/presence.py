import paho.mqtt.client as mqtt
from MQTT import db

class Presence():
    def __init__(self, member, status):
        self.member = member
        self.status = status

    def updateStatus(self):
        PresenceActions = db.PresenceActions()
        if PresenceActions.checkPresence(self.member, self.status) == False:
            self.sendMQTT()

    def fetchStatus(self):
        PresenceActions = db.PresenceActions()
        presence_data = PresenceActions.fetchPresence()
        print(presence_data)
        self.member = "kay"
        self.status = presence_data["kay"]
        self.sendMQTT()

        self.member = "owen"
        self.status = presence_data["owen"]
        self.sendMQTT()

    def sendMQTT(self):
        client = mqtt.Client("pi")
        client.connect("192.168.68.116")
        client.publish("presence/" + self.member, self.status)

    