from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler import SpindlerBattery
from battery.nubbin import NubbinBattery

class carFactory(Car):
    
    def create_callope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(self, CapuletEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date))

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(self, WilloughbyEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date))

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        return Car(self, SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date))

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(self, WilloughbyEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date))

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(self, CapuletEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date))