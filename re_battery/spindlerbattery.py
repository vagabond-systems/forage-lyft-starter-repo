from year_to_date import add_years_to_date
from battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def need_services(self):
        date_which_battery_serviced_by = add_years_to_date(
            self.last_service_date + 2)
        if date_which_battery_serviced_by < self.current_date:
            return True
        else:
            return False
