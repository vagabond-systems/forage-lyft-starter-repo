from cars import *
from engines import *
from batteries import *
from datetime import datetime, date

class CarFactory():
    def create_calliope(last_service_date: date, current_mileage: int, last_service_mileage: int, engine=CapuletEngine, battery=SpindlerBattery, current_date=datetime.date.today()):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage, engine, battery)

    def create_glissade(last_service_date: date, current_mileage: int, last_service_mileage: int, engine=WilloughbyEngine, battery=SpindlerBattery, current_date=datetime.date.today()):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage, engine, battery)

    def create_palindrome(last_service_date: date, current_mileage: int, last_service_mileage: int, engine=SternmanEngine, battery=SpindlerBattery, current_date=datetime.date.today()):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage, engine, battery)

    def create_rorschach(last_service_date: date, current_mileage: int, last_service_mileage: int, engine=WilloughbyEngine, battery=NubbinBattery, current_date=datetime.date.today()):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage, engine, battery)

    def create_thovex(last_service_date: date, current_mileage: int, last_service_mileage: int, engine=CapuletEngine, battery=NubbinBattery, current_date=datetime.date.today()):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage, engine, battery)
        