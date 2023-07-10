from car import Car

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class CarFactory(Car):
    """
    A factory class for creating different types of cars.

    This factory class provides static methods to create instances of various car models
    with different engine and battery combinations. Each method takes specific parameters
    to configure the car based on the desired model and its current status.

    Note: The class assumes that the imported modules (car, engine, battery) exist in the project.
    """
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        calliope = Car(battery, engine)
        
        return calliope
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        glissade = Car(battery, engine)
        
        return glissade

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        battery = SpindlerBattery(last_service_date, current_date)
        palindrome = Car(battery, engine)
        
        return palindrome

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        rorschach = Car(battery, engine)
        
        return rorschach

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        thovex = Car(battery, engine)
        
        return thovex
