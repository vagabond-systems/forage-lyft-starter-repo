#  import battery modules
#  import engine modules
#  import car object

from battery.spindler_battery import spindler_battery
from battery.nubbin_battery import nubbin_battery

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from car import Car

class car_factory():
    @staticmethod
    def Calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = spindler_battery(last_service_date, current_date)
        return Car(engine, battery)

    #  Ques: why do we use static method?

    @staticmethod
    def Glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = spindler_battery(last_service_date, current_date)
        return Car(engine, battery)
    
    @staticmethod
    def Palindrome(current_date, last_service_date, current_mileage, last_service_mileage):
            engine = SternmanEngine(current_mileage, last_service_mileage)
            battery = spindler_battery(last_service_date, current_date)
            return Car(engine, battery)
    
    @staticmethod
    def Rohrschach(current_date, last_service_date, current_mileage, last_service_mileage):
            engine = CapuletEngine(current_mileage, last_service_mileage)
            battery = nubbin_battery(last_service_date, current_date)
            return Car(engine, battery) 
    
    @staticmethod
    def Thovex(current_date, last_service_date, current_mileage, last_service_mileage):
            engine = CapuletEngine(current_mileage, last_service_mileage)
            battery = nubbin_battery(last_service_date, current_date)
            return Car(engine, battery)    
    