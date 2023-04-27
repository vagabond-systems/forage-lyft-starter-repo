from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


class CarFactory():
    def __init__(self):
        self.car = Car()

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.car.engineStrategy = CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.car.batteryStrategy = SpindlerBattery(
            current_date=current_date, last_service_date=last_service_date)
        return self.car

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.car.engineStrategy = WilloughbyEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.car.batteryStrategy = SpindlerBattery(
            last_service_date=last_service_date, current_date=current_date)
        return self.car

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        self.car.engineStrategy = SternmanEngine(
            warning_light_is_on=warning_light_on)
        self.car.batteryStrategy = SpindlerBattery(
            last_service_date=last_service_date, current_date=current_date)
        return self.car

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.car.engineStrategy = WilloughbyEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.car.batteryStrategy = NubbinBattery(
            last_service_date=last_service_date, current_date=current_date)
        return self.car

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.car.engineStrategy = CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.car.batteryStrategy = NubbinBattery(
            last_service_date=last_service_date, current_date=current_date)
        return self.car
