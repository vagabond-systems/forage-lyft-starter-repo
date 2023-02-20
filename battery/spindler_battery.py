from .battery import Battery
from .utils import battery_service_year

class Spindler(Battery):

    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
    def needs_service(self):

        service_due = battery_service_year(self.last_service_date,2)

        return service_due < self.current_date
        