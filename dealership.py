class Dealership:
    def __init__(self, name, cars):
        self.name = name
        self.cars = cars

    def get_name(self):
        return self.name

    def get_cars(self):
        return self.cars

    def add_car(self, car):
        self.cars.append(car)

    def sell_car(self, car):
        self.cars.remove(car)

    def __str__(self):
        return f"{self.name} has {len(self.cars)} cars"
