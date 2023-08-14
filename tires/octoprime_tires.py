from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tirewearreading):
        self.tirewearreading = tirewearreading

    def needs_service(self):
        return sum(self.tirewearreading) >= 3.0
