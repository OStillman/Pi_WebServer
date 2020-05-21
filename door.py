import threading
import constants
from Hue import light_control as lights

class DoorSensor:
    def __init__(self, data):
        self.data = data
        if data['Sensor'] == "Front_Door":
            self.DoorToggle()

    def DoorToggle(self):
        if self.data['Status'] == "Open":
            self.DoorOpened()
        else:
            self.DoorClosed()

    
    def DoorOpened(self):
        print("Door Open")
        if not constants.__DevMode__:
            on_thread = threading.Thread(target=lights.SimpleLightsToggle, args=("group", constants.hallway, True, constants.hallway_brightness))
            off_motion_thread = threading.Thread(target=lights.SimpleLightsToggle, args=("motion_sensor", constants.motion_sensor_id, False))
            on_thread.start()
            off_motion_thread.start()

    def DoorClosed(self):
        print("Door Closed")
        if not constants.__DevMode__:
            off_thread = threading.Thread(target=lights.SimpleLightsToggle, args=("motion_sensor", constants.motion_sensor_id, True))
            off_thread.start()
