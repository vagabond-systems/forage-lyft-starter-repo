from datetime import datetime
from engine.willoughby_engine import WilloughbyEngine
from battery.spindlerBattery import SpindlerBattery
from car import Car


class Glissade(Car):
    def __init(self, last_service_date, current_mileage):
        super().__init__(last_service_date, current_mileage)  # Call the constructors of parent classes
        self.current_date = datetime.today().date()
        self.engine =  WilloughbyEngine(last_service_date, current_mileage)
        self.battery = SpindlerBattery (last_service_date, self.current_date)

