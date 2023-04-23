from datetime import date
from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    def needs_service(self) -> bool:
        service_interval = 180 # Service interval is six months
        days_since_service = (self.current_date - self.last_service_date).days
        return days_since_service >= service_interval
