from datetime import date
from battery.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, current_date: date, last_service_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    def needs_service(self) -> bool:
        service_interval = 365 * 2 # Service interval is one year
        days_since_service = (self.current_date - self.last_service_date).days
        print(days_since_service, self.last_service_date, self.current_date)
        return days_since_service >= service_interval