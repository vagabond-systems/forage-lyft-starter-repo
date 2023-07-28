from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def need_service(self):
        return any(wear >= 0.9 for wear in self.tire_wear_array)