from .tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_sensor_readings):
        self.tire_sensor_readings = tire_sensor_readings

    def needs_service(self):
        for tire in self.tire_sensor_readings:
            if tire >= 0.9:
                return True

        return False