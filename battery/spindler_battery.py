from battery.battery import Battery
from datetime import datetime


class SpindlerBattery(Battery):
    def __init__(self, last_service_date: datetime) -> None:
        self.__last_service_date = last_service_date

    # should be service every two years
    def needs_service(self) -> bool:
        service_threshold_date = self.__last_service_date.replace(year=self.__last_service_date.year + 2)

        return service_threshold_date < datetime.today().date()
