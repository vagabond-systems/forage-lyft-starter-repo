from dateutil.relativedelta import relativedelta

from battery import battery

class SpindlerBattery(battery.Battery):
    def __init__(self, current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        difference = relativedelta(self.current_date, self.last_service_date)

        return difference.years >= 2
