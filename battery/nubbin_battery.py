from battery.battery import Battery
from datetime import datetime


class NubbinBattery(Battery):
    def __init__(self, last_service_date: datetime) -> None:
        self.last_service_date = last_service_date

    # should be service every 4 years
    def battery_should_be_serviced(self) -> bool:
        today = datetime.today().date()
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return service_threshold_date < today
