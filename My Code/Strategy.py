from Car import *

class Serviceable:
    def needs_service() -> bool:
        return Car.needs_service()