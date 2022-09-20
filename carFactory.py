from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler import SpindlerBattery
from battery.nubbin import NubbinBattery
from tires.carrigan import Carrigan
from tires.octoprime import Octoprime

class carFactory(Car):
    
    def create_callope(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Car(self, CapuletEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date), Carrigan(tire_wear))

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Car(self, WilloughbyEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date), Octoprime(tire_wear))

    def create_palindrome(self, current_date, last_service_date, warning_light_on, tire_wear):
        return Car(self, SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date), Carrigan(tire_wear))

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Car(self, WilloughbyEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date), Octoprime(tire_wear))

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Car(self, CapuletEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date), Carrigan(tire_wear))