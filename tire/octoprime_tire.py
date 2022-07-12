from .tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_sensor_readings):
        self.tire_sensor_readings = tire_sensor_readings

    def needs_service(self):
        total = sum(self.tire_sensor_readings)

        if total >= 3:
            return True
        else:
            return False