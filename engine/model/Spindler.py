
from EB import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date =current_date

    def engine_should_be_serviced(self):
        return self.current_date -  self.last_service_date>2


