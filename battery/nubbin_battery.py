from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.service_threshold_date = last_service_date.replace(year=last_service_date.year + 4)

    def battery_should_be_serviced(self):
        return  self.service_threshold_date < self.current_date
