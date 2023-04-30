from tire.tireStrategy import TireStrategy


class CarriganTire(TireStrategy):
    def __init__(self, tire_values) -> None:
        self.tire_values = tire_values

    def needs_service(self):
        pass
