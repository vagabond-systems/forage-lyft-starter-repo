from datetime import datetime
from battery import *
from engine import *
from car import Car

class CarFactory():

    def create_Calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        Calliope = Car('1/1/2020', Capulet_Engine(last_service_date, current_mileage, last_service_mileage), Spindler_Battery(last_service_date))
    def create_Rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        Rorschach = Car('1/1/2020', Willoughby_Engine(last_service_date, current_mileage, last_service_mileage), Nubbin_Battery(last_service_date))
    def create_Glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        Glissade = Car('1/1/2020', Willoughby_Engine(last_service_date, current_mileage, last_service_mileage), Spindler_Battery(last_service_date))
    def create_Palindrome(self, current_date, last_service_date, current_mileage, last_service_mileage):
        Palindrome = Car('1/1/2020', Sternman_Engine(last_service_date, True), Spindler_Battery(last_service_date))
    def create_Thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        Thovex = Car('1/1/2020', Capulet_Engine(last_service_date, current_mileage, last_service_mileage), Nubbin_Battery(last_service_date))