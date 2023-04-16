from tire.tire import Tire

class CarriganTires(Tire):
    def __init__(self, sensors):
        self.sensors = sensors

    def need_service(self):
        sensor_counter = 0
        for x in self.sensors:
            if x > 0.9:
                sensor_counter += 1
        return True if sensor_counter >= 1 else False