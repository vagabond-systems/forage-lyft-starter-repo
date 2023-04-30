from battery.batteryStrategy import IBatteryStrategy


class SpindlerBattery(IBatteryStrategy):
    # last_service_date, current_date are date objects
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.service_threshold_age = 3
        self.service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + self.service_threshold_age)

    def needs_service(self):
        if self.current_date >= self.service_threshold_date:
            return True
        else:
            return False
