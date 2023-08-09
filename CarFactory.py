from battery.spindlerBattery import SpindlerBattery
from battery.nubinBattery import NubinBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from car import Car
from datetime import date


class CarFactory:

    def create_calliope(current_service_date: date, last_service_date: date, current_service_mileage: int,
                        last_service_mileage) -> Car:
        engine = CapuletEngine(current_service_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_service_date)
        return Car(engine, battery)

    def create_glissade(current_service_date: date, last_service_date: date, current_service_mileage: int,
                        last_service_mileage) -> Car:
        engine = WilloughbyEngine(current_service_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_service_date)
        return Car(engine, battery)

    def create_palindrome(current_service_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_service_date)
        return Car(engine, battery)

    def create_rorschach(current_service_date: date, last_service_date: date, current_service_mileage: int,
                         last_service_mileage) -> Car:
        engine = WilloughbyEngine(current_service_mileage, last_service_mileage)
        battery = NubinBattery(last_service_date, current_service_date)
        return Car(engine, battery)

    def create_thovex(current_service_date: date, last_service_date: date, current_service_mileage: int,
                      last_service_mileage) -> Car:
        engine = CapuletEngine(current_service_mileage, last_service_mileage)
        battery = NubinBattery(last_service_date, current_service_date)
        return Car(engine, battery)
