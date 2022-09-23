from abc import ABC, abstractmethod
from datetime import datetime
from utils import add_years_to_date

class Battery(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

#########################################################################

class NubinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = datetime.strptime(current_date, '%Y-%m-%d').date()
        self.last_service_date = datetime.strptime(last_service_date, '%Y-%m-%d').date()

    ## Should be serviced once every 4 years
    def needs_service(self) -> bool:
        next_service_date = add_years_to_date(self.last_service_date, 4)
        return self.current_date >= next_service_date

#########################################################################

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = datetime.strptime(current_date, '%Y-%m-%d').date()
        self.last_service_date = datetime.strptime(last_service_date, '%Y-%m-%d').date()

    ## Should be serviced once every 2 years
    def needs_service(self) -> bool:
        next_service_date = add_years_to_date(this.last_service_date, 2)
        return self.current_date >= next_service_date