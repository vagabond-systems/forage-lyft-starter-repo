from datetime import datetime
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tyre.carrigan_tyre import CarriganTyre
from tyre.octoprime_tyre import OctoprimeTyre

class CarFactory:
    def create_calliope(self, last_service_date, current_mileage, last_service_mileage, worn_counts):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        tyre = CarriganTyre(worn_counts)
        car = Car(engine, battery, tyre)
        return car

    def create_glissade(self, last_service_date, current_mileage, last_service_mileage, worn_counts):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        tyre = OctoprimeTyre(worn_counts)
        car = Car(engine, battery, tyre)
        return car

    def create_palindrome(self, last_service_date, warning_light_is_on, worn_counts):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date)
        tyre = CarriganTyre(worn_counts)
        car = Car(engine, battery, tyre)
        return car

    def create_rorschach(self, last_service_date, current_mileage, last_service_mileage, worn_counts):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tyre = OctoprimeTyre(worn_counts)
        car = Car(engine, battery, tyre)
        return car

    def create_thovex(self, last_service_date, current_mileage, last_service_mileage, worn_counts):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tyre = CarriganTyre(worn_counts)
        car = Car(engine, battery, tyre)
        return car








# carfactory = CarFactory()
# calliope = carfactory.create_calliope(datetime(2012,5,17).date(), 70000, 30000)
# print(calliope.needs_service())

