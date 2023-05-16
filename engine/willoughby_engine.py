from engine import Engine

class WilloughbyEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        super().__init__(current_mileage, last_service_mileage)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
