import domain.car
from datetime import datetime 

class SpindlerBattery(car):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
