from Shows import todayOutput
import paho.mqtt.client as mqtt

class ShowsToday():
    def __init__(self):
        pass

    def fetchToday(self):
        TodayOutput = todayOutput.TodayOutput()
        today_shows = TodayOutput.today
        self.sendMQTT(today_shows)


    def sendMQTT(self, today_shows):
        client = mqtt.Client("pi")
        client.connect("192.168.68.116")
        client.publish("today/shows", str(today_shows))