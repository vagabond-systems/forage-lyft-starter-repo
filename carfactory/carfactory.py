from car import Car 
from battery.model.nubin import NubinBattery
from engine.model.capulet_engine import CapuletEngine 


class CarFactory:
    @staticmethod
    def create_thovex(current_date, last_service_date, current_milage, last_service_mileage):
        engine = CapuletEngine(current_mileage=current_milage, last_service_mileage=last_service_mileage)
        battery = NubinBattery(current_date=current_date, last_service_date=last_service_date)
        car = Car(engine=engine, battery=battery)
        return car
