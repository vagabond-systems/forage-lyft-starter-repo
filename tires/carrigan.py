from tires.tires import Tires

class carriganTires(Tires):
    def __init__(self, tires_wear_sensors):
        self.tires_wear_sensors = tires_wear_sensors


    def needs_service(self):
        if self.tires_wear_sensors >=0.9:
            return True
        else:
            return False
