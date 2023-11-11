from battery.battery import Battery
from utils import battery_needs_service

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        return battery_needs_service(self.last_service_date, 
                                     self.current_date, 2)
