from Car.serviceable import Serviceable 
from Engine import Engine
from Battery import Battery

class Car(Serviceable): 
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery
    
    def needs_service(self):
        if self.engine.needs_service == True or self.battery.needs_service == True:
            return True
        else:
            return False
