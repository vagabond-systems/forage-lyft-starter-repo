from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin import Nubbin
from battery.spindler import Spindler


class Factory(Car):
    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(self, CapuletEngine(current_mileage, last_service_mileage), Spindler(last_service_date, current_date))
    
    @staticmethod
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(self, WilloughbyEngine(current_mileage, last_service_mileage), Spindler(last_service_date, current_date))

    @staticmethod
    def create_palindrome(self, current_date, last_service_date, warning_indicator):
        return Car(self, SternmanEngine(warning_indicator), Spindler(last_service_date, current_date))

    @staticmethod
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(self, WilloughbyEngine(current_mileage, last_service_mileage), Nubbin(last_service_date, current_date))

    @staticmethod
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(self, CapuletEngine(current_mileage, last_service_mileage), Nubbin(last_service_date, current_date))
