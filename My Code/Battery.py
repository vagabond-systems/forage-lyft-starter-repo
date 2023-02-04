from datetime import datetime

class Battery:
    def __init__(last_service_date: date, current_date:date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    def needs_service() -> bool:
        pass




# subclasses
class SpindlerBattery(Battery):
    def __init__(last_service_date: date, current_date:date):
        super().__init__(last_service_date, current_date)

    def needs_service() -> bool:
        pass

class NubbinBattery(Battery):
    def __init__(last_service_date: date, current_date:date):
        super().__init__(last_service_date, current_date)

    def needs_service() -> bool:
        pass