from model.car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery


class Rorschach(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(
            engine=WilloughbyEngine(current_mileage, last_service_mileage),
            battery=NubbinBattery(last_service_date),
        )
