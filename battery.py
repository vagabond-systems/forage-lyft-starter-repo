from datetime import datetime
from serviceable import Serviceable

class Battery(Serviceable):
    @property
    def current_date(self) -> str:
        pass

    @current_date.setter
    def current_date(self, date) -> None:
        pass

    @property
    def last_service_date(self) -> str:
        pass

    @last_service_date.setter
    def last_service_date(self, date) -> None:
        pass

#########################################################################

class NubinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self._current_date = datetime.strptime(current_date, '%Y-%m-%d').date()
        self._last_service_date = datetime.strptime(last_service_date, '%Y-%m-%d').date()

    @property
    def current_date(self) -> str:
        return self._current_date

    @current_date.setter
    def current_date(self, date) -> None:
        self._current_date = date

    @property
    def last_service_date(self) -> str:
        return self._last_service_date

    @last_service_date.setter
    def last_service_date(self, date) -> None:
        self._last_service_date = date

    ## Calculated by adding 4 years to the last_service_date
    def next_service_date(self):
        return datetime(
            self.last_service_date.year + 4, 
            self.last_service_date.month, 
            self.last_service_date.day).date()

    ## Should be serviced once every 4 years
    def needs_service(self):
        return self._current_date >= self.next_service_date()

#########################################################################

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self._current_date = datetime.strptime(current_date, '%Y-%m-%d').date()
        self._last_service_date = datetime.strptime(last_service_date, '%Y-%m-%d').date()

    @property
    def current_date(self) -> str:
        return self._current_date

    @current_date.setter
    def current_date(self, date) -> None:
        self._current_date = date

    @property
    def last_service_date(self) -> str:
        return self._last_service_date

    @last_service_date.setter
    def last_service_date(self, date) -> None:
        self._last_service_date = date

    ## Calculated by adding 2 years to the last_service_date
    def next_service_date(self):
        return datetime(
            self.last_service_date.year + 2, 
            self.last_service_date.month, 
            self.last_service_date.day).date()

    ## Should be serviced once every 2 years
    def needs_service(self):
        return self._current_date >= self.next_service_date()