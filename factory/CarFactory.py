from car.Calliope import Calliope
from car.Car import Car
from car.Glissade import Glissade
from car.Palindrome import Palindrome
from car.Rorschach import Rorschach
from car.Thovex import Thovex
from ICarFactory import ICarFactory
from factory.BatteryFactory import BatteryFactory
from factory.EngineFactory import EngineFactory


class CarFactory(ICarFactory):
    
    @staticmethod
    def create_a_car(car_type, engine_type, battery_type, last_service_date, last_service_mileage, 
                        current_mileage, current_date, warning_light_on) -> Car :
        
        an_engine = EngineFactory.create_engine(engine_type, last_service_mileage, current_mileage, warning_light_on)
        a_battery = BatteryFactory.create_battery(battery_type, last_service_date, current_date)
            
        if (car_type.capitalize() == 'Calliope'):
            return Calliope(an_engine, a_battery, last_service_date)
        elif (car_type.capitalize() == 'Glissade'):
            return Glissade(an_engine, a_battery, last_service_date)
        elif (car_type.capitalize() == 'Palindrome'):
            return Palindrome(an_engine, a_battery, last_service_date)
        elif (car_type.capitalize() == 'Rorschach'):
            return Rorschach(an_engine, a_battery, last_service_date)
        elif (car_type.capitalize() == 'Thovex'):
            return Thovex(an_engine, a_battery, last_service_date)
        else: 
            raise ValueError("Wrong type of car.")
        
        