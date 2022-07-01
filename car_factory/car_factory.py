from car.car import Car
from engine.capulet_engine import CapuletEngine
from engine.engine import Engine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from _datetime import datetime


class CarFactory:
    def create_calliope(self, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)

    def create_glissade(self, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)

    def create_palindrome(self, last_service_date, warning_light_on: bool) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)

    def create_rorschach(self, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        return Car(engine, battery)

    def create_thovex(self, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        return Car(engine, battery)

# today = datetime.today()
# last_service_date = today.replace(year=today.year - 3)
# current_mileage = 0
# last_service_mileage = 0
# facroty = CarFactory()
# car = facroty.create_thovex(today, current_mileage=current_mileage, last_service_mileage=last_service_mileage,
#              last_service_date=last_service_date)
# print(car.needs_service())
