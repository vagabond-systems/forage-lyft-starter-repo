import datetime
from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        current_date = datetime.datetime.now().date()
        return (current_date - self.last_service_date).days >= 1460  # 4 years in days