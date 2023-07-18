from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self, sensors):
        total_wear = sum(sensors)
        return total_wear >= 3