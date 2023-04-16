from tire.tire import Tire

class OctoprimeTires(Tire):
    def __init__(self, sensors):
        self.sensors = sensors

    def need_service(self):
        sensor_counter = 0
        for x in self.sensors:
            sensor_counter += x
        return True if sensor_counter >= 3 else False