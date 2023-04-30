from tire.tireStrategy import TireStrategy


class CarriganTire(TireStrategy):
    def __init__(self, tire_values: list) -> None:
        self.tire_values = tire_values

    def needs_service(self):
        ctr: int = 0
        for i in self.tire_values:
            if i >= 0.9:
                ctr += 1
        if ctr >= 1:
            return True
        else:
            return False
