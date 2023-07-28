from car.car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


# factory to create cars
class CarFactory:
    def create_calliope(self, last_service_date, current_mileage: int, last_service_mileage: int, tires_condition: []) \
            -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        tires = CarriganTires(tires_condition)

        return Car(engine, battery, tires)

    def create_glissade(self, last_service_date, current_mileage: int, last_service_mileage: int, tires_condition: []) \
            -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        tires = CarriganTires(tires_condition)
        return Car(engine, battery, tires)

    def create_palindrome(self, last_service_date, warning_light_on: bool, tires_condition: []) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date)
        tires = OctoprimeTires(tires_condition)
        return Car(engine, battery, tires)

    def create_rorschach(self, last_service_date, current_mileage: int, last_service_mileage: int, tires_condition: []
                         ) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tires = OctoprimeTires(tires_condition)
        return Car(engine, battery, tires)

    def create_thovex(self, last_service_date, current_mileage: int, last_service_mileage: int, tires_condition: []) \
            -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tires = OctoprimeTires(tires_condition)
        return Car(engine, battery, tires)

