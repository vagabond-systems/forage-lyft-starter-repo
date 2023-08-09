from tire.tire import Tire


class OctoPrimeTire(Tire):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        s = sum(self.sensors)
        if s >= 3:
            return True
        return False


