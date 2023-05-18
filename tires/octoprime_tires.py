from tires.tires import Tire

class OctoprimeTires(Tire):
    def __init__(self, front_left, front_right, back_left, back_right):
        self.tires = [front_left, front_right, back_left, back_right]

    def needs_service(self):
        value = 0
        for tire in self.tires:
            value += tire
            if value >= 3:
                return True
        
        return False
        
        