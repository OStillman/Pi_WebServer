import threading
from Hue import light_control as lights
import notify

class DoorSensor:
    def __init__(self, data, config):
        self.data = data
        self.config = config
        if data['Sensor'] == "Front_Door":
            self.DoorToggle()

    def DoorToggle(self):
        if self.data['Status'] == "Open":
            self.DoorOpened()
        else:
            self.DoorClosed()

    
    def DoorOpened(self):
        print("Door Open")
        if self.config['Devmode']['actions']:
            on_thread = threading.Thread(target=lights.SimpleLightsToggle, args=(self.config, "group", self.config['LightSettings']['groups']['hallway'], True, self.config['LightSettings']['brightness']))
            off_motion_thread = threading.Thread(target=lights.SimpleLightsToggle, args=(self.config, "motion_sensor", self.config['LightSettings']['motion_sensor']['id'], False))
            notify_thread = threading.Thread(target=self.notify)
            on_thread.start()
            off_motion_thread.start()
            notify_thread.start()

    def DoorClosed(self):
        print("Door Closed")
        if self.config['Devmode']['actions']:
            off_thread = threading.Thread(target=lights.SimpleLightsToggle, args=(self.config, "motion_sensor", self.config['LightSettings']['motion_sensor']['id'], True))
            off_thread.start()

    def notify(self):
        pushoverSettings = self.config['PushoverSettings']
        url = pushoverSettings['general']['url']
        user_key = pushoverSettings['tokens']['user_key']
        app_token = pushoverSettings['tokens']['app_token']
        notify.Notify(url, app_token, user_key, "ALERT: Door Open")
