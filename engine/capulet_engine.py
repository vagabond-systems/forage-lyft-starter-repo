from serviceable import Serviceable

class CapuletEngine(Serviceable):
    def __init__(self, current_mileage):
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        return self.current_mileage >= 30000