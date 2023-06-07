from datetime import date, timedelta

class SpindlerBattery:
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_interval = timedelta(days=1095)  # Three years interval
        return self.current_date - self.last_service_date >= service_interval
