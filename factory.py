from car import Car
from capulete_engine import CapuletEngine
from sternman_engine import SternmanEngine
from willoughby_engine import WilloughbyEngine
from nubbin import Nubbin
from spindler import Spindler


class Factory(Car):
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(self, CapuletEngine, Spindler)
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(self, WilloughbyEngine, Spindler)

    def create_palindrome(self, current_date, last_service_date, warning_indicator):
        return Car(self, SternmanEngine, Spindler)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(self, WilloughbyEngine, Nubbin)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(self, CapuletEngine, Nubbin)
