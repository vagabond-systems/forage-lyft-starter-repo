from tires.tires import Tire

class CarriganTires(Tire):
    def __init__(self, front_left, front_right, back_left, back_right):
        self.tires = [front_left, front_right, back_left, back_right]

    def needs_service(self):
        for tire in self.tires:
            if tire >= 0.9:
                return True
        
        return False
        
        