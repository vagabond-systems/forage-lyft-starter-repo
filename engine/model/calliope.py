from datetime import datetime

from engine.capulet_engine import CapuletEngine
from battery.spindlerBattery import SpindlerBattery
from car import Car

class Calliope(Car):

    def __init(self, last_service_date, current_mileage):
        super().__init__(last_service_date, current_mileage)  # Call the constructors of parent classes
        self.current_date = datetime.today().date()
        self.engine = CapuletEngine (last_service_date, current_mileage)
        self.battery = SpindlerBattery (last_service_date, self.current_date)