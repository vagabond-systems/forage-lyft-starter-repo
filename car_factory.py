from datetime import datetime
from engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from battery import SpindlerBattery, NubbinBattery
from car import Car

class CarFactory:
    @staticmethod
    def create_calliope(current_mileage, last_service_mileage, last_service_date):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(current_mileage,last_service_mileage, last_service_date):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(datetime.today().date())  # Assume new battery for Palindrome
        return Car(engine, battery)

    @staticmethod
    def create_rorschach(current_mileage, last_service_mileage, last_service_date):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        return Car(engine, battery)

    @staticmethod
    def create_thovex(current_mileage, last_service_mileage, last_service_date):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        return Car(engine, battery)
