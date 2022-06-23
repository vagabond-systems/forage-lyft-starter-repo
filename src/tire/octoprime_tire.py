from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        return sum(self.sensors) >= 3
