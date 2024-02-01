from abc import ABC, abstractmethod
from datetime import datetime
from car import Car 
from battery import BatteryInterface 
from engine import Engine 


class CarFactory(ABC):
    def __init__(self):
        create_car1 = Car(Engine(), BatteryInterface())
