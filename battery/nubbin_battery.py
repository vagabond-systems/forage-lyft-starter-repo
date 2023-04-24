from datetime import date
from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, current_date: date, last_service_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    def needs_service(self) -> bool:
        #  service interval was previously 180
        service_interval = 1460 # Service interval is six months
        days_since_service = (self.current_date - self.last_service_date).days
        return days_since_service >= service_interval
