from tire.Tire import Tire


class CarriganTires(Tire):
    def __init__(self, tires_array):
        self.tires_array = tires_array

    def needs_service(self):
        return any(tire >= 0.9 for tire in self.tires_array)
