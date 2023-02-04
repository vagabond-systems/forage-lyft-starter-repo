from datetime import datetime, date

class Battery:
    def __init__(self, last_service_date: date, current_date:date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    def needs_service() -> bool:
        pass




# subclasses
class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date:date):
        super().__init__(last_service_date, current_date)

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return service_threshold_date < datetime.today().date()

class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date:date):
        super().__init__(last_service_date, current_date)

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return service_threshold_date < datetime.today().date()