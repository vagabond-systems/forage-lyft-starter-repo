from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, wornArr):
        self.sum = sum(wornArr)

    def tire_should_be_serviced(self):
        return self.sum >= 0.9
