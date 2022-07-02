from battery.battery import Battery
from datetime import datetime


class NubbinBattery(Battery):
    def __init__(self, last_service_date: datetime) -> None:
        self._last_service_date = last_service_date

    # should be service every 4 years
    def needs_service(self) -> bool:
        today = datetime.today().date()
        service_threshold_date = self._last_service_date.replace(year=self._last_service_date.year + 4)
        return service_threshold_date < today
