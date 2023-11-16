from battery.Battery import Battery
from datetime import datetime


class SpindlerBattery(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.current_data = datetime.today().date()

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False


if __name__ == "__main__":
    today = datetime.today().date()
    last_service_date = today.replace(year=today.year - 5)
    print(last_service_date)
    nb = SpindlerBattery(last_service_date)
    print(nb.needs_service())
