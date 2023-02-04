from Car import *
from Engine import *
from Battery import *
from datetime import datetime

class CarFactory():
    
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, CapuletEngine(), SpindlerBattery()):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, WilloughbyEngine(), SpindlerBattery()):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_palindrome(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, SternmanEngine(), SpindlerBattery()):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, WilloughbyEngine(), NubbinBattery()):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, CapuletEngine(), NubbinBattery()):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)
        