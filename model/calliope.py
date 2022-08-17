from datetime import datetime

from car import Car


class Calliope(Car):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.needs_service():
            return True
        else:
            return False
