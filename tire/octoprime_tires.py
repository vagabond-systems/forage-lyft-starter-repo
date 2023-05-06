import random

from tire.tire import Tire

class OctoprimeTire(Tire):
    
    def __init__(self):
        self.tire_sensor_readings = [random.random() for _ in range(4)]
    
    def needs_service(self):
        
        tire_sensor_readings = self.tire_sensor_readings
        
        if sum(tire_sensor_readings) >= 3:
            return True
        return False

        
