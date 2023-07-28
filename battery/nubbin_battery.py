from battery.battery import Battery
from datetime import datetime


# serviced every 4 years
class NubbinBattery(Battery):
    def __init__(self, last_service_date) -> None:
        self._last_service_date = last_service_date

    # return true if it has been at least 4 years since last service date
    def needs_service(self) -> bool:
        today = datetime.today().date()
        service_threshold_date = self._last_service_date.replace(year=self._last_service_date.year + 4)
        return service_threshold_date < today
