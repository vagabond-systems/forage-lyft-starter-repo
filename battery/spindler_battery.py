from battery.battery import Battery
from datetime import datetime


# serviced every 2 years
class SpindlerBattery(Battery):
    def __init__(self, last_service_date: datetime) -> None:
        self.__last_service_date = last_service_date

    # returns true if has been ovr 2 years since last service
    def needs_service(self) -> bool:
        service_threshold_date = self.__last_service_date.replace(year=self.__last_service_date.year + 2)
        return service_threshold_date < datetime.today().date()
