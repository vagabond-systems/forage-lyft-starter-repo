from car_factory import CarFactory
from model.serviceable import Serviceable

class Calliope(Serviceable):
    def __init__(self,current_date, last_service_date, current_mileage, last_service_mileage) -> None:
        self.__calliope = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
    def needs_service(self) -> bool:
        return self.__calliope.needs_service()

class Glissade(Serviceable): 
    def __init__(self,current_date, last_service_date, current_mileage, last_service_mileage) -> None:
        self.__glissade = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
    def needs_service(self) -> bool:
        return self.__glissade.needs_service();

class Palindrome(Serviceable): 
    def __init__(self,current_date, last_service_date, current_mileage, last_service_mileage) -> None:
        self.__palindrome = CarFactory.create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage)
    def needs_service(self) -> bool:
        return self.__palindrome.needs_service();

class Rorschach(Serviceable): 
    def __init__(self,current_date, last_service_date, current_mileage, last_service_mileage) -> None:
        self.__rorschach = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
    def needs_service(self) -> bool:
        return self.__rorschach.needs_service();

class Thovex(Serviceable): 
    def __init__(self,current_date, last_service_date, current_mileage, last_service_mileage) -> None:
        self.__thovex = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
    def needs_service(self) -> bool:
        return self.__thovex.needs_service();
