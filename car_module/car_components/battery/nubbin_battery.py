from car_module.car_components.battery.battery_interface import Battery
from datetime import date
from utils import add_years_to_date

class NubbinBattery(Battery):
    def __init__(self, current_date :date, last_service_date:date ):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self) ->bool:
        service_date = add_years_to_date(original_date=self.last_service_date,years_to_add=4)
        return service_date < self.current_date 
