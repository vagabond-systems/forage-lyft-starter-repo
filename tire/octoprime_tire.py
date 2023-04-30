from tire.tireStrategy import TireStrategy


class OctoprimeTire(TireStrategy):
    def __init__(self, tire_values: list) -> None:
        self.tire_values = tire_values

    def needs_service(self):
        if sum(self.tire_values) >= 3:
            return True
        else:
            return False
