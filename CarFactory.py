from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class CarFactory:
    def create_calliope(self, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)

    def create_glissade(self, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)

    def create_palindrome(self, last_service_date, warning_light_is_on):
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        battery = NubbinBattery(last_service_date)
        return Car(engine, battery)

    def create_rorschach(self, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        return Car(engine, battery)

    def create_thovex(self, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        return Car(engine, battery)
