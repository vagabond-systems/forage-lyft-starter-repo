from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        for s in self.sensors:
            if s >= 0.9:
                return True

        return False
