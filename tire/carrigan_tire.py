from tire.tireStrategy import ITireStrategy


class CarriganTire(ITireStrategy):
    def __init__(self, tire_values: list) -> None:
        self.tire_values = tire_values

    def needs_service(self):
        ctr: int = 0
        for i in self.tire_values:
            if i >= 0.9:
                return True
        return False
