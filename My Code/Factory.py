from Car import *

class CarFactory():
    
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_palindrome(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)
        