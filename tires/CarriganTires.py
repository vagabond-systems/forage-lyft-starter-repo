
class CarriganTires:
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        return any(wear >= 0.9 for wear in self.tire_wear)
