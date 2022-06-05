from battery.nubbinBattery import NubbinBattery
from battery.spindlerBattery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


# dates are arrays formatted in (YY, MM, DD) order

class CarFactory():

    @staticmethod
    def create_Calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        Calliope = Car('1/1/2020', CapuletEngine(last_service_date, current_mileage, last_service_mileage),
                       SpindlerBattery(last_service_date, current_date))
        return Calliope

    @staticmethod
    def create_Rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        Rorschach = Car('1/1/2020', WilloughbyEngine(last_service_date, current_mileage, last_service_mileage),
                        NubbinBattery(last_service_date, current_date))
        return Rorschach

    @staticmethod
    def create_Glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        Glissade = Car('1/1/2020', WilloughbyEngine(last_service_date, current_mileage, last_service_mileage),
                       SpindlerBattery(last_service_date, current_date))
        return Glissade

    @staticmethod
    def create_Palindrome(current_date, last_service_date, current_mileage, last_service_mileage):
        Palindrome = Car('1/1/2020', SternmanEngine(last_service_date, True),
                         SpindlerBattery(last_service_date, current_date))

        return Palindrome

    @staticmethod
    def create_Thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        Thovex = Car('1/1/2020', CapuletEngine(last_service_date, current_mileage, last_service_mileage),
                     NubbinBattery(last_service_date, current_date))

        return Thovex
