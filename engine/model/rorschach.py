from datetime import datetime
from battery.nubbinBattery import NubbinBattery
from car import Car
from engine.willoughby_engine import WilloughbyEngine


class Rorschach(WilloughbyEngine):
    def __init(self, last_service_date, current_mileage):
        super().__init__(last_service_date, current_mileage)  # Call the constructors of parent classes
        self.current_date = datetime.today().date()
        self.engine =  WilloughbyEngine(last_service_date, current_mileage)
        self.battery = NubbinBattery (last_service_date, self.current_date)

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
