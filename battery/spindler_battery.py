from battery.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def service_needed(self):
        service_date = self.last_service_date + (2*365)
        if self.current_date > service_date:
            return True
        else:
            return False