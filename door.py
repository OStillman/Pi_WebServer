import threading
from Hue import light_control as lights

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
            on_thread.start()
            off_motion_thread.start()

    def DoorClosed(self):
        print("Door Closed")
        if self.config['Devmode']['actions']:
            off_thread = threading.Thread(target=lights.SimpleLightsToggle, args=(self.config, "motion_sensor", self.config['LightSettings']['motion_sensor']['id'], True))
            off_thread.start()
