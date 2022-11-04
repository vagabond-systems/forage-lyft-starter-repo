from tires import Tires

class Carrigan(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear


    def needs_service(self):
        if self.tire_wear >= 0.9:
            return True
        else:
            return False