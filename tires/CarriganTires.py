from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self,tire_wear):
        self.tire_wear = tire_wear
        self.tire_need_service = 0.9
    
    def need_service(self) -> bool:
        for tire in self.tire_wear:
            if tire >= self.tire_need_service:
                return True
        return False
        
        