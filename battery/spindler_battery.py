from .battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = last_service_date

    def needs_service(self):
        years = current_date.year - last_service_date.year

        if years < 2:
            return False
        else:
            return True
