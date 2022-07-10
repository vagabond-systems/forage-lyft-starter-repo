from engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from battery import SpindlerBattery, NubbinBattery
from .car import Car

class CarFactory:
    def __init__(self, last_service_date, current_mileage, last_service_mileage, warning_light_on=False):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_date = last_service_date
        self.warning_light_on = warning_light_on
        self.last_service_mileage = last_service_mileage

    def create_calliope(self):
        engine = CapuletEngine(self.current_mileage, self.last_service_mileage)
        battery = SpindlerBattery(self.last_service_date, self.current_date)
        calliope = Car(engine, battery)
        return calliop

    def create_glissade(self):
        engine = WilloughbyEngine(self.current_mileage, self.last_service_mileage)
        battery = SpindlerBattery(self.last_service_date, self.current_date)
        willoughby = Car(engine, battery)
        return willoughby

    def create_palindrome(self):
        engine = SternmanEngine(self.warning_light_is_on)
        battery = SpindlerBattery(self.last_service_date, self.current_date)
        palindrome = Car(engine, battery)
        return palindrome

    def create_rorschach(self):
        engine = WilloughbyEngine(self.current_mileage, self.last_service_mileage)
        battery = NubbinBattery(self.last_service_date, self.current_date)
        rorschach = Car(engine, battery)
        return rorschach

    def create_thovex(self):
        engine = CapuletEngine(self.current_mileage, self.last_service_mileage)
        battery = NubbinBattery(self.last_service_date, self.current_date)
        thovex = Car(engine, battery)
        return thovex