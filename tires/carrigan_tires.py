from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tirewearreading):
        self.tirewearreading = tirewearreading

    def needs_service(self):
        for a in self.tirewearreading:
            if a>= 0.9:
                return True
        return False
