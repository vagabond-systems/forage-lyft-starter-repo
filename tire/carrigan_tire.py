import random

from tire.tire import Tire

class CarriganTire(Tire):
    
    def __init__(self):
        self.tire_sensor_readings = [random.random() for _ in range(4)]
    
    def needs_service(self):
        
        tire_sensor_readings = self.tire_sensor_readings
        
        if max(tire_sensor_readings) >= 0.9:
            return True
        return False

        
