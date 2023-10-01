from engine.engine import Engine


class CapuletEngine(Engine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def service_needed(self):
        return self.current_mileage - self.last_service_mileage > 30000
