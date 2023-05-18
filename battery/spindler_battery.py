from battery.battery import Battery
from datetime import timedelta

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        two_years_ago = self.current_date - timedelta(days=365*2)
        return two_years_ago > self.last_service_date