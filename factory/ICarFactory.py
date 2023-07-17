from abc import ABC, abstractstaticmethod
from car.Car import Car


class ICarFactory(ABC):
    
    @abstractstaticmethod    
    def create_car(engine, battery) -> Car:
        pass