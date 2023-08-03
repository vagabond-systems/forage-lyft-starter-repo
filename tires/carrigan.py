from tires.tires import Tires

class carriganTires(Tires):
    def __init__(self, tires_wear_sensors):
        self.tires_wear_sensors = tires_wear_sensors


    def needs_service(self):
        for tire in self.tires_wear_sensors:
            if tire >=0.9:
                return True
        
        return False
