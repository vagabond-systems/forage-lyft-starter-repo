from tires.tires import Tires

class octoprimeTires(Tires):
    def __init__(self, tires_wear_sensors):
        self.tires_wear_sensors = tires_wear_sensors


    def needs_service(self):
        if self.tires_wear_sensors >=3:
            return True
        else:
            return False
