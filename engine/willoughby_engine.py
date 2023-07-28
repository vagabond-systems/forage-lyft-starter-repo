from engine.engine import Engine

class WilloughbyEngine(Engine):
    def __init__(self, current_mileage):
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        return self.current_mileage >= 60000