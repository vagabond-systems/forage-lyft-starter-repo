from cars import *
from engines import *
from batteries import *
from datetime import datetime, date

class CarFactory():
    
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, CapuletEngine(), SpindlerBattery()):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage, CapuletEngine(), SpindlerBattery())

    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, WilloughbyEngine(), SpindlerBattery()):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage, WilloughbyEngine(), SpindlerBattery())

    def create_palindrome(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, SternmanEngine(), SpindlerBattery()):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage, SternmanEngine(), SpindlerBattery())

    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, WilloughbyEngine(), NubbinBattery()):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage, WilloughbyEngine(), NubbinBattery())

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, CapuletEngine(), NubbinBattery()):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage, CapuletEngine(), NubbinBattery())
        