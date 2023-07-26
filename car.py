from abc import ABC
from Engine_And_Battery import Serviceable
from battery.battery import Battery
from engine.engine import Engine


class Car(Serviceable):
    def __init__(self,engine:Engine,battery:Battery):
        self.engine = engine
        self.battery = battery
        
    def need_service(self) -> bool:
        return self.engine.need_service() or self.battery.need_service()
