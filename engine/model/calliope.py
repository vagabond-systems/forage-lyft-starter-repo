from car.car import Car


class Calliope(Car):
    def __init__(self, engine, battery):
        super().__init__(engine, battery) # giving this to the car
        
    