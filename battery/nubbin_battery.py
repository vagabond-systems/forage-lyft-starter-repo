from battery import Battery
from datetime import date

class NubbinBattery(Battery):
    def __init__(self, current_date: date, last_service_date: date) -> None:
        self.__current_date = current_date
        self.__last_service_date = last_service_date
    def needs_service(self) -> bool:
        service_threshold_date = self.__last_service_date.replace(year=self.__last_service_date.year + 1)
        if self.__current_date > service_threshold_date:
            return True
        return False