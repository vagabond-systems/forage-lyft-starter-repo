from datetime import datetime
from battery.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        current_date = datetime.today().date()
        return (current_date - self.last_service_date).days >= 1095  # 2 years in days
