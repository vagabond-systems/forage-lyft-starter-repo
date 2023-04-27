from batteryStrategy import IBatteryStrategy


class NubbinBattery(IBatteryStrategy):
    # last_service_date, current_date are date objects
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.service_threshold_age = 4

    def needs_service(self):
        if self.current_date.year - self.last_service_date.year > self.service_threshold_age:
            return True
        else:
            return False
