from model.car import Car
from engine.capulet_engine import CapuletEngine
from battery.splindler_battery import SplindlerBattery


class Calliope(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(
            engine=CapuletEngine(current_mileage, last_service_mileage),
            battery=SplindlerBattery(last_service_date),
        )
