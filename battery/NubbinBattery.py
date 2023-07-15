from battery.IBattery import IBattery


class NubbinBattery(IBattery):

    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date, current_date)

    def needs_service(self):
        difference_in_years = self.get_current_date().year - self.get_last_service_date().year
        return difference_in_years % 4 == 0
