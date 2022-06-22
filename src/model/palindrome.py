from model.car import Car

from battery.splindler_battery import SplindlerBattery
from engine.sternman_engine import SternmanEngine


class Palindrome(Car):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(
            engine=SternmanEngine(warning_light_is_on),
            battery=SplindlerBattery(last_service_date),
        )
