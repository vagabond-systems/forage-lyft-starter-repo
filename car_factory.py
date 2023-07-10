from car import Car

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class CarFactory(Car):
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        calliope = Car(battery, engine)
        
        return calliope
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        glissade = Car(battery, engine)
        
        return glissade

    def create_palindrome(self, current_date, last_service_date, waning_light_on):
        engine = SternmanEngine(last_service_date, waning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        palindrome = Car(battery, engine)
        
        return palindrome

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        rorschach = Car(battery, engine)
        
        return rorschach

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        thovex = Car(battery, engine)
        
        return thovex
