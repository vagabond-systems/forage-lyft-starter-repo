from datetime import *
from car import Car
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CarFactory:
    @staticmethod
    def create_calliope(current_date: date,  last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        battery = SpindlerBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_glissade(current_date: date,  last_service_date: date, current_mileage: int, last_service_mileage: int):
        battery = SpindlerBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_palindrome(current_date: date,  last_service_date: date, warning_light_on: bool):
        battery = SpindlerBattery(current_date, last_service_date)
        engine = SternmanEngine(warning_light_on)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_rorschach(current_date: date,  last_service_date: date, current_mileage: int, last_service_mileage: int):
        battery = NubbinBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_thovex(current_date: date,  last_service_date: date, current_mileage: int, last_service_mileage: int):
        battery = NubbinBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        car = Car(engine, battery)
        return car
